# Localization Pack for Melvor Idle 2

Unofficial community translations for Melvor Idle 2 in one mod.
Currently **German (Deutsch)** and **French (Français)**. More languages are coming. Missing your language? Open an issue and suggest it.

Not affiliated with or endorsed by Games By Malcs or Jagex.

## Links

* Nexus Mods: [Localization Pack on Nexus Mods](https://www.nexusmods.com/melvoridle2/mods/7)
* Steam Guide: [Localization Pack on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3841947675)
* Download: see [Releases](../../releases)

## How these translations were made

Please read this first. We want to be open about where the texts come from.

| Language | Texts | From Melvor Idle | Translated by AI |
|---|---|---|---|
| German (Deutsch) | 13,605 | 566 (4%) | 13,039 (96%) |
| French (Français) | 13,605 | 586 (4%) | 13,019 (96%) |

* **From Melvor Idle:** texts that are identical in the first game (Melvor Idle) were taken from its official translation.
* **Translated by AI:** all other texts were translated with AI and checked automatically (placeholders, formatting tags and line breaks must match the original). They have not been fully reviewed by a human yet.
* **Translated in-game by script:** some texts are assembled by the game while it runs (for example "3 Turns" or "10 minutes"). The included script translates these in the game, using the same translations.

Found a wrong or missing translation? Please open an issue.

## Installation

1. Close the game.
2. In Steam: right-click **Melvor Idle 2** > **Manage** > **Browse local files**.
3. Download the latest release and extract it (`override.cfg` and the `Mods` folder) into that folder, next to `Melvor2.exe`.
4. Start the game and choose your language in **Settings > Language**.

```
Melvor Idle 2/
├── Melvor2.exe
├── override.cfg
└── Mods/
    └── Localization Pack/
        ├── Languages/
        │   └── (one .po file per language)
        ├── localization_pack.gd
        ├── mod.json
        └── README.txt
```

**Uninstall:** delete `override.cfg` and the folder `Mods/Localization Pack`, then select English again in the game.

## Notes

* Does not change any game files or save games. Steam Cloud and achievements keep working.
* Only one mod can use `override.cfg`. Remove other translation mods first.
* All languages of this pack are installed together. You may delete the `.po` files of languages you don't need from the `Languages` folder.
* After a game update, some new texts may stay in English until the pack is updated.

### Help us find missing texts

1. Open `Mods/Localization Pack/mod.json` and set `"log_missing": true`.
2. Play the game. Texts that stayed in English are written to `localization_pack_missing.txt`.
3. To find that file: press **Windows key + R**, type `%APPDATA%\Games By Malcs\Melvor Idle 2` and press Enter.
4. Attach the file to an issue.

## Repository layout

| Path | Content |
|---|---|
| `mod/` | The mod exactly as it is installed (`override.cfg`, `Mods/Localization Pack/`) |
| `work/items.json` | All texts of the game that need a translation, with stable ids |
| `work/<lang>/*.json` | Translations by id (`de`, `fr`) |
| `work/STYLE.md`, `work/STYLE_fr.md` | Translation rules and terms per language |
| `tools/` | Build and maintenance scripts (Python 3, needs `polib`) |

### Building from source

The original game files are not part of this repository. You need your own copy of the game.

```
pip install polib
python tools/extract_po.py "<Steam>/steamapps/common/Melvor Idle 2/Melvor2.exe"
copy source\game\en_GB.po source\en_GB.po
python tools/build.py
python tools/package.py
```

The finished mod is written to `dist/`. After a game update, `python tools/add_texts.py --po source/game/en_GB.po` adds new texts to `work/items.json` without changing existing ids.

## License

The code in this repository (`tools/`, `localization_pack.gd`) is released under the [MIT License](LICENSE).

The English source texts contained in the translation files belong to Games By Malcs. They are included only because a translation file needs them as keys.
