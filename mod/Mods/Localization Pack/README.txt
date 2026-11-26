Localization Pack for Melvor Idle 2
===================================
Version 1.4.0, made for game version 0.11.7-alpha (Steam Early Access)
Unofficial community translations for Melvor Idle 2 in one mod.
Not affiliated with or endorsed by Games By Malcs or Jagex.

Languages: German (Deutsch), French (Français), Spanish (Español), Brazilian Portuguese (Português), Japanese (日本語), Polish (Polski), Russian (Русский), Chinese (Simplified) (简体中文), Chinese (Traditional) (繁體中文), Vietnamese (Tiếng Việt)
More languages are coming. Missing your language? Suggest it (see LINKS).


LINKS
-----
Nexus Mods:  https://www.nexusmods.com/melvoridle2/mods/7
GitHub:      https://github.com/Mr-CyPh3R/Melvor-Idle-2-Localization-Pack
Steam Guide: https://steamcommunity.com/sharedfiles/filedetails/?id=3841947675


TRANSPARENCY: HOW THESE TRANSLATIONS WERE MADE
----------------------------------------------
Language                          Texts   From Melvor Idle  From Melvor Idle 2  Translated by AI
--------------------------------  ------  ----------------  ------------------  ----------------
German (Deutsch)                  13,708  566 (4%)          0 (0%)              13,142 (96%)
French (Français)                 13,708  586 (4%)          0 (0%)              13,122 (96%)
Spanish (Español)                 13,708  601 (4%)          0 (0%)              13,107 (96%)
Brazilian Portuguese (Português)  13,708  599 (4%)          0 (0%)              13,109 (96%)
Japanese (日本語)                    13,708  618 (5%)          0 (0%)              13,090 (95%)
Polish (Polski)                   13,708  0 (0%)            0 (0%)              13,708 (100%)
Russian (Русский)                 13,708  622 (5%)          0 (0%)              13,086 (95%)
Chinese (Simplified) (简体中文)       13,708  0 (0%)            11,394 (83%)        2,314 (17%)
Chinese (Traditional) (繁體中文)      13,708  0 (0%)            0 (0%)              13,708 (100%)
Vietnamese (Tiếng Việt)           13,708  0 (0%)            0 (0%)              13,708 (100%)

- From Melvor Idle: texts that are identical in the first game (Melvor Idle) were taken from
  its official translation.
- From Melvor Idle 2: texts from the game's own Chinese translation, which is included in the
  game files but not available in the language menu yet.
  Traditional Chinese was converted from the finished Simplified texts and proofread by AI,
  so it is counted as AI.
- Translated by AI: all other texts were translated with AI and checked
  automatically (placeholders, formatting tags and line breaks must match the original).
  They have not been fully reviewed by a human yet.
- Translated in-game by script: some texts are assembled by the game while it runs
  (for example "3 Turns" or "10 minutes"). The included script localization_pack.gd translates
  these in the game, using the same translations.
- Found a wrong or missing translation? Please report it (see LINKS).


INSTALLATION
------------
1. Close the game.
2. In Steam: right-click "Melvor Idle 2" > Manage > Browse local files.
3. Extract the archive (override.cfg and the "Mods" folder) into that folder, next to Melvor2.exe:

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

4. Start the game and choose your language in Settings > Language.


UNINSTALL
---------
Delete override.cfg and the folder "Mods/Localization Pack". Then select English again in the game.


NOTES
-----
- Does not change any game files or save games. Steam Cloud and achievements keep working.
- Only one mod can use override.cfg. Remove other translation mods first.
  All languages of this pack are installed together and can be selected in the language list.
  You may delete the .po files of languages you don't need from the "Languages" folder.
  The game then only notes the missing file in its log and keeps running normally.
- After a game update, some new texts may stay in English until the pack is updated.
- Help find missing texts: set "log_missing": true in mod.json. The game then writes texts that
  stayed in English to localization_pack_missing.txt. To find that file:
    1. Press the Windows key + R.
    2. Type %APPDATA%\Games By Malcs\Melvor Idle 2 and press Enter.
    3. The folder opens; localization_pack_missing.txt is in it.
  Please send us that file (see LINKS).
