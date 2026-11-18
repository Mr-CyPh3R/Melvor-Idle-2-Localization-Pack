"""Schneidet die eingebauten Sprachdateien (.po) aus der Spiel-Exe (Godot-PCK ist eingebettet).

Aufruf (im Projektordner): python tools/extract_po.py [Pfad zu Melvor2.exe]
Schreibt source/game/<Sprache>.po, z. B. source/game/en_GB.po. Nach einem Spiel-Update damit die
neue englische Vorlage holen und dann python tools/add_texts.py --po source/game/en_GB.po ausführen.
"""
import mmap, os, re, sys

exe = sys.argv[1] if len(sys.argv) > 1 else r'G:\steam\steamapps\common\Melvor Idle 2\Melvor2.exe'
os.makedirs('source/game', exist_ok=True)
with open(exe, 'rb') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for h in (m.start() for m in re.finditer(rb'msgid ""\r?\nmsgstr ""', mm)):
        chunk = mm[h:h + 8_000_000]
        end = chunk.find(b'\x00')  # Dateien im PCK sind durch Null-Bytes getrennt
        chunk = chunk[:end if end > 0 else len(chunk)]
        lang = re.search(rb'"Language: ([A-Za-z_]+)', chunk[:3000])
        name = lang.group(1).decode() if lang else f'unknown_{h:x}'
        out = f'source/game/{name}.po'
        open(out, 'wb').write(chunk)
        print(f'{out}: {chunk.count(b"\nmsgid ")} Einträge, {len(chunk):,} Bytes')
