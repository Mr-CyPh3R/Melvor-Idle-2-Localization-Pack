"""Teilt die englische Vorlage in Arbeitspakete (NUR für den allerersten Aufbau, vergibt ids neu!).

Für neue Texte später: tools/add_texts.py (behält vorhandene ids).

Aufruf (im Projektordner): python tools/split.py
Liest  source/en_GB.po, source/mi1_en.json, source/mi1_de.json
Schreibt work/chunks/NNN.json  ([{"id", "ctx", "en", "en_plural", "hint"}])
         work/de/mi1.json       ({id: Übersetzung} aus Melvor Idle 1, exakte Treffer)
         work/glossary.tsv      (kurze Begriffe aus Melvor Idle 1, EN -> DE)
"""
import collections, json, os, re, polib

CHUNK_CHARS = 12000
os.makedirs('work/chunks', exist_ok=True)
os.makedirs('work/de', exist_ok=True)


def entry_id(e):
    return f'{e.msgctxt or ""}\x04{e.msgid}\x04{e.msgid_plural or ""}'


po = polib.pofile('source/en_GB.po')
en = json.load(open('source/mi1_en.json', encoding='utf-8'))
de = json.load(open('source/mi1_de.json', encoding='utf-8'))
pairs = collections.defaultdict(collections.Counter)
for k, v in en.items():
    if de.get(k) and de[k] != v:
        pairs[v.strip()][de[k].strip()] += 1

items, seen, prefill = [], set(), {}
for e in po:
    if e.obsolete or entry_id(e) in seen:
        continue
    seen.add(entry_id(e))
    iid = f'{len(items):05d}'
    hint = (e.comment or '').replace('TRANSLATORS: ', '')
    items.append({'id': iid, 'ctx': e.msgctxt, 'en': e.msgid, 'en_plural': e.msgid_plural or None, 'hint': hint})
    # Nur einfache Einträge ohne Platzhalter direkt aus MI1 übernehmen
    if not e.msgid_plural and '{' not in e.msgid and e.msgid.strip() == e.msgid and e.msgid in pairs:
        prefill[iid] = pairs[e.msgid].most_common(1)[0][0]

chunks, cur, size = [], [], 0
for it in items:
    if it['id'] in prefill:
        continue
    cur.append(it)
    size += len(it['en']) + len(it['en_plural'] or '') + 40
    if size >= CHUNK_CHARS:
        chunks.append(cur); cur, size = [], 0
if cur:
    chunks.append(cur)
for i, c in enumerate(chunks):
    json.dump(c, open(f'work/chunks/{i:03d}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

json.dump(prefill, open('work/de/mi1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(items, open('work/items.json', 'w', encoding='utf-8'), ensure_ascii=False)

# Glossar: kurze, eindeutige Begriffe (max. 4 Wörter, ohne Platzhalter)
with open('work/glossary.tsv', 'w', encoding='utf-8') as g:
    for k in sorted(pairs):
        if 0 < len(k.split()) <= 4 and not re.search(r'[{}<>${}]', k) and len(k) <= 40:
            g.write(f'{k}\t{pairs[k].most_common(1)[0][0]}\n')

print('Einträge', len(items), 'aus MI1', len(prefill), 'Pakete', len(chunks))
