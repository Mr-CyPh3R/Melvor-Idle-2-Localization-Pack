# Auftrag für Übersetzungs-Agenten (Vorlage)

Für neue Arbeitspakete aus `tools/add_texts.py` (z. B. `u00`, `m00`). Pro Agent 3–5 Pakete, mehrere Agenten
parallel. `<PAKETE>` ersetzen. Für eine andere Sprache als Deutsch: `work/de/` → `work/<code>/` und eine
eigene `STYLE`-Datei mit Begriffen der Zielsprache anlegen.

---

Du übersetzt Texte des Spiels Melvor Idle 2 vom Englischen ins Deutsche.
Arbeitsordner: H:\Melvor Idle 2 Mods (alle Pfade relativ dazu). Ändere NUR die unten genannten Dateien in work/de/.

1. Lies zuerst work/STYLE.md vollständig und halte dich strikt daran (du-Form, Glossar, Platzhalter unverändert).
   Bereits festgelegte Übersetzungen stehen in work/de/*.json (ids siehe work/items.json). Vor dem Übersetzen
   eines Namens dort nach demselben englischen Namen suchen und GENAU dieselbe Form verwenden:
   python -c "import json,glob,sys;it={i['id']:i['en'] for i in json.load(open('work/items.json',encoding='utf-8'))};tr={};[tr.update(json.load(open(f,encoding='utf-8'))) for f in glob.glob('work/de/*.json')];q=sys.argv[1].lower();[print(k,it[k],'=>',v) for k,v in tr.items() if k in it and q in it[k].lower()][:20]" "Bird Nest"
   Offizielles Glossar aus Melvor Idle 1: grep -P "^Begriff\t" work/glossary.tsv
2. Bearbeite nacheinander diese Pakete: <PAKETE>.
   Für jedes Paket NAME: work/chunks/NAME.json lesen (id, ctx, en, en_plural, hint) und work/de/NAME.json schreiben:
   {"id": "Text"}, bei en_plural {"id": ["Einzahl", "Mehrzahl"]}. Jede id muss vorkommen. Gültiges JSON (\" und \n), UTF-8.
   [Companion Name], [Icon] u. ä. in eckigen Klammern sind Platzhalter des Spiels: unverändert lassen.
3. Danach: python tools/build.py --check . Jede Zeile "FEHLER <id>" deiner Pakete beheben, bis keine mehr kommt.
Gib zurück: erledigte Pakete, Anzahl Einträge, verbleibende Fehler, neu festgelegte Begriffe.
