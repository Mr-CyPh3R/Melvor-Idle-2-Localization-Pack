"""Baut das Mod-Paket "Localization Pack" und installiert es auf Wunsch ins Spiel.

Aufruf (im Projektordner): python tools/package.py [--install]
Sprachen stehen in mod/Mods/Localization Pack/mod.json unter "languages" ("file": Pfad im Mod-Ordner).
Für jede Sprache <code> wird dist/<code>.po (aus tools/build.py) an den Pfad aus "file" kopiert (Languages/Game/<code>.po),
Übersetzungen für andere Mods (dist/mods/<Mod>/) nach Languages/Mods/<Mod>/ (nur für die Mod-Loader-Fassung).
Die override.cfg wird aus der Liste der Spielsprachen erzeugt, damit alle Sprachen des Packs geladen werden.
Ergebnis: dist/Localization_Pack_v<version>_Standalone.zip mit override.cfg und Mods/Localization Pack/ (ohne Languages/Mods),
         dist/Localization_Pack_v<version>_ModLoader.zip mit Mods/Localization Pack/ samt Languages/Mods und DLL
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

# Übersetzungen für andere Mods (dist/mods/<Mod>/<code>.po aus tools/build.py) unter Languages/Mods/<Mod>/
for mod in sorted(os.listdir('dist/mods')) if os.path.isdir('dist/mods') else []:
    for code, lang in cfg['languages'].items():
        built = f'dist/mods/{mod}/{code}.po'
        if os.path.exists(built):
            rel = f'Languages/Mods/{mod}/{os.path.basename(lang["file"])}'
            os.makedirs(os.path.join(MOD_DIR, os.path.dirname(rel)), exist_ok=True)
            shutil.copyfile(built, os.path.join(MOD_DIR, rel))
            # nicht in die override.cfg: ohne Mod Loader gibt es diese Texte nicht, mit Mod Loader lädt sie die DLL

langs = ', '.join(f'{l["english_name"]} ({l["name"]})' for c, l in cfg['languages'].items())

# README aus Vorlage: Sprachliste und Herkunft der Texte (dist/<code>.stats.json aus tools/build.py)
rows = [('Language', 'Texts', 'From Melvor Idle', 'From Melvor Idle 2', 'Translated by AI')]
for code, l in cfg['languages'].items():
    st = json.load(open(f'dist/{code}.stats.json', encoding='utf-8'))
    pct = lambda n: f'{n:,} ({round(100 * n / st["translated"])}%)'
    rows.append((f'{l["english_name"]} ({l["name"]})', f'{st["translated"]:,}', pct(st['from_melvor_idle_1']), pct(st['from_game']), pct(st['ai'])))
w = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
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

LOADER_ONLY = os.path.join(MOD_DIR, 'Languages', 'Mods')  # Texte anderer Mods nur in der Mod-Loader-Fassung
zip_path = f'dist/Localization_Pack_v{cfg["version"]}_Standalone.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(SRC):
        if os.path.normpath(root).startswith(os.path.normpath(LOADER_ONLY)):
            continue
        for f in files:
            full = os.path.join(root, f)
            z.write(full, os.path.relpath(full, SRC).replace(os.sep, '/'))
print('Paket:', zip_path)
for i in zipfile.ZipFile(zip_path).infolist():
    print(f'  {i.file_size:>9}  {i.filename}')

# Version für Melvor Mod Loader: derselbe Mod-Ordner plus LocalizationPack.dll, ohne override.cfg
# (die gehört dem Loader); README mit eigenem Abschnitt INSTALLATION/UNINSTALL aus tools/README.modloader.txt
dll = 'modloader/LocalizationPack/bin/LocalizationPack.dll'
if os.path.exists(dll):
    loader_readme = readme[:readme.index('INSTALLATION\n')] + open('tools/README.modloader.txt', encoding='utf-8').read() \
        + readme[readme.index('NOTES\n'):].replace('- Only one mod can use override.cfg. Remove other translation mods first.', '- Remove other translation mods first.')
    loader = cfg['mod_loader_version']  # Titel: "1.2.0 (Mod Loader 0.2.0)"
    loader_readme = loader_readme.replace(f'Version {cfg["version"]},', f'Version {cfg["version"]} (Mod Loader {loader}),', 1)
    loader_zip = f'dist/Localization_Pack_v{cfg["version"]}_ModLoader.zip'
    with zipfile.ZipFile(loader_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(MOD_DIR):
            for f in files:
                full = os.path.join(root, f)
                arc = os.path.relpath(full, SRC).replace(os.sep, '/')
                if f == 'README.txt':
                    z.writestr(arc, loader_readme)
                else:
                    z.write(full, arc)
        z.write(dll, f'{MOD_REL}/LocalizationPack.dll')
    print('Paket:', loader_zip)
else:
    print('Hinweis: kein ModLoader-Paket,', dll, 'fehlt (cd modloader/LocalizationPack; dotnet build -c Release -o bin)')

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
    shutil.copytree(MOD_DIR, dst, ignore=lambda d, names: ['Mods'] if os.path.normpath(d) == os.path.normpath(os.path.dirname(LOADER_ONLY)) else [])
    print('installiert nach', GAME)
