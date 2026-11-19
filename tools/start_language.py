"""Legt eine neue Sprache an: Treffer aus Melvor Idle 1, Glossar und Arbeitspakete.

Aufruf (im Projektordner): python tools/start_language.py <lang>     z. B. fr
Liest  work/items.json, source/mi1_en.json, source/mi1_<lang>.json (offizielle Sprachdatei von Melvor Idle 1,
       https://melvoridle.com/lang/<lang>.json; fehlt sie, startet die Sprache ohne Vorlage)
Schreibt work/<lang>/mi1.json        ({id: Text} exakte Treffer aus Melvor Idle 1)
         work/glossary_<lang>.tsv    (kurze Begriffe EN<TAB>Zielsprache aus Melvor Idle 1)
         work/chunks/<lang>_NNN.json (Arbeitspakete für alle noch nicht übersetzten ids)
Danach: Pakete übersetzen lassen (tools/TRANSLATE_PROMPT.md), dann python tools/build.py --lang <lang>.
"""
import collections, json, os, re, sys

CHUNK_CHARS = 12000
lang = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
items = json.load(open('work/items.json', encoding='utf-8'))
os.makedirs(f'work/{lang}', exist_ok=True)

pairs = collections.defaultdict(collections.Counter)
src = f'source/mi1_{lang}.json'
if os.path.exists(src):
    en = json.load(open('source/mi1_en.json', encoding='utf-8'))
    tl = json.load(open(src, encoding='utf-8'))
    for k, v in en.items():
        if tl.get(k) and tl[k] != v:
            pairs[v.strip()][tl[k].strip()] += 1

# Nur einfache Einträge ohne Platzhalter direkt übernehmen (wie bei Deutsch in tools/split.py)
prefill = {i['id']: pairs[i['en']].most_common(1)[0][0] for i in items
           if not i['en_plural'] and '{' not in i['en'] and i['en'].strip() == i['en'] and i['en'] in pairs}
json.dump(prefill, open(f'work/{lang}/mi1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

with open(f'work/glossary_{lang}.tsv', 'w', encoding='utf-8') as g:
    for k in sorted(pairs):
        if 0 < len(k.split()) <= 4 and not re.search(r'[{}<>$]', k) and len(k) <= 40:
            g.write(f'{k}\t{pairs[k].most_common(1)[0][0]}\n')

done = set(prefill)
for f in os.listdir(f'work/{lang}'):
    done |= set(json.load(open(f'work/{lang}/{f}', encoding='utf-8')))
todo = [i for i in items if i['id'] not in done]
chunks, cur, size = [], [], 0
for it in todo:
    cur.append(it)
    size += len(it['en']) + len(it['en_plural'] or '') + 40
    if size >= CHUNK_CHARS:
        chunks.append(cur); cur, size = [], 0
if cur:
    chunks.append(cur)
for n, c in enumerate(chunks):
    json.dump(c, open(f'work/chunks/{lang}_{n:03d}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(f'{lang}: {len(items)} Texte, aus Melvor Idle 1: {len(prefill)}, offen: {len(todo)}, Pakete: {len(chunks)}')
