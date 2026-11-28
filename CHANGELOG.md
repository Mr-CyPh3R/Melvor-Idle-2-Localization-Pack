# Changelog

## Unreleased

### New languages
* European Portuguese (Português, Portugal): 13,711 texts, translated from English by AI with the terms of the official European Portuguese translation of Melvor Idle (599 texts taken from it). Kept apart from Brazilian Portuguese, with the European spelling and "tu". The Mod Loader menu (F1) is translated too.
* Turkish (Türkçe): 13,711 texts, translated from English by AI with the terms of the official Turkish translation of Melvor Idle (605 texts taken from it). Written with "sen" like Melvor Idle, short times as "2 sa 5 dk". The Mod Loader menu (F1) is translated too.

### Fixes
* Three texts of the save menu were missing in every language and are now translated: "Backup Save", "Export Backup Save" and "View Other Saves".

### Other
* The version without Mod Loader no longer contains the folder Languages/Mods (texts for Mod Loader, which are only used with Mod Loader).
* The table "How these translations were made" now also counts the texts filled in by script (names the game looks up without context, and the conversion of Chinese, Traditional), so every language shows about 15,170 texts.

## 1.4.0 (2026-11-26)

### New languages
* Chinese, Simplified (简体中文): 13,708 texts. 11,394 (83%) from the game's own Chinese translation, which is included in the game files but not available in the language menu yet, 2,314 (17%) translated or corrected by AI. The Mod Loader menu (F1) is translated too.
* Chinese, Traditional (繁體中文): 13,708 texts, converted from the Simplified texts with wording for Taiwan and terms from the official Traditional Chinese translation of Melvor Idle, proofread by AI. The Mod Loader menu (F1) is translated too.
* Vietnamese (Tiếng Việt): 13,708 texts, all translated by AI. Melvor Idle has no official Vietnamese translation, so there were no official terms to start from. The Mod Loader menu (F1) is translated too.

### Fixes
* After a language change, the window size, screen and anti-aliasing lists in the display settings now show the new language too.
* Tracker bar: the tracking period list ("1 minute", "10 minutes" and its heading), the target level ("Level 3") and the time left ("1m 9s") are now translated.
* Short times like "1m 9s" are written with the units of the language (German "1 Min. 9 Sek.", French "1 min 9 s"), also in the character selection ("less than 1m") and in the empty tracker ("--h --m --s"). German shows "/Std." instead of "/h" there.
* Russian and Polish: durations use the right plural form again ("1 минута", "12 секунд" instead of "1 минуты", "12 секунды"), for example in the tracker, the offline progress and the last save time.

### Melvor Mod Loader
* All 10 notes that Mod Loader 0.3.0 shows in the game (for example a mod did not start, a mod was partly switched off after an error, items of removed mods waiting for room in the bank) are translated into every language of the pack. Messages that only go to MelvorModLoader.log stay in English.

### Other
* In the game view, the game version ("Melvor Idle 2: v0.11.7-alpha") is shown right of the logo in the top left corner instead of the top centre, so it no longer covers the window title and the skill header.
* Languages with only one plural form are supported.
* Two languages that share a language code (Chinese, Simplified and Traditional) are kept apart while the game runs.

## 1.3.0 (2026-11-25)

### New languages
* Polish (Polski): 13,708 texts, all translated by AI. Melvor Idle has no official Polish translation, so there were no official terms to start from.
* Russian (Русский): 13,708 texts. 622 (5%) from the official Russian translation of Melvor Idle, 13,086 (95%) translated by AI.

### Melvor Mod Loader
* The Localization Pack is now compatible with Melvor Mod Loader: players who use mods can play in their own language too. Download the file "Mod Loader version".
* `LocalizationPack.dll` loads the pack through Mod Loader instead of its own override.cfg, so it works together with other Mod Loader mods.
* The Mod Loader menu (F1) is translated into every language of the pack.

### Game update
* On 2026-11-25 the game update v0.11.7-alpha was released. 105 new texts were found and translated into all languages of the pack (for example the new bank tab icons, set bonuses, notification settings and shop categories).

### Fixes
* Quest requirements such as "Must be able to defeat a Combat Level 1 Enemy" are now translated.
* With English selected, times in the "Welcome back" window no longer show units in the Windows language (for example "19 Minuten").
* Shorter texts in the shop toolbar and shorter item names on the Agility shop cards, so the shop no longer slides under the sidebar in French, Polish, Brazilian Portuguese and Russian.

### Other
* Languages with more than two plural forms are supported. Polish and Russian use three ("1 sekunda", "2 sekundy", "5 sekund"); the rule for each language is set in `mod.json`.
* Language files are now in `Languages/Game`, texts of other mods in `Languages/Mods/<Mod>`. When updating, delete the old folder "Mods/Localization Pack" first.

## 1.2.0 (2026-11-23)

### New languages
* Brazilian Portuguese (Português, Brasil): 13,603 texts. 599 (4%) from the official Brazilian Portuguese translation of Melvor Idle, 13,004 (96%) translated by AI.
* Japanese (日本語): 13,603 texts. 618 (5%) from the official Japanese translation of Melvor Idle, 12,985 (95%) translated by AI.

### Fixes
* Local and cloud save times in the pause menu now keep their translated units on every timer update.
* Switching languages now refreshes shop item names and the hidden item filters in Woodcutting and Mining while those screens are open.
* The combat screen now refreshes the player's and enemy's accuracy labels, including the attack stance, when switching languages.
* The startup loading message now follows the selected game language even when the game initially supplies text in another language.
* Shop descriptions with named colors or item icons now use the language pack.

### Other
* Languages written without spaces (Japanese) wrap long texts such as quest synopses inside their boxes.

## 1.1.0 (2026-11-20)

### New languages
* French (Français): 13,603 texts. 586 (4%) from the official French translation of Melvor Idle, 13,017 (96%) translated by AI.
* Spanish (Español): 13,603 texts. 601 (4%) from the official Spanish translation of Melvor Idle, 13,002 (96%) translated by AI.

### Fixes
* Time units are now always shown in the selected language. The game formats durations (for example "10 minutes" in the "Welcome back" window) in the Windows language, not in the game language. The script now recognises time units of every language in the pack and replaces them with the selected language.

### Other
* Language files are named by locale like the game's own file (`de_DE.po`, `fr_FR.po`, `es_ES.po`).
* Language list shows each language in its own name ("Deutsch, Deutschland", "Français, France", "Español, España", "English, United Kingdom").
* Tools for adding further languages (`tools/start_language.py`, `tools/build.py --lang`).

### Known issues
* A character name that is identical to a game text (for example "Demo") is translated as well.

## 1.0.0 (2026-11-18)

* First release: German (Deutsch), 13,605 texts. 566 (4%) from the official German translation of Melvor Idle, 13,039 (96%) translated by AI.
