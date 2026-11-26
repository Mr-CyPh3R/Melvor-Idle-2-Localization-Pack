"""Baut dist/<locale>.po (Locale-Code aus mod.json, z. B. de_DE) aus der Vorlage und den Übersetzungen in work/<lang>/*.json und prüft die Platzhalter.

Aufruf (im Projektordner): python tools/build.py [--lang de] [--check]   (Standard: de)
work/<lang>/*.json: {id: "Text"} oder bei Pluralen {id: ["Einzahl", "Mehrzahl"]} (so viele Formen, wie "plural_forms" in mod.json verlangt, Polnisch 3)
Exit 1, wenn eine Übersetzung Platzhalter, Tags oder Zeilenumbrüche verändert.
Installieren ins Spiel: python tools/package.py --install
"""
import collections, gettext, glob, json, os, re, sys, polib

BRACE = re.compile(r'\{[^{}]*\}')
TAG = re.compile(r'\[/?[A-Za-z_]+[^\]]*\]')
COND = re.compile(r'^\{([^:{}]+):(cond|plural|choose):')


def signature(text):
    """Was in einer Übersetzung gleich bleiben muss."""
    braces = []
    for b in BRACE.findall(text):
        m = COND.match(b)
        braces.append(f'{{{m.group(1)}:{m.group(2)}:…}}' if m else b)  # Wörter in cond/plural dürfen übersetzt werden
    return (collections.Counter(braces), collections.Counter(TAG.findall(text)), text.count('\n'))


def check(en, de):
    if not isinstance(de, str) or not de.strip():
        return 'leer'
    a, b = signature(en), signature(de)
    if a[0] != b[0]:
        return f'Platzhalter {dict(a[0] - b[0])} fehlen / {dict(b[0] - a[0])} zu viel'
    if a[1] != b[1]:
        return f'Tags {dict(a[1] - b[1])} fehlen / {dict(b[1] - a[1])} zu viel'
    if a[2] != b[2]:
        return f'Zeilenumbrüche {a[2]} -> {b[2]}'
    return None


LANG = sys.argv[sys.argv.index('--lang') + 1] if '--lang' in sys.argv else 'de'
# Locale-Code der fertigen Datei (z. B. de_DE) aus mod.json: Eintrag, dessen "locale" der Ordnername in work/ ist
_cfg = json.load(open('mod/Mods/Localization Pack/mod.json', encoding='utf-8'))
LOCALE = next((c for c, l in _cfg['languages'].items() if l.get('locale') == LANG), LANG)
# Pluralregel der Zielsprache aus mod.json ("plural_forms", gettext-Format); Godot liest sie aus dem Kopf der .po
PLURAL = _cfg['languages'].get(LOCALE, {}).get('plural_forms')
NPLURALS = int(re.search(r'nplurals\s*=\s*(\d+)', PLURAL).group(1)) if PLURAL else 2
FORMS = '["Einzahl", "Mehrzahl"]' if NPLURALS == 2 else f'{NPLURALS} Formen'


def plural_index(rule, n):
    """Wertet die C-Formel aus "plural=..." für n aus; gettext.c2py prüft die Zeichen und nutzt kein freies eval."""
    return gettext.c2py(rule.split('plural=', 1)[1].rstrip('; '))(n)


assert [plural_index('nplurals=3; plural=(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);', n)
        for n in (1, 2, 4, 5, 12, 22, 25, 101)] == [0, 1, 1, 2, 2, 1, 2, 2]
assert [plural_index('nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);', n)
        for n in (1, 2, 5, 11, 12, 21, 22, 25, 111)] == [0, 1, 2, 2, 2, 0, 1, 2, 2]  # Russisch: 21 wie 1
assert [plural_index('nplurals=2; plural=(n > 1);', n) for n in (0, 1, 2)] == [0, 0, 1]
if PLURAL:  # Regel aus mod.json muss gültig sein und genau NPLURALS Formen liefern
    assert {plural_index(PLURAL, n) for n in range(200)} == set(range(NPLURALS)), PLURAL


