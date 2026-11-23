# Changelog

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
