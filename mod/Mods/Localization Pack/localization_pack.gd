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
var _log_missing := false
var _log_file: FileAccess
var _logged := {}

var _active := ""          # currently active pack language ("" = off)
var _nodes: Array = []     # tracked text controls (WeakRef)
var _queue: Array = []     # newly added controls
var _pos := 0
var _written := {}         # instance_id -> text we wrote last
var _original := {}        # instance_id -> original English text
var _cache := {}
var _templates := {}       # keyword -> array of {re, tokens, dst}
var _units := {}           # language -> settings from mod.json (time units etc.)
var _lang_names := {}      # Godot's English language name -> native name ("German" -> "Deutsch")
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
		var native: String = cfg.languages[lang].get("name", "")
		if not native.is_empty():  # otherwise the language list shows Godot's English name ("German")
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
	_re_unit = RegEx.create_from_string("(?i)\\b(\\d+(?:[.,]\\d+)?) ?(" + "|".join(alternatives) + ")(?!\\p{L})")
	_log_missing = cfg.get("log_missing", false)
	print("Localization Pack %s loaded, languages: %s" % [cfg.get("version", "?"), ", ".join(_languages)])


func _process(_delta: float) -> void:
	var lang := _pack_language(TranslationServer.get_locale())
	if lang != _active:
		if _active != "":
			_restore_all()
		_active = lang
		_cache.clear()
		_written.clear()
		if lang != "":
			_build_templates(lang)
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
		if locale == lang or locale.begins_with(lang + "_"):
			return lang
	return ""


func _add_tree(n: Node) -> void:
	_on_node_added(n)
	for c in n.get_children():
		_add_tree(c)


func _on_node_added(n: Node) -> void:
	if n is Label or n is RichTextLabel or n is Button:
		_nodes.append(weakref(n))
		_queue.append(n)


func _check(n) -> void:
	if not is_instance_valid(n) or not n.is_visible_in_tree():
		return
	var s: String = n.text
	if s.is_empty():
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
		if not _original.has(id):
			_original[id] = s
		n.text = t
	_written[id] = t


func _restore_all() -> void:
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
	var trans := TranslationServer.get_translation_object(lang)
	if trans == null:
		return
	_words_en.clear()
	_words_tr.clear()
	for src in trans.get_message_list():
		var dst := String(trans.get_message(src))
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
	for i in range(matches.size() - 1, -1, -1):
		var m: RegExMatch = matches[i]
		var unit: String = _unit_words.get(m.get_string(2).to_lower(), "")
		if not names.has(unit):
			continue
		var forms: Array = names[unit]
		var one := m.get_string(1) == "1"
		out = out.substr(0, m.get_start()) + m.get_string(1) + " " + forms[0 if one else 1] + out.substr(m.get_end())
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
		# Append across game sessions; tools/import_missing.py collects the file later.
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
