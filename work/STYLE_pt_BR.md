# Regras de tradução Melvor Idle 2 → Português do Brasil

## Estilo
- Tratamento por **você**, como a tradução oficial brasileira do Melvor Idle 1: «Tem certeza de que deseja …?», «Escolha …».
- Português do Brasil natural de jogo, conciso. Botões e títulos curtos.
- Texto em MAIÚSCULAS no inglês: também em maiúsculas em português. Title Case inglês → maiúscula só na primeira palavra (e nomes próprios), salvo nomes de habilidades e itens do glossário.
- Espaço antes de «%» não é usado no Brasil («20%»).
- Sem travessão nem meia-risca (– —) como pontuação; use vírgula, dois-pontos ou parênteses.
- Os termos de `work/glossary_pt_BR.tsv` (Melvor Idle 1 oficial, EN<TAB>PT) têm prioridade. Busca: `grep -P "^Termo\t" work/glossary_pt_BR.tsv`.
- Nomes de itens e monstros: se estiverem no glossário, copie exatamente. Senão, traduza no mesmo estilo.
- Mesmo nome inglês = mesma tradução em todo lugar. Antes de traduzir um nome, procure se já existe em `work/pt_BR/*.json`.

## Intocável (senão `python tools/build.py --lang pt_BR --check` falha)
- Tudo entre `{…}` fica idêntico caractere por caractere, ex. `{Value:+0.##%;-#.##%}`, `{LocalContext.Item.DisplayName}`, `{0:N0}`. A ordem na frase pode mudar.
- Exceção: em `{Value:cond:<0?Decreased|>=0?Increased}` só se traduzem as palavras após `?`: `{Value:cond:<0?Reduzido|>=0?Aumentado}`.
- Tags BBCode `[b]`, `[/b]`, `[color=#…]`, `[img height=…]`, `[effectIcon/]`, `[ul]` etc.: idênticas e na mesma quantidade.
- `[Companion Name]`, `[Icon]`, `[seconds]`, `[pixels]`, `[Sighting]`, `[Observation]` e outras palavras entre colchetes são marcadores do jogo: não traduzir.
- Mesmo número de quebras de linha `\n`. Mantenha espaços no início e no fim.
- Textos de origem aparentemente quebrados (ex. `{DungeonIcon[/img]`): copie como estão.
- Plurais (`en_plural`): `["singular", "plural"]`. Em português o singular vale para 0 e 1.

## Termos básicos (Melvor Idle 1 oficial)
Woodcutting=Corte de Lenha · Fishing=Pesca · Firemaking=Arte do Fogo · Cooking=Culinária · Mining=Mineração · Smithing=Metalurgia · Thieving=Roubo · Fletching=Fabricação de Flechas · Crafting=Artesanato · Runecrafting=Criação de Runas · Herblore=Herbologia · Agility=Agilidade · Astrology=Astrologia · Farming=Agricultura · Summoning=Evocação · Slayer=Extermínio · Slayer Coins=Moedas de Extermínio · Attack=Ataque · Strength=Força · Defence=Defesa · Hitpoints=Pontos Vitais · HP=PV · Ranged=Combate à Distância · Magic=Magia · Prayer=Oração · Combat=Combate · Mastery=Proficiência · Mastery Pool=Fundo de Proficiência · Equipment=Equipamentos · Shop=Loja · Bank=Banco · Bank Space=Espaços no Banco · GP=Moedas de Ouro · Gold=Ouro · Level=Nível · Ore=Minério · Bar=Barra · Bones=Ossos · Food=Comida · Arrows=Flechas · Rune Essence=Essência Rúnica · Evasion=Evasão · Damage Reduction=Redução de Dano · Stealth=Furtividade · Special Attack=Ataque Especial · Stun=Atordoamento · Poison=Veneno · Golbin=Golbin · Completion Log=Registro de Conclusão · Statistics=Estatísticas · Settings=Configurações · Archaeology=Arqueologia · Cartography=Cartografia · Corruption=Corrupção · Unlock=Desbloquear · Locked=Bloqueado · Cancel=Cancelar · Confirm=Confirmar · Save (botão)=Salvar · Items=Itens

## Termos novos do Melvor Idle 2 (fixados, use sempre)
Hunting=Caça · Ranching=Pecuária · Animal Husbandry=Cuidado de Animais · Beastcrafting=Artesanato Bestial · Toolbelt=Cinto de Ferramentas · Quest(s)=Missão(ões) · Recipe=Receita · Skill=Habilidade · Experience/XP=Experiência/XP · Item=Item · Pet=Mascote · Loot=Espólio · Dungeon=Masmorra · Monster=Monstro · Boss=Chefe · Area=Área · Potion=Poção · Rune=Runa · Seed=Semente · Logs=Toras · Max Hit=Acerto Máx. · Accuracy=Precisão · Charges=Cargas · Modifier=Modificador · Preservation=Preservação · Output Doubling=Duplicação de Produção · Input Preservation=Preservação de Materiais · Mastery Guild=Guilda de Proficiência · Technique=Técnica · Turn(s)=Turno(s) · Stack(s)=Acúmulo(s) · Ward=Barreira (Protection=Proteção) · Interval=Intervalo · Chance=Chance · Damage=Dano · Upgrade=Melhorar · Save (substantivo)=Jogo Salvo · Load=Carregar · Options=Opções · Language=Idioma · Melvor Cloud=Melvor Cloud · Offline Progress=Progresso Offline · Gamemode=Modo de Jogo · Aurora=Aurora · Beastslayer=Mata-feras · Agility Marks=Marcas de Agilidade · Clearwater=Clearwater (nomes próprios de lugares sem tradução, salvo se estiverem no glossário)
Dawnsteel=Aço da Aurora · Mallet=Maço (Rune Mallet=Maço Rúnico) · Defender (escudo)=Defensora · Slime=Gosma · Silt=Lodo · Dracolith=Dracolith · Wurm=Verme (Sand Wurm=Verme da Areia, glossário) · Charcoal=Carvão Vegetal · Coal=Carvão · Agility Obstacle=Obstáculo
