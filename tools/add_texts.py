"""Neue englische Texte in die Übersetzungsarbeit aufnehmen, ohne vorhandene Nummern zu verschieben.

Aufruf (im Projektordner):
  python tools/add_texts.py --po source/game/en_GB.po      neue Vorlage nach einem Spiel-Update
  python tools/add_texts.py --missing [Datei ...]          Protokolle englisch gebliebener Texte
      (ohne Datei: %APPDATA%/Games By Malcs/Melvor Idle 2/localization_pack_missing.txt;
       Dateien von Spielern einfach als weitere Pfade anhängen)

Hängt nur Texte an, die es in work/items.json noch nicht gibt, mit fortlaufenden neuen ids, und
schreibt sie als Arbeitspakete work/chunks/<Präfix><NN>.json. Danach die Pakete übersetzen (wie die
anderen, nach work/STYLE.md) und python tools/build.py ausführen.
Hinweis: tools/split.py ist nur für den allerersten Aufbau; erneut ausgeführt würde es die ids neu vergeben.
"""
import json, os, re, sys, polib

CHUNK_CHARS = 12000
items = json.load(open('work/items.json', encoding='utf-8'))
key = lambda ctx, en, pl: f'{ctx or ""}\x04{en}\x04{pl or ""}'
known = {key(i['ctx'], i['en'], i['en_plural']) for i in items}
known_text = {i['en'] for i in items} | {i['en_plural'] for i in items if i['en_plural']}
next_id = max(int(i['id']) for i in items) + 1
new = []


def add(ctx, en, pl, hint):
    global next_id
    k = key(ctx, en, pl)
    if k in known or not re.search('[A-Za-z]{2,}', en):
        return
    known.add(k)
    new.append({'id': f'{next_id:05d}', 'ctx': ctx, 'en': en, 'en_plural': pl, 'hint': hint})
    next_id += 1


if '--po' in sys.argv:
    for e in polib.pofile(sys.argv[sys.argv.index('--po') + 1]):
        if not e.obsolete:
            add(e.msgctxt, e.msgid, e.msgid_plural or None, (e.comment or '').replace('TRANSLATORS: ', ''))
    prefix = 'u'
elif '--missing' in sys.argv:
    files = sys.argv[sys.argv.index('--missing') + 1:] or [os.path.join(
        os.environ['APPDATA'], 'Games By Malcs', 'Melvor Idle 2', 'localization_pack_missing.txt')]
    # Bereits übersetzte deutsche Ausgaben nicht als "neu" aufnehmen
    tr_values = set()
    for f in os.listdir('work/de'):
        for v in json.load(open(os.path.join('work/de', f), encoding='utf-8')).values():
            tr_values.update(v if isinstance(v, list) else [v])
    for f in files:
        for line in open(f, encoding='utf-8'):
            # Zeilen sind mit Godots c_escape() geschrieben: \n, \t, \", \\ zurückwandeln
            s = re.sub(r'\\([\\"\'nt])', lambda m: {'n': '\n', 't': '\t'}.get(m.group(1), m.group(1)), line.rstrip('\n'))
            if s and s not in known_text and s not in tr_values:
                add(None, s, None, 'Im Spiel englisch geblieben (localization_pack_missing.txt)')
    prefix = 'm'
else:
    sys.exit(__doc__)

if not new:
    sys.exit('Keine neuen Texte.')
items += new
json.dump(items, open('work/items.json', 'w', encoding='utf-8'), ensure_ascii=False)
n = 0
while os.path.exists(f'work/chunks/{prefix}{n:02d}.json'):
    n += 1
cur, size, files_written = [], 0, []
for it in new + [None]:
    if it is not None:
        cur.append(it); size += len(it['en']) + len(it['en_plural'] or '') + 40
    if cur and (it is None or size >= CHUNK_CHARS):
        name = f'work/chunks/{prefix}{n:02d}.json'
        json.dump(cur, open(name, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        files_written.append(name); cur, size, n = [], 0, n + 1
print(f'{len(new)} neue Texte, Pakete: {", ".join(files_written)}')
