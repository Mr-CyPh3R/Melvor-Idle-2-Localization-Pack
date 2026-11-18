"""Baut das Mod-Paket "Localization Pack" und installiert es auf Wunsch ins Spiel.

Aufruf (im Projektordner): python tools/package.py [--install]
Sprachen stehen in mod/Mods/Localization Pack/mod.json unter "languages" ("file": Pfad im Mod-Ordner).
Für jede Sprache <code> wird dist/<code>.po (aus tools/build.py) an den Pfad aus "file" kopiert (Languages/<code>.po).
Die override.cfg wird aus dieser Liste erzeugt, damit alle Sprachen des Packs geladen werden.
Ergebnis: dist/Localization_Pack_v<version>.zip mit override.cfg und Mods/Localization Pack/
--install kopiert alles in den Spielordner (überschreibt nur eine eigene override.cfg).
"""
import json, os, shutil, sys, zipfile

GAME = r'G:\steam\steamapps\common\Melvor Idle 2'
SRC = 'mod'
MOD_REL = 'Mods/Localization Pack'
MARK = 'Localization Pack for Melvor Idle 2'
OWN_MARKS = (MARK, 'Localization Pack für Melvor Idle 2', 'Test: eigene deutsche')  # auch ältere eigene Versionen
MOD_DIR = os.path.join(SRC, MOD_REL)

cfg = json.load(open(os.path.join(MOD_DIR, 'mod.json'), encoding='utf-8'))
paths = ['res://Locale/en_GB.po']
for code, lang in cfg['languages'].items():
    built = f'dist/{code}.po'
    if not os.path.exists(built):
        sys.exit(f'Abbruch: {built} fehlt. Zuerst die Übersetzung bauen.')
    dst = os.path.join(MOD_DIR, lang['file'])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(built, dst)
    paths.append(f'res://{MOD_REL}/{lang["file"]}')

langs = ', '.join(f'{l["english_name"]} ({l["name"]})' for c, l in cfg['languages'].items())

# README aus Vorlage: Sprachliste und Herkunft der Texte (dist/<code>.stats.json aus tools/build.py)
rows = [('Language', 'Texts', 'From Melvor Idle', 'Translated by AI')]
for code, l in cfg['languages'].items():
    st = json.load(open(f'dist/{code}.stats.json', encoding='utf-8'))
    pct = lambda n: f'{n:,} ({round(100 * n / st["translated"])}%)'
    rows.append((f'{l["english_name"]} ({l["name"]})', f'{st["translated"]:,}', pct(st['from_melvor_idle_1']), pct(st['ai'])))
w = [max(len(r[i]) for r in rows) for i in range(4)]
table = '\n'.join('  '.join(c.ljust(w[i]) for i, c in enumerate(r)).rstrip() for r in rows[:1] + [tuple('-' * x for x in w)] + rows[1:])
readme = open('tools/README.template.txt', encoding='utf-8').read().format(
    version=cfg['version'], game_version=cfg['game_version'], languages=langs, language_table=table)
open(os.path.join(MOD_DIR, 'README.txt'), 'w', encoding='utf-8').write(readme)

override = f'''; {MARK}, version {cfg["version"]} (unofficial). Languages: {langs}
; Files are in "{MOD_REL}". Uninstall: delete this file and the folder "{MOD_REL}".

[autoload]

LocalizationPack="*res://{MOD_REL}/localization_pack.gd"

[internationalization]

locale/translations=PackedStringArray({", ".join(f'"{p}"' for p in paths)})
'''
open(os.path.join(SRC, 'override.cfg'), 'w', encoding='utf-8').write(override)

zip_path = f'dist/Localization_Pack_v{cfg["version"]}.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(SRC):
        for f in files:
            full = os.path.join(root, f)
            z.write(full, os.path.relpath(full, SRC).replace(os.sep, '/'))
print('Paket:', zip_path)
for i in zipfile.ZipFile(zip_path).infolist():
    print(f'  {i.file_size:>9}  {i.filename}')

if '--install' in sys.argv:
    target = os.path.join(GAME, 'override.cfg')
    if os.path.exists(target):
        text = open(target, encoding='utf-8', errors='replace').read()
        # Eigene ältere Versionen erkennen, override.cfg anderer Mods nicht überschreiben
        if not any(m in text for m in OWN_MARKS):
            sys.exit(f'Abbruch: {target} gehört zu einer anderen Mod. Bitte zuerst prüfen.')
    shutil.copyfile(os.path.join(SRC, 'override.cfg'), target)
    dst = os.path.join(GAME, MOD_REL)
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(MOD_DIR, dst)
    print('installiert nach', GAME)
