extends Node
## Localization Pack for Melvor Idle 2: runtime helper.
##
## Godot translates most texts itself through the .po files. Some texts, however, are assembled in the
## game's C# code ("3 Turns", "10 minutes", "Stab, Slash") or set on controls without automatic
## translation. This script checks visible texts and replaces remaining English text.
## It only works while one of this pack's languages is selected and restores the original text when
## switching back. Always active: renaming the language buttons to the language's own name.
## It does not change game files or save games.

const MOD_DIR := "Mods/Localization Pack"
const CHECKS_PER_FRAME := 200   # known text controls re-checked per frame
const MAX_TEMPLATE_LEN := 200   # longer texts are not used as patterns
const LOG_IGNORE := ["Games by Malcs (C)"]  # texts that stay English on purpose (start of text)

var _languages: PackedStringArray = []    # language codes of this pack, e.g. ["de"]
var _loading_label: Control
const LOADING_MESSAGES := ["Loading...", "Loading Game View...", "Loading Offline Progress...", "Loading Save...", "Preloading Base Game Data...", "Loading Entity Resources...", "Loading Data Editor..."]
var _loading_messages := {}
var _log_missing := false
var _log_file: FileAccess
var _logged := {}

var _active := ""          # currently active pack language ("" = off)
var _nodes: Array = []     # tracked text controls (WeakRef)
var _queue: Array = []     # newly added controls
var _pos := 0
var _written := {}         # instance_id -> text we wrote last
var _original := {}        # instance_id -> original English text
var _wrap_modes := {}      # instance_id -> [control, original autowrap mode] (wrap_anywhere only)
var _cache := {}
var _templates := {}       # keyword -> array of {re, tokens, dst}
var _rich_sources := {}
var _rich_style := RegEx.create_from_string("\\[(?:/?b|/color|color=(?:#[0-9A-Fa-f]+|[A-Za-z]+))\\]")
var _rich_icon := RegEx.create_from_string("\\[img(?: [^\\]]*)?\\]res://[^\\[]+\\[/img\\]")
var _less_than_prefix := RegEx.create_from_string("(?i)less than\\s+$")
var _units := {}           # language -> settings from mod.json (time units etc.)
var _lang_names := {}      # Godot's English language name -> display name ("German, Germany" -> "Deutsch, Deutschland")
var _words_en := {}        # words from English source texts (log_missing only)
var _words_tr := {}        # words from translations (log_missing only)
var _re_digits := RegEx.create_from_string("\\d[\\d.,]*")

var _re_latin := RegEx.create_from_string("[A-Za-z]{3,}")
var _re_word := RegEx.create_from_string("[A-Za-z]{4,}")
var _re_token := RegEx.create_from_string("\\{[^{}]+\\}")
var _re_unit: RegEx      # number + time unit in English or any pack language (built in _read_config)
var _unit_words := {}     # lower-case unit word -> unit key ("sekunden" -> "second")


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	process_priority = 100
	_read_config()
	get_tree().node_added.connect(_on_node_added)
	_add_tree(get_tree().root)


func _read_config() -> void:
	var base := OS.get_executable_path().get_base_dir().path_join(MOD_DIR)
	var f := FileAccess.open(base.path_join("mod.json"), FileAccess.READ)
	if f == null:
		push_warning("Localization Pack: mod.json not found in " + base)
		return
	var cfg = JSON.parse_string(f.get_as_text())
	if typeof(cfg) != TYPE_DICTIONARY:
		push_warning("Localization Pack: mod.json is not valid JSON")
		return
	for lang in cfg.get("languages", {}):
		_languages.append(lang)
		var catalog := TranslationServer.get_translation_object(lang)
		if catalog != null:
			for source in LOADING_MESSAGES:
				_loading_messages[source] = source
				var translated := String(catalog.get_message(source))
				if not translated.is_empty():
					_loading_messages[translated] = source
		var native: String = cfg.languages[lang].get("display", cfg.languages[lang].get("name", ""))
		if not native.is_empty():  # otherwise the language list shows Godot's English name ("German, Germany")
			_lang_names[TranslationServer.get_locale_name(lang)] = native
			_lang_names[TranslationServer.get_language_name(lang.get_slice("_", 0))] = native
	_units = cfg.get("languages", {})
	# The game formats durations in the Windows language, not the game language, so accept unit words
	# of English and of every pack language and replace them with the active language's words.
	for unit in ["day", "hour", "minute", "second", "turn"]:
		_unit_words[unit] = unit
		_unit_words[unit + "s"] = unit
	for lang in _units:
		var names: Dictionary = _units[lang].get("units", {})
		for unit in names:
			for form in names[unit]:
				_unit_words[String(form).to_lower()] = unit
	var words := _unit_words.keys()
	words.sort_custom(func(a, b): return a.length() > b.length())
	var alternatives := PackedStringArray()
	for w in words:
		alternatives.append(_escape(w))
	_re_unit = RegEx.create_from_string("(?i)(?<![\\p{Latin}\\d])(\\d+(?:[.,]\\d+)?) ?(" + "|".join(alternatives) + ")(?!\\p{Latin})")
	_log_missing = cfg.get("log_missing", false)
	print("Localization Pack %s loaded, languages: %s" % [cfg.get("version", "?"), ", ".join(_languages)])


