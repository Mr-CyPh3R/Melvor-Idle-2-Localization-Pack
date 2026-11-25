"""Übernimmt Übersetzungen aus einer fertigen .po (z. B. der chinesischen Datei des Spiels) nach work/<lang>/game.json.

Aufruf (im Projektordner): python tools/import_po.py <po-Datei> <lang>      z. B. source/game/zh_CN.po zh
Nur exakte Treffer (msgctxt + msgid + msgid_plural wie in work/items.json), nichts wird geraten.
Plural: die Formen der Quelle als Liste. Danach: python tools/start_language.py <lang> (Pakete nur für offene ids).
"""
import json, os, sys, polib

po_file, lang = sys.argv[1], sys.argv[2]
items = json.load(open('work/items.json', encoding='utf-8'))
po = polib.pofile(po_file)
src = {(e.msgctxt or '', e.msgid, e.msgid_plural or ''): e for e in po if not e.obsolete}

out = {}
for it in items:
    e = src.get((it['ctx'] or '', it['en'], it['en_plural'] or ''))
    if e is None:
        continue
    if it['en_plural']:
        forms = [e.msgstr_plural[k] for k in sorted(e.msgstr_plural)]
        if all(forms):
            out[it['id']] = forms
    elif e.msgstr:
        out[it['id']] = e.msgstr

os.makedirs(f'work/{lang}', exist_ok=True)
json.dump(out, open(f'work/{lang}/game.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(f'{lang}: {len(out)} von {len(items)} Texten aus {po_file} übernommen -> work/{lang}/game.json')