# Sprachnamen, die in jeder Sprache im Original bleiben (Sprachliste zeigt jede Sprache in ihrem eigenen Namen)
KEEP_ENGLISH = {'English, United Kingdom', 'English (United Kingdom)'}


def plural_pairs(one, many, forms):
    """(Englisch, Übersetzung) je Form. Sprachen mit nur einer Form (Chinesisch) brauchen die Platzhalter der Mehrzahl."""
    return [(many, forms[0])] if NPLURALS == 1 and forms else list(zip([one] + [many] * len(forms), forms))


def entry_id(e):
    return f'{e.msgctxt or ""}\x04{e.msgid}\x04{e.msgid_plural or ""}'


items = json.load(open('work/items.json', encoding='utf-8'))
by_key = {f'{i["ctx"] or ""}\x04{i["en"]}\x04{i["en_plural"] or ""}': i for i in items}
tr = {}
for f in sorted(glob.glob(f'work/{LANG}/*.json')):
    tr.update(json.load(open(f, encoding='utf-8')))

po = polib.pofile('source/en_GB.po')
# Kurzer Code im Kopf (z. B. "de"): gespeicherte Spieleinstellungen "Language": "de" bleiben gültig
po.metadata['Language'] = _cfg['languages'].get(LOCALE, {}).get('locale', LOCALE)
po.metadata['Language-Team'] = f'{LANG} (Community)'
if PLURAL:
    po.metadata['Plural-Forms'] = PLURAL
po.metadata['Last-Translator'] = 'Melvor Idle 2 Mods'
done = errors = 0
applied = set()
for e in po:
    it = by_key.get(entry_id(e))
    t = tr.get(it['id']) if it else None
    if t is None or e.msgid in KEEP_ENGLISH:
        continue
    if e.msgid_plural:
        if not (isinstance(t, list) and len(t) == NPLURALS):
            print(f'FEHLER {it["id"]}: Plural braucht {FORMS}'); errors += 1; continue
        errs = [check(a, b) for a, b in plural_pairs(e.msgid, e.msgid_plural, t)]
    else:
        errs = [check(e.msgid, t)]
    errs = [x for x in errs if x]
    if errs:
        print(f'FEHLER {it["id"]}: {"; ".join(errs)}\n   EN: {e.msgid!r}\n   DE: {t!r}'); errors += 1; continue
    if e.msgid_plural:
        e.msgstr_plural = dict(enumerate(t))
    else:
        e.msgstr = t
    done += 1; applied.add(it['id'])

# Zusatztexte, die nicht in der offiziellen Vorlage stehen (C#-Code, Laufzeit): als neue Einträge anhängen
known = {entry_id(e) for e in po}
for key, it in by_key.items():
    t = tr.get(it['id'])
    if key in known or t is None or it['en'] in KEEP_ENGLISH:
        continue
    pairs = plural_pairs(it['en'], it['en_plural'], t) if it['en_plural'] and isinstance(t, list) else [(it['en'], t)]
    errs = [x for x in (check(a, b) for a, b in pairs) if x]
    if it['en_plural'] and not (isinstance(t, list) and len(t) == NPLURALS):
        errs.append(f'Plural braucht {FORMS}')
    if errs:
        print(f'FEHLER {it["id"]}: {"; ".join(errs)}\n   EN: {it["en"]!r}\n   DE: {t!r}'); errors += 1; continue
    ne = polib.POEntry(msgctxt=it['ctx'], msgid=it['en'], comment='Zusatztext (nicht in der offiziellen Vorlage)')
    if it['en_plural']:
        ne.msgid_plural, ne.msgstr_plural = it['en_plural'], dict(enumerate(t))
    else:
        ne.msgstr = t
    po.append(ne); done += 1; applied.add(it['id'])

# Godot verwirft die ganze .po, wenn ein Plural-Eintrag nicht genau NPLURALS Formen hat:
# unübersetzte Einträge der Vorlage (2 Formen) mit der letzten Form auffüllen bzw. kürzen (Chinesisch: 1 Form).
for e in po:
    if e.msgid_plural and len(e.msgstr_plural) != NPLURALS:
        last = e.msgstr_plural[max(e.msgstr_plural)]
        e.msgstr_plural = {i: e.msgstr_plural.get(i, last) for i in range(NPLURALS)}