func _process(_delta: float) -> void:
	if is_instance_valid(_loading_label):
		_update_loading_message(_loading_label)
	var lang := _pack_language(TranslationServer.get_locale())
	if lang != _active:
		if _active != "":
			_restore_all()
		_active = lang
		_cache.clear()
		_written.clear()
		if lang != "":
			_build_templates(lang)
		_refresh_language_views()
	for n in _queue:
		_check(n)
	_queue.clear()
	var count := mini(CHECKS_PER_FRAME, _nodes.size())
	for i in count:
		if _pos >= _nodes.size():
			_pos = 0
		var n = _nodes[_pos].get_ref()
		if n == null:
			_nodes.remove_at(_pos)
		else:
			_check(n)
			_pos += 1


func _pack_language(locale: String) -> String:
	for lang in _languages:
		# Same language part is enough: a saved setting "de" still activates the pack language "de_DE"
		if locale.get_slice("_", 0) == lang.get_slice("_", 0):
			return lang
	return ""


func _add_tree(n: Node) -> void:
	_on_node_added(n)
	for c in n.get_children():
		_add_tree(c)


func _on_node_added(n: Node) -> void:
	if n is Control and "TimeUpdateTimer" in n and "LastSavedTime" in n and "LastCloudSavedTime" in n:
		if n.is_node_ready():
			_bind_save_times(n)
		else:
			n.ready.connect(_bind_save_times.bind(n), CONNECT_ONE_SHOT)
	elif n is PanelContainer and n.has_method("UpdatePurchaseQuantity") and "_purchaseQuantity" in n:
		n.add_to_group(&"LocalizationPackShopCards")
	elif n is Control and n.has_method("PopulateCategoryList") and "ShowHiddenCheckBox" in n and n.has_method("Update"):
		n.add_to_group(&"LocalizationPackCategoryFilters")
	elif n is Control and n.has_method("UpdateStats") and "AccuracyStanceLabel" in n:
		n.add_to_group(&"LocalizationPackOffensiveStats")
	if n is Label or n is RichTextLabel or n is Button:
		if n.name == &"Message" and n.get_path() == ^"/root/Main/LoadingScreen/ColorRect/Message":
			_loading_label = n
		_nodes.append(weakref(n))
		_queue.append(n)


func _bind_save_times(menu: Control) -> void:
	var timer: Timer = menu.get("TimeUpdateTimer")
	var local_time: Label = menu.get("LastSavedTime")
	var cloud_time: Label = menu.get("LastCloudSavedTime")
	if timer == null or local_time == null or cloud_time == null:
		return
	var refresh := _refresh_save_times.bind(local_time, cloud_time)
	if not timer.timeout.is_connected(refresh):
		timer.timeout.connect(refresh, CONNECT_DEFERRED)
	if not menu.visibility_changed.is_connected(refresh):
		menu.visibility_changed.connect(refresh, CONNECT_DEFERRED)


func _refresh_save_times(local_time: Label, cloud_time: Label) -> void:
	_check(local_time)
	_check(cloud_time)


func _refresh_language_views() -> void:
	for card in get_tree().get_nodes_in_group(&"LocalizationPackShopCards"):
		var quantity: int = card.get("_purchaseQuantity")
		if card.is_node_ready() and quantity >= 0:
			card.set("_purchaseQuantity", -1)
			card.call("UpdatePurchaseQuantity")
			if card.get("_purchaseQuantity") == -1:
				card.set("_purchaseQuantity", quantity)
	for view in get_tree().get_nodes_in_group(&"LocalizationPackCategoryFilters"):
		if view.is_node_ready():
			view.call("Update")
	for view in get_tree().get_nodes_in_group(&"LocalizationPackOffensiveStats"):
		if view.is_node_ready():
			view.call("UpdateStats")


