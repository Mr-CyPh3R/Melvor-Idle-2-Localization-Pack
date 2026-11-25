INSTALLATION (MELVOR MOD LOADER VERSION)
----------------------------------------
This version is for players who use Melvor Mod Loader (0.2.0 or newer) and works together
with other Mod Loader mods. Without Mod Loader, use the normal version with override.cfg.

1. Install Melvor Mod Loader first: https://falorfrozen-cmd.github.io/MelvorModLoader/
2. Close the game.
3. In Steam: right-click "Melvor Idle 2" > Manage > Browse local files.
4. Extract the archive (the "Mods" folder) into that folder, next to Melvor2.exe.
   Keep the override.cfg of Mod Loader, this pack does not bring its own:

     Melvor Idle 2/
     ├── Melvor2.exe
     ├── override.cfg                          (from Mod Loader)
     ├── data_MelvorModLoader_windows_x86_64/  (from Mod Loader)
     └── Mods/
         └── Localization Pack/
             ├── Languages/
             │   ├── Game/   (one .po file per language)
             │   └── Mods/   (texts of other mods, for example Melvor Mod Loader)
             ├── LocalizationPack.dll
             ├── localization_pack.gd
             ├── mod.json
             └── README.txt

5. Start the game and choose your language in Settings > Language.
   The Mod Loader menu (F1) is shown in the chosen language as well.
   MelvorModLoader.log in the game folder should list "Mod loaded: LocalizationPack".

Updating from an older version: delete the folder "Mods/Localization Pack" first.


UNINSTALL
---------
Delete the folder "Mods/Localization Pack". Then select English again in the game.


