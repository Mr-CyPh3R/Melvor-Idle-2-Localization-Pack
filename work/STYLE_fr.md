# Règles de traduction Melvor Idle 2 → Français

## Style
- Vouvoiement (**vous**), comme la traduction officielle française de Melvor Idle 1 : « Êtes-vous sûr … ? », « Choisissez … ».
- Français naturel de jeu vidéo, concis. Boutons et titres courts.
- Texte en MAJUSCULES en anglais : en majuscules aussi en français. Title Case anglais → majuscule seulement au premier mot (et noms propres).
- Typographie française : espace avant « : ; ! ? » et « % » (« 20 % »), sauf si le signe suit directement un placeholder `{…}`. Guillemets « … » pour les citations.
- Pas de tiret cadratin ni demi-cadratin (– —) comme ponctuation ; utiliser virgule, deux-points ou parenthèses.
- Les termes de `work/glossary_fr.tsv` (Melvor Idle 1 officiel, EN<TAB>FR) sont prioritaires. Recherche : `grep -P "^Terme\t" work/glossary_fr.tsv`.
- Noms d'objets et de monstres : si présents dans le glossaire, les reprendre exactement. Sinon, traduire dans le même style (« Iron Dagger » → « Dague de fer », « Oak Logs » → « Bûches de chêne »).
- Même nom anglais = même traduction partout. Avant de traduire un nom, chercher s'il est déjà traduit dans `work/fr/*.json`.

## Intouchable (sinon `python tools/build.py --lang fr --check` échoue)
- Tout ce qui est entre `{…}` reste identique caractère par caractère, ex. `{Value:+0.##%;-#.##%}`, `{LocalContext.Item.DisplayName}`, `{0:N0}`. L'ordre dans la phrase peut changer.
- Exception : dans `{Value:cond:<0?Decreased|>=0?Increased}` seuls les mots après `?` se traduisent : `{Value:cond:<0?Réduit|>=0?Augmenté}`.
- Balises BBCode `[b]`, `[/b]`, `[color=#…]`, `[img height=…]`, `[effectIcon/]`, `[ul]` etc. : identiques et en même nombre.
- `[Companion Name]`, `[Icon]`, `[seconds]`, `[pixels]`, `[Sighting]`, `[Observation]` et autres mots entre crochets sont des marqueurs du jeu : ne pas traduire.
- Même nombre de retours à la ligne `\n`. Garder les espaces au début et à la fin.
- Textes sources apparemment cassés (ex. `{DungeonIcon[/img]`) : recopier tels quels.
- Pluriels (`en_plural`) : `["singulier", "pluriel"]`. En français le singulier sert pour 0 et 1.

## Termes de base (Melvor Idle 1 officiel)
Woodcutting=Coupe de bois · Fishing=Pêche · Firemaking=Feu de camp · Cooking=Cuisine · Mining=Exp. minière · Smithing=Métallurgie · Thieving=Larcin · Fletching=Archerie · Crafting=Artisanat · Runecrafting=Créa. de runes · Herblore=Herboristerie · Agility=Agilité · Astrology=Astrologie · Farming=Agriculture · Summoning=Invocation · Slayer=Pourfendeur · Slayer Coins=Pièces de Pourfendeur · Attack=Attaque · Strength=Force · Defence=Défense · Hitpoints=Constitution · Ranged=Cbt à distance · Magic=Magie · Prayer=Prières · Combat=Combat · Mastery=Maîtrise · Mastery Pool=Réserve de maîtrise · Equipment=Équipement · Shop=Magasin · Bank=Banque · Bank Space=Espace bancaire · GP=PO · Gold=Or · Level=Niveau · Ore=Minerai · Bar=Lingot · Bones=Os · Food=Aliment · Arrows=Flèches · Rune Essence=Essence runique · Evasion=Esquive · Damage Reduction=Réduction de dégâts · Stealth=Furtivité · Special Attack=Attaque spéciale · Stun=Étourdissement · Poison=Empoisonnement · Golbin=Golbin · Completion Log=Journal d'accomplissement · Statistics=Statistiques · Settings=Paramètres · Archaeology=Archéologie · Cartography=Cartographie · Corruption=Corruption · Unlock=Débloquer · Locked=Verrouillé · Cancel=Annuler · Confirm=Confirmer · Save (bouton)=Sauvegarder

## Nouveaux termes Melvor Idle 2 (fixés, à utiliser partout)
Hunting=Chasse · Ranching=Élevage · Animal Husbandry=Soins des animaux · Beastcrafting=Façonnage bestial · Toolbelt=Ceinture à outils · Quest(s)=Quête(s) · Recipe=Recette · Skill=Compétence · Experience/XP=Expérience/XP · Item=Objet · Pet=Familier · Loot=Butin · Dungeon=Donjon · Monster=Monstre · Boss=Boss · Area=Zone · Potion=Potion · Rune=Rune · Seed=Graine · Logs=Bûches · Max Hit=Coup max. · Accuracy=Précision · Charges=Charges · Modifier=Modificateur · Preservation=Préservation · Output Doubling=Doublement de production · Input Preservation=Préservation des ressources · Mastery Guild=Guilde de maîtrise · Technique=Technique · Turn(s)=Tour(s) · Stack(s)=Cumul(s) · Ward=Protection · Interval=Intervalle · Chance=Chance · Damage=Dégâts · Upgrade=Améliorer · Save (nom)=Sauvegarde · Load=Charger · Options=Options · Language=Langue · Melvor Cloud=Melvor Cloud · Offline Progress=Progression hors ligne · Gamemode=Mode de jeu · Aurora=Aurore · Beastslayer=Tueur de bêtes · Agility Marks=Marques d'agilité · Clearwater=Clearwater (noms de lieux propres non traduits sauf s'ils sont dans le glossaire)