func _update_loading_message(n) -> void:
	if not n.is_visible_in_tree() or not _loading_messages.has(n.text):
		return
	var loading := String(TranslationServer.translate(_loading_messages[n.text]))
	if n.text != loading:
		n.text = loading


func _check(n) -> void:
	if not is_instance_valid(n) or not n.is_visible_in_tree():
		return
	if _active != "":
		_apply_wrap(n)
	var s: String = n.text
	if s.is_empty():
		if _active != "" and n is RichTextLabel and n.name in [&"Description", &"CustomDescription", &"InstructionLabel"]:
			var rendered: String = n.get_parsed_text()
			var rich_id: int = n.get_instance_id()
			if _written.get(rich_id) == rendered:
				return
			_written[rich_id] = rendered
			_original.erase(rich_id)
			var source: String = _rich_sources.get(rendered, rendered)
			var translated := _t(source)
			if translated != source:
				_original[rich_id] = source
				_written[rich_id] = translated
				n.text = translated
		return
	if n is Button and _lang_names.has(s):
		n.text = _lang_names[s]
		return
	if _active == "":
		return
	var id: int = n.get_instance_id()
	if _written.get(id, "") == s:
		return
	var t := _convert(s)
	if t != s:
		_original[id] = s
		n.text = t
	else:
		_original.erase(id)
	_written[id] = t


# Languages without spaces (wrap_anywhere in mod.json) never break at word boundaries, so long
# texts run past their box. Let word-wrapping controls break anywhere while such a language is active.
func _apply_wrap(n) -> void:
	if not _units.get(_active, {}).get("wrap_anywhere", false) or not "autowrap_mode" in n:
		return
	var mode: int = n.autowrap_mode
	if mode == TextServer.AUTOWRAP_WORD or mode == TextServer.AUTOWRAP_WORD_SMART:
		_wrap_modes[n.get_instance_id()] = [weakref(n), mode]
		n.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY


func _restore_all() -> void:
	for entry in _wrap_modes.values():
		var c = entry[0].get_ref()
		if c != null and c.autowrap_mode == TextServer.AUTOWRAP_ARBITRARY:
			c.autowrap_mode = entry[1]
	_wrap_modes.clear()
	for ref in _nodes:
		var n = ref.get_ref()
		if n == null:
			continue
		var id: int = n.get_instance_id()
		if _original.has(id) and n.text == _written.get(id, ""):
			n.text = _original[id]
	_original.clear()


func _convert(s: String) -> String:
	if _cache.has(s):
		return _cache[s]
	var t := _translate(s)
	if _cache.size() > 20000:
		_cache.clear()
	_cache[s] = t
	if _log_missing and t == s and _looks_english(s) and not _ignored(s):
		var key := _re_digits.sub(s, "#", true)  # report counters like "(5 / 11,258)" only once
		if not _logged.has(key):
			_logged[key] = true
			_log_line(s)
	return t


func _ignored(s: String) -> bool:
	for prefix in LOG_IGNORE:
		if s.begins_with(prefix):
			return true
	return false


## More words that only occur in English source texts than words that only occur in translations.
func _looks_english(s: String) -> bool:
	var en := 0
	var other := 0
	for m in _re_latin.search_all(s):
		var w := m.get_string().to_lower()
		var in_en := _words_en.has(w)
		var in_tr := _words_tr.has(w)
		if in_en and not in_tr:
			en += 1
		elif in_tr and not in_en:
			other += 1
	return en > other


func _translate(s: String) -> String:
	if not _re_latin.search(s):
		return s
	var t := _t(s)
	if t != s:
		return t
	var core := s.strip_edges()
	if core != s and _t(core) != core:
		return s.replace(core, _t(core))
	if ", " in core:
		var parts := core.split(", ")
		var out := PackedStringArray()
		for p in parts:
			var tp := _t(p)
			if tp == p:
				break
			out.append(tp)
		if out.size() == parts.size():
			return s.replace(core, ", ".join(out))
	t = _from_template(core)
	if t != core:
		return s.replace(core, _replace_units(t))
	return _replace_units(s)


