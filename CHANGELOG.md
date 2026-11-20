# Changelog

## Unreleased

### New languages
* French (Français): 13,603 texts. 586 (4%) from the official French translation of Melvor Idle, 13,017 (96%) translated by AI.
* Spanish (Español): 13,603 texts. 601 (4%) from the official Spanish translation of Melvor Idle, 13,002 (96%) translated by AI.

### Fixes
* Time units are now always shown in the selected language. The game formats durations (for example "10 minutes" in the "Welcome back" window) in the Windows language, not in the game language. The script now recognises time units of every language in the pack and replaces them with the selected language.

### Other
* Language files are named by locale like the game's own file (`de_DE.po`, `fr_FR.po`).
* Language list shows each language in its own name ("Deutsch, Deutschland", "Français, France", "English, United Kingdom").
* Tools for adding further languages (`tools/start_language.py`, `tools/build.py --lang`).

### Known issues
* A character name that is identical to a game text (for example "Demo") is translated as well.

## 1.0.0 (2026-11-18)

* First release: German (Deutsch), 13,605 texts. 566 (4%) from the official German translation of Melvor Idle, 13,039 (96%) translated by AI.