# Godot übersetzt angezeigte Texte automatisch per tr(text) ohne Kontext. Namen stehen in der Vorlage
# aber nur mit msgctxt "PluralName" -> zusätzlich kontextlose Einträge für Einzahl und Mehrzahl anlegen
# (Mehrzahl: Form 1, bei Polnisch die Form für 2 bis 4, also der Nominativ Plural für alleinstehende Namen).
plain = {e.msgid for e in po if not e.msgctxt and not e.obsolete}
added = 0
for e in list(po):
    if e.msgctxt != 'PluralName' or not e.msgid_plural or not e.msgstr_plural.get(0):
        continue
    for src, dst in ((e.msgid, e.msgstr_plural[0]), (e.msgid_plural, e.msgstr_plural[min(1, NPLURALS - 1)])):
        if src not in plain and dst != src:
            po.append(polib.POEntry(msgid=src, msgstr=dst, comment='Kontextlos (automatisch aus PluralName)'))
            plain.add(src); added += 1
print('kontextlose Namen ergänzt:', added)

if '--check' not in sys.argv:  # --check: nur prüfen, nichts schreiben (für parallele Läufe)
    os.makedirs('dist', exist_ok=True)
    po.save(f'dist/{LOCALE}.po')
print(f'übersetzt {done} von {len([e for e in po if not e.obsolete])}, Fehler {errors}')
# Herkunft für die Transparenz-Angabe in der README (tools/package.py liest dist/<lang>.stats.json)
mi1_file = f'work/{LANG}/mi1.json'  # fehlt bei Sprachen ohne Melvor-Idle-1-Vorlage (zh_CN: Vorlage ist die .po des Spiels)
mi1 = set(json.load(open(mi1_file, encoding='utf-8'))) if os.path.exists(mi1_file) else set()
game_file = f'work/{LANG}/game.json'  # Texte aus der Übersetzung, die das Spiel selbst mitbringt (tools/import_po.py)
game = {k for k, v in json.load(open(game_file, encoding='utf-8')).items() if tr.get(k) == v} if os.path.exists(game_file) else set()
stats = {'translated': done, 'from_melvor_idle_1': len(applied & mi1), 'from_game': len(applied & game - mi1),
         'ai': len(applied - mi1 - game), 'name_copies': added}
json.dump(stats, open(f'dist/{LOCALE}.stats.json', 'w', encoding='utf-8'), indent=1)
print('Herkunft:', stats)

# Übersetzungen für andere Mods: work/mods/<Mod>/items.json ([{id, en}]) und <lang>.json ({id: Text})
# -> dist/mods/<Mod>/<Locale>.po (tools/package.py legt sie unter Languages/Mods/<Mod>/ ab)
for items_file in sorted(glob.glob('work/mods/*/items.json')):
    mod_dir = os.path.dirname(items_file)
    mod = os.path.basename(mod_dir)
    tr_file = os.path.join(mod_dir, f'{LANG}.json')
    if not os.path.exists(tr_file):
        continue
    mod_items = json.load(open(items_file, encoding='utf-8'))
    mod_tr = json.load(open(tr_file, encoding='utf-8'))
    mod_po = polib.POFile()
    mod_po.metadata = {'Language': po.metadata['Language'], 'MIME-Version': '1.0',
                       'Content-Type': 'text/plain; charset=UTF-8', 'Content-Transfer-Encoding': '8bit'}
    for it in mod_items:
        t = mod_tr.get(it['id'])
        err = check(it['en'], t) if t is not None else None
        if err:
            print(f'FEHLER {mod} {it["id"]}: {err}\n   EN: {it["en"]!r}\n   DE: {t!r}'); errors += 1
        elif t is not None:
            mod_po.append(polib.POEntry(msgid=it['en'], msgstr=t))
    if '--check' not in sys.argv:
        os.makedirs(f'dist/mods/{mod}', exist_ok=True)
        mod_po.save(f'dist/mods/{mod}/{LOCALE}.po')
    print(f'{mod}: übersetzt {len(mod_po)} von {len(mod_items)}')
sys.exit(1 if errors else 0)
