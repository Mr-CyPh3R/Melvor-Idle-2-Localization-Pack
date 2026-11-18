# Übersetzungsregeln Melvor Idle 2 → Deutsch

## Stil
- Anrede **du** (wie das offizielle deutsche Melvor Idle 1): „Bist du sicher …?“, „Wähle …“.
- Kurz und natürlich, wie in einem deutschen Spiel. Knöpfe und Überschriften knapp halten.
- Großschreibung: Text, der im Englischen GANZ GROSS steht, auch im Deutschen ganz groß. Title Case wird zu normaler deutscher Schreibung.
- Zahlen und Prozent kommen aus Platzhaltern, nicht anfassen.
- Begriffe aus `work/glossary.tsv` (offizielles Melvor Idle 1, EN<TAB>DE) haben Vorrang. Bei Unsicherheit: `grep -P "^Begriff\t" work/glossary.tsv`.
- Gegenstands- und Monsternamen: wenn im Glossar, genau so übernehmen. Sonst sinnvoll eindeutschen im Stil des Glossars (z. B. „Iron Dagger“ → „Eisen-Dolch“).

## Unantastbar (Prüfung in tools/build.py schlägt sonst fehl)
- Alles in `{…}` bleibt Zeichen für Zeichen gleich, z. B. `{Value:+0.##%;-#.##%}`, `{LocalContext.Item.DisplayName}`, `{0:N0}`. Reihenfolge im Satz darf sich ändern.
- Ausnahme: In `{Value:cond:<0?Decreased|>=0?Increased}` dürfen nur die Wörter nach `?` übersetzt werden: `{Value:cond:<0?Verringert|>=0?Erhöht}`.
- BBCode-Tags `[b]`, `[/b]`, `[color=#…]`, `[img height=…]`, `[effectIcon/]`, `[ul]` usw. bleiben gleich und in gleicher Anzahl.
- Gleiche Anzahl Zeilenumbrüche `\n`. Führende und abschließende Leerzeichen beibehalten.
- Kaputt wirkende Quelltexte (z. B. `{DungeonIcon[/img]`) genau so übernehmen.

## Kernbegriffe (aus Melvor Idle 1)
Woodcutting=Holzfällerei · Fishing=Fischen · Firemaking=Funkenschlagen · Cooking=Kochen · Mining=Bergbau · Smithing=Schmieden · Thieving=Diebstahl · Fletching=Bognerei · Crafting=Handwerk · Runecrafting=Runenfertigung · Herblore=Pflanzenkunde · Agility=Gewandtheit · Astrology=Astrologie · Farming=Landwirtschaft · Summoning=Beschwörung · Slayer=Berserker · Slayer Coins=Berserkermünzen · Attack=Angriff · Strength=Stärke · Defence=Verteidigung · Hitpoints=Lebenspunkte · Ranged=Fernkampf · Magic=Magie · Prayer=Gebet · Combat=Kampf · Mastery=Meisterung · Mastery Pool=Meisterungsfundus · Equipment=Ausrüstung · Shop=Laden · Bank=Bank · GP=GM · Level=Stufe · Ore=Erz · Bar=Barren · Bones=Knochen · Food=Nahrung · Arrows=Pfeile · Evasion=Umgehung · Damage Reduction=Schadensreduzierung · Rune Essence=Runenessenz · Golbin=Golbin · Completion Log=Vollendungs-Logbuch · Statistics=Statistiken · Settings=Einstellungen · Archaeology=Archäologie · Cartography=Kartografie · Corruption=Verderbnis

Neu in Melvor Idle 2 (festgelegt, überall gleich verwenden):
Hunting=Jagd · Ranching=Viehzucht · Animal Husbandry=Tierhaltung · Beastcrafting=Bestienhandwerk · Toolbelt=Werkzeuggürtel · Quest(s)=Quest(s) · Recipe=Rezept · Skill=Fertigkeit · Experience/XP=Erfahrung/EP · Item=Gegenstand · Pet=Haustier · Loot=Beute · Dungeon=Dungeon · Monster=Monster · Potion=Trank · Rune=Rune · Seed=Samen · Logs=Holz (Oak Logs=Eichenholz) · Max Hit=Max. Treffer · Accuracy=Genauigkeit · Charges=Ladungen · Modifier=Modifikator · Preservation=Erhaltung · Mastery Guild=Meistergilde · Technique=Technik · Aurora=Aurora · Ward=Schutz · Save=Speicherstand (Substantiv) / Speichern (Knopf) · Melvor Cloud=Melvor Cloud · Offline Progress=Offline-Fortschritt · Gamemode=Spielmodus