## Build patterns from all translated entries with placeholders, e.g. "{0:N0} Unlocks Available".
func _build_templates(lang: String) -> void:
	_templates.clear()
	_rich_sources.clear()
	var trans := TranslationServer.get_translation_object(lang)
	if trans == null:
		return
	_words_en.clear()
	_words_tr.clear()
	for src in trans.get_message_list():
		var dst := String(trans.get_message(src))
		if "[" in src and "{" not in src and dst != src:
			var plain := _rich_style.sub(_rich_icon.sub(src, " ", true), "", true)
			if plain != src and "[" not in plain and not _rich_sources.has(plain):
				_rich_sources[plain] = src
		if _log_missing:
			for m in _re_latin.search_all(src):
				_words_en[m.get_string().to_lower()] = true
			for m in _re_latin.search_all(dst):
				_words_tr[m.get_string().to_lower()] = true
		if src.length() > MAX_TEMPLATE_LEN or not "{" in src:
			continue
		if dst.is_empty() or dst == src:
			continue
		var pattern := "^"
		var tokens := []
		var literal := ""
		var pos := 0
		for m in _re_token.search_all(src):
			var lit := src.substr(pos, m.get_start() - pos)
			pattern += _escape(lit) + "(.+?)"
			literal += lit + " "
			tokens.append(m.get_string())
			pos = m.get_end()
		pattern += _escape(src.substr(pos)) + "$"
		literal += src.substr(pos)
		var key := ""
		for w in _re_word.search_all(literal):
			if w.get_string().length() > key.length():
				key = w.get_string()
		if key.is_empty() or tokens.is_empty():
			continue
		var re := RegEx.new()
		if re.compile(pattern) != OK:
			continue
		key = key.to_lower()
		if not _templates.has(key):
			_templates[key] = []
		_templates[key].append({"re": re, "tokens": tokens, "dst": dst})


func _from_template(s: String) -> String:
	var tried := {}
	for w in _re_word.search_all(s):
		var key := w.get_string().to_lower()
		if tried.has(key) or not _templates.has(key):
			continue
		tried[key] = true
		for tpl in _templates[key]:
			var m: RegExMatch = tpl.re.search(s)
			if m == null:
				continue
			var out: String = tpl.dst
			for i in tpl.tokens.size():
				var v := m.get_string(i + 1)
				out = out.replace(tpl.tokens[i], _t(v))
			return out
	return s


## "10 minutes" or "10 Minuten" -> words of the active language, using the units from mod.json.
func _replace_units(s: String) -> String:
	var names: Dictionary = _units.get(_active, {}).get("units", {})
	if names.is_empty() or _re_unit == null:
		return s
	var matches := _re_unit.search_all(s)
	var out := s
	var separator: String = _units[_active].get("unit_separator", " ")
	var less_than: String = _units[_active].get("less_than", "")
	for i in range(matches.size() - 1, -1, -1):
		var m: RegExMatch = matches[i]
		var unit: String = _unit_words.get(m.get_string(2).to_lower(), "")
		if not names.has(unit):
			continue
		var forms: Array = names[unit]
		var one := m.get_string(1) == "1"
		var value := m.get_string(1) + separator + String(forms[0 if one else 1])
		var prefix := out.substr(0, m.get_start())
		if not less_than.is_empty():
			var qualifier := _less_than_prefix.search(prefix)
			if qualifier != null:
				prefix = prefix.substr(0, qualifier.get_start())
				value = less_than.replace("{0}", value)
		out = prefix + value + out.substr(m.get_end())
	return out


func _escape(s: String) -> String:
	var out := ""
	for c in s:
		if c in "\\.^$|?*+()[]{}":
			out += "\\"
		out += c
	return out


func _log_line(s: String) -> void:
	if _log_file == null:
		# Append across game sessions; tools/add_texts.py --missing collects the file later.
		var path := "user://localization_pack_missing.txt"
		if FileAccess.file_exists(path):
			_log_file = FileAccess.open(path, FileAccess.READ_WRITE)
			if _log_file != null:
				_log_file.seek_end()
		else:
			_log_file = FileAccess.open(path, FileAccess.WRITE)
		if _log_file == null:
			_log_missing = false
			return
	_log_file.store_line(s.c_escape())
	_log_file.flush()


func _t(s: String) -> String:
	return String(TranslationServer.translate(s))
