"""Baut dist/de.po aus der Vorlage und den Übersetzungen in work/de/*.json und prüft die Platzhalter.

Aufruf (im Projektordner): python tools/build.py [--check]
work/de/*.json: {id: "Text"} oder bei Pluralen {id: ["Einzahl", "Mehrzahl"]}
Exit 1, wenn eine Übersetzung Platzhalter, Tags oder Zeilenumbrüche verändert.
Installieren ins Spiel: python tools/package.py --install
"""
import collections, glob, json, os, re, sys, polib

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


def entry_id(e):
    return f'{e.msgctxt or ""}\x04{e.msgid}\x04{e.msgid_plural or ""}'


items = json.load(open('work/items.json', encoding='utf-8'))
by_key = {f'{i["ctx"] or ""}\x04{i["en"]}\x04{i["en_plural"] or ""}': i for i in items}
tr = {}
for f in sorted(glob.glob('work/de/*.json')):
    tr.update(json.load(open(f, encoding='utf-8')))

po = polib.pofile('source/en_GB.po')
po.metadata['Language'] = 'de'
po.metadata['Language-Team'] = 'Deutsch (Community)'
po.metadata['Last-Translator'] = 'Melvor Idle 2 Mods'
done = errors = 0
applied = set()
for e in po:
    it = by_key.get(entry_id(e))
    t = tr.get(it['id']) if it else None
    if t is None:
        continue
    if e.msgid_plural:
        if not (isinstance(t, list) and len(t) == 2):
            print(f'FEHLER {it["id"]}: Plural braucht ["Einzahl", "Mehrzahl"]'); errors += 1; continue
        errs = [check(e.msgid, t[0]), check(e.msgid_plural, t[1])]
    else:
        errs = [check(e.msgid, t)]
    errs = [x for x in errs if x]
    if errs:
        print(f'FEHLER {it["id"]}: {"; ".join(errs)}\n   EN: {e.msgid!r}\n   DE: {t!r}'); errors += 1; continue
    if e.msgid_plural:
        e.msgstr_plural = {0: t[0], 1: t[1]}
    else:
        e.msgstr = t
    done += 1; applied.add(it['id'])

# Zusatztexte, die nicht in der offiziellen Vorlage stehen (C#-Code, Laufzeit): als neue Einträge anhängen
known = {entry_id(e) for e in po}
for key, it in by_key.items():
    t = tr.get(it['id'])
    if key in known or t is None:
        continue
    pairs = [(it['en'], t[0] if isinstance(t, list) else t)] + ([(it['en_plural'], t[1])] if it['en_plural'] and isinstance(t, list) else [])
    errs = [x for x in (check(a, b) for a, b in pairs) if x]
    if it['en_plural'] and not (isinstance(t, list) and len(t) == 2):
        errs.append('Plural braucht ["Einzahl", "Mehrzahl"]')
    if errs:
        print(f'FEHLER {it["id"]}: {"; ".join(errs)}\n   EN: {it["en"]!r}\n   DE: {t!r}'); errors += 1; continue
    ne = polib.POEntry(msgctxt=it['ctx'], msgid=it['en'], comment='Zusatztext (nicht in der offiziellen Vorlage)')
    if it['en_plural']:
        ne.msgid_plural, ne.msgstr_plural = it['en_plural'], {0: t[0], 1: t[1]}
    else:
        ne.msgstr = t
    po.append(ne); done += 1; applied.add(it['id'])

# Godot übersetzt angezeigte Texte automatisch per tr(text) ohne Kontext. Namen stehen in der Vorlage
# aber nur mit msgctxt "PluralName" -> zusätzlich kontextlose Einträge für Einzahl und Mehrzahl anlegen.
plain = {e.msgid for e in po if not e.msgctxt and not e.obsolete}
added = 0
for e in list(po):
    if e.msgctxt != 'PluralName' or not e.msgid_plural or not e.msgstr_plural.get(0):
        continue
    for src, dst in ((e.msgid, e.msgstr_plural[0]), (e.msgid_plural, e.msgstr_plural[1])):
        if src not in plain and dst != src:
            po.append(polib.POEntry(msgid=src, msgstr=dst, comment='Kontextlos (automatisch aus PluralName)'))
            plain.add(src); added += 1
print('kontextlose Namen ergänzt:', added)

if '--check' not in sys.argv:  # --check: nur prüfen, nichts schreiben (für parallele Läufe)
    os.makedirs('dist', exist_ok=True)
    po.save('dist/de.po')
print(f'übersetzt {done} von {len([e for e in po if not e.obsolete])}, Fehler {errors}')
# Herkunft für die Transparenz-Angabe in der README (tools/package.py liest dist/de.stats.json)
mi1 = set(json.load(open('work/de/mi1.json', encoding='utf-8')))
stats = {'translated': done, 'from_melvor_idle_1': len(applied & mi1), 'ai': done - len(applied & mi1), 'name_copies': added}
json.dump(stats, open('dist/de.stats.json', 'w', encoding='utf-8'), indent=1)
print('Herkunft:', stats)
sys.exit(1 if errors else 0)
