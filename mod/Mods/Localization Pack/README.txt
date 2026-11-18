Localization Pack for Melvor Idle 2
===================================
Version 1.0.0 - made for game version 0.11.6-alpha.1 (Steam Early Access)
Unofficial community translations for Melvor Idle 2 in one mod.
Not affiliated with or endorsed by Games By Malcs or Jagex.

Languages: German (Deutsch)
More languages are coming. Missing your language? Suggest it (see LINKS).


LINKS
-----
Nexus Mods:  (coming soon)
GitHub:      (coming soon)
Steam Guide: (coming soon)


TRANSPARENCY: HOW THESE TRANSLATIONS WERE MADE
----------------------------------------------
Language          Texts   From Melvor Idle  Translated by AI
----------------  ------  ----------------  ----------------
German (Deutsch)  13,605  566 (4%)          13,039 (96%)

- From Melvor Idle: texts that are identical in the first game (Melvor Idle) were taken from
  its official translation.
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
             │   └── (one .po file per language)
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
