# Reglas de traducción Melvor Idle 2 → Español (España)

## Estilo
- Tuteo (**tú**), como la traducción oficial española de Melvor Idle 1: «¿Seguro que quieres …?», «Elige …».
- Español de España, natural y conciso, como en un videojuego. Botones y títulos breves.
- Texto en MAYÚSCULAS en inglés: también en mayúsculas en español. Title Case inglés → mayúscula solo en la primera palabra (y nombres propios).
- Signos de apertura «¿» y «¡». Espacio antes de «%» («20 %»), salvo si el signo va pegado a un placeholder `{…}`.
- Sin raya ni semirraya (– —) como puntuación; usa coma, dos puntos o paréntesis.
- Los términos de `work/glossary_es.tsv` (Melvor Idle 1 oficial, EN<TAB>ES) tienen prioridad. Búsqueda: `grep -P "^Término\t" work/glossary_es.tsv`.
- Nombres de objetos y monstruos: si están en el glosario, cópialos exactamente. Si no, tradúcelos con el mismo estilo («Iron Dagger» → «Daga de hierro», «Oak Logs» → «Troncos de roble»).
- Mismo nombre inglés = misma traducción en todas partes. Antes de traducir un nombre, busca si ya está traducido en `work/es/*.json`.

## Intocable (si no, `python tools/build.py --lang es --check` falla)
- Todo lo que va entre `{…}` se queda igual carácter por carácter, p. ej. `{Value:+0.##%;-#.##%}`, `{LocalContext.Item.DisplayName}`, `{0:N0}`. El orden en la frase puede cambiar.
- Excepción: en `{Value:cond:<0?Decreased|>=0?Increased}` solo se traducen las palabras tras `?`: `{Value:cond:<0?Reducido|>=0?Aumentado}`.
- Etiquetas BBCode `[b]`, `[/b]`, `[color=#…]`, `[img height=…]`, `[effectIcon/]`, `[ul]` etc.: idénticas y en el mismo número.
- `[Companion Name]`, `[Icon]`, `[seconds]`, `[pixels]`, `[Sighting]`, `[Observation]` y otras palabras entre corchetes son marcadores del juego: no traducir.
- Mismo número de saltos de línea `\n`. Conserva los espacios al principio y al final.
- Textos de origen aparentemente rotos (p. ej. `{DungeonIcon[/img]`): cópialos tal cual.
- Plurales (`en_plural`): `["singular", "plural"]`.

## Términos básicos (Melvor Idle 1 oficial)
Woodcutting=Tala · Fishing=Pesca · Firemaking=Dominio del fuego · Cooking=Cocina · Mining=Minería · Smithing=Herrería · Thieving=Robo · Fletching=Arquería · Crafting=Artesanía · Runecrafting=Creación de runas · Herblore=Herbología · Agility=Agilidad · Astrology=Astrología · Farming=Agricultura · Summoning=Invocación · Slayer=Exterminio · Slayer Coins=Monedas de exterminio · Attack=Ataque · Strength=Fuerza · Defence=Defensa · Hitpoints=Puntos de vida · HP=PS · Ranged=A distancia · Magic=Magia · Prayer=Plegaria · Combat=Combate · Mastery=Maestría · Mastery Pool=Reserva de maestría · Equipment=Equipo · Shop=Tienda · Bank=Inventario · Bank Space=Espacio de inventario · GP=ORO · Gold=Oro · Level=Nivel · Ore=Mineral · Bar=Lingote · Bones=Huesos · Food=Comida · Arrows=Flechas · Rune Essence=Esencia rúnica · Evasion=Evasión · Damage Reduction=Reducción de daño · Stealth=Sigilo · Special Attack=Ataque especial · Stun=Aturdimiento · Poison=Envenenamiento · Golbin=Golbin · Completion Log=Registro de finalización · Statistics=Estadísticas · Settings=Ajustes · Archaeology=Arqueología · Cartography=Cartografía · Corruption=Corrupción · Unlock=Desbloquear · Locked=Bloqueado · Cancel=Cancelar · Confirm=Confirmar · Save (botón)=Guardar · Items=Objetos

## Términos nuevos de Melvor Idle 2 (fijados, úsalos siempre)
Hunting=Caza · Ranching=Ganadería · Animal Husbandry=Cuidado de animales · Beastcrafting=Artesanía bestial · Toolbelt=Cinturón de herramientas · Quest(s)=Misión(es) · Recipe=Receta · Skill=Habilidad · Experience/XP=Experiencia/XP · Item=Objeto · Pet=Mascota · Loot=Botín · Dungeon=Mazmorra · Monster=Monstruo · Boss=Jefe · Area=Zona · Potion=Poción · Rune=Runa · Seed=Semilla · Logs=Troncos · Max Hit=Golpe máx. · Accuracy=Precisión · Charges=Cargas · Modifier=Modificador · Preservation=Conservación · Output Doubling=Duplicación de producción · Input Preservation=Conservación de materiales · Mastery Guild=Gremio de maestría · Technique=Técnica · Turn(s)=Turno(s) · Stack(s)=Acumulación(es) · Ward=Protección · Interval=Intervalo · Chance=Probabilidad · Damage=Daño · Upgrade=Mejorar · Save (sustantivo)=Partida guardada · Load=Cargar · Options=Opciones · Language=Idioma · Melvor Cloud=Melvor Cloud · Offline Progress=Progreso sin conexión · Gamemode=Modo de juego · Aurora=Aurora · Beastslayer=Matabestias · Agility Marks=Marcas de agilidad · Clearwater=Clearwater (nombres propios de lugares sin traducir salvo que estén en el glosario)
