# Localization Pack for Melvor Idle 2

Unofficial community translations for Melvor Idle 2 in one mod.
Currently **German (Deutsch)**, **French (Français)**, **Spanish (Español)**, **Brazilian Portuguese (Português, Brasil)**, **Japanese (日本語)**, **Polish (Polski)**, **Russian (Русский)**, **Chinese, Simplified (简体中文)** and **Chinese, Traditional (繁體中文)**. More languages are coming. Missing your language? Open an issue and suggest it.

Not affiliated with or endorsed by Games By Malcs or Jagex.

## Links

* Nexus Mods: [Localization Pack on Nexus Mods](https://www.nexusmods.com/melvoridle2/mods/7)
* Steam Guide: [Localization Pack on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3841947675)
* Download: see [Releases](../../releases)

## How these translations were made

Please read this first. We want to be open about where the texts come from.

| Language | Texts | From Melvor Idle | From Melvor Idle 2 | Translated by AI |
|---|---|---|---|---|
| German (Deutsch) | 13,708 | 566 (4%) | 0 (0%) | 13,142 (96%) |
| French (Français) | 13,708 | 586 (4%) | 0 (0%) | 13,122 (96%) |
| Spanish (Español) | 13,708 | 601 (4%) | 0 (0%) | 13,107 (96%) |
| Brazilian Portuguese (Português, Brasil) | 13,708 | 599 (4%) | 0 (0%) | 13,109 (96%) |
| Japanese (日本語) | 13,708 | 618 (5%) | 0 (0%) | 13,090 (95%) |
| Polish (Polski) | 13,708 | 0 (0%) | 0 (0%) | 13,708 (100%) |
| Russian (Русский) | 13,708 | 622 (5%) | 0 (0%) | 13,086 (95%) |
| Chinese, Simplified (简体中文) | 13,708 | 0 (0%) | 11,394 (83%) | 2,314 (17%) |
| Chinese, Traditional (繁體中文) | 13,708 | 0 (0%) | 0 (0%) | 13,708 (100%) |

* **From Melvor Idle:** texts that are identical in the first game (Melvor Idle) were taken from its official translation.
* **From Melvor Idle 2:** texts from the game's own Chinese translation, which is included in the game files but not available in the language menu yet. Chinese, Traditional was converted from the finished Simplified texts (wording for Taiwan, terms from the official Traditional Chinese translation of Melvor Idle) and proofread by AI, so it is counted as AI.
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
        │   ├── Game/   (one .po file per language)
        │   └── Mods/   (texts of other mods, for example Melvor Mod Loader)
        ├── localization_pack.gd
        ├── mod.json
        └── README.txt
```

**Uninstall:** delete `override.cfg` and the folder `Mods/Localization Pack`, then select English again in the game.

### Installation with Melvor Mod Loader

If you play with [Melvor Mod Loader](https://falorfrozen-cmd.github.io/MelvorModLoader/) (0.2.0 or newer), download the **Mod Loader version** (`Localization_Pack_v<version>_ModLoader_<loader>.zip`) instead. It works together with other Mod Loader mods.

1. Install Melvor Mod Loader first, then close the game.
2. Extract the archive (only the `Mods` folder) next to `Melvor2.exe`. Keep the `override.cfg` of Mod Loader, this version does not bring its own.
3. Start the game and choose your language in **Settings > Language**. The Mod Loader menu (F1) follows the chosen language.

**Uninstall:** delete the folder `Mods/Localization Pack`, then select English again in the game.

## Notes

* Does not change any game files or save games. Steam Cloud and achievements keep working.
* Only one mod can use `override.cfg`. Remove other translation mods first. If you use Melvor Mod Loader, take the Mod Loader version instead.
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
| `work/<lang>/*.json` | Translations by id (`de`, `fr`, `es`, `pt_BR`, `ja`, `pl`, `ru`) |
| `work/mods/<Mod>/` | Texts of other mods (`items.json`) and their translations (`<lang>.json`) |
| `modloader/` | `LocalizationPack.dll` for Melvor Mod Loader (C#, .NET 10) |
| `work/STYLE.md`, `work/STYLE_<lang>.md` | Translation rules and terms per language |
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
