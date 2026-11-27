# Regras de tradução Melvor Idle 2 → Português de Portugal (pt_PT)

## Estilo
- Português **europeu** (não brasileiro), como a tradução oficial portuguesa do Melvor Idle 1 (`work/pt_PT/mi1.json`, exemplos de estilo).
- Tratamento por **tu**, como no Melvor Idle 1: «O teu ataque cura-te…», «Tens a certeza de que queres…?», «Escolhe…». Pronomes átonos em ênclise segundo a norma europeia («cura-te», «dá-lhe», «encontra-o»); próclise só onde a gramática europeia exige (negação, «que», advérbios: «não te esqueças», «já o tens»).
- Imperativo de «tu» nos botões e instruções quando houver verbo: «Guardar» (infinitivo em botões, como no MI1) mas «Clica para…», «Escolhe…» em frases.
- Vocabulário europeu: ecrã (não tela), guardar (não salvar), definições (não configurações), utilizador, equipa, registo, ficheiro, rato, telemóvel, autocarro, pequeno-almoço, sumo, comboio, casa de banho, receção, «estar a + infinitivo» (não gerúndio: «a carregar…», não «carregando…»).
- Ortografia do Acordo Ortográfico de 1990, como o MI1: ação, ações, atual, ótimo, receção.
- Português natural de jogo, conciso. Botões e títulos curtos, sem ponto final. Descrições com frases completas e ponto final.
- Texto em MAIÚSCULAS no inglês: também em maiúsculas. Title Case inglês → maiúscula só na primeira palavra (e nomes próprios), salvo nomes do glossário.
- Sem espaço antes de «%» («20%»). Sem travessão nem meia-risca (– —) como pontuação, nem « - »; use vírgula, dois-pontos, parênteses ou reticências.
- Os termos de `work/glossary_pt_PT.tsv` (Melvor Idle 1 oficial, EN<TAB>PT) têm prioridade. Busca: `grep -P "^Termo\t" work/glossary_pt_PT.tsv`.
- Nomes de itens e monstros: se estiverem no glossário, copie exatamente. Senão, traduza no mesmo estilo.
- Mesmo nome inglês = mesma tradução em todo lugar. Antes de traduzir um nome, procure se já existe em `work/pt_PT/*.json`.
- Género neutro para o jogador e para [Companion Name] quando o inglês não indica género: reformule («Obtiveste…», «[Companion Name] acena»), evite adjetivos com género referidos ao jogador.
- Tempo: "{0} ago" = "há {0}", "{0} remaining" = "faltam {0}".

## Intocável (senão `python -X utf8 tools/build.py --lang pt_PT --check` falha)
- Tudo entre `{…}` fica idêntico caractere por caractere, ex. `{Value:+0.##%;-#.##%}`, `{LocalContext.Item.DisplayName}`, `{0:N0}`. A ordem na frase pode mudar.
- Exceção: em `{Value:cond:<0?Decreased|>=0?Increased}` só se traduzem as palavras após `?`: `{Value:cond:<0?Reduzido|>=0?Aumentado}`.
- Tags BBCode `[b]`, `[/b]`, `[color=#…]`, `[img height=…]`, `[effectIcon/]`, `[ul]` etc.: idênticas e na mesma quantidade.
- `[Companion Name]`, `[Player Name]`, `[Icon]`, `[seconds]`, `[pixels]`, `[Sighting]`, `[Observation]` e outras palavras entre colchetes são marcadores do jogo: não traduzir.
- Mesmo número de quebras de linha `\n`. Mantenha espaços no início e no fim. Barra invertida antes de `\n` (`\\n`) fica.
- Textos de origem aparentemente quebrados (ex. `{DungeonIcon[/img]`): copie como estão.
- Plurais (`en_plural`): `["singular", "plural"]`. Em português europeu o singular vale só para 1 (0 é plural: «0 itens»).

## Termos básicos (Melvor Idle 1 oficial, pt)
Woodcutting=Corte de Lenha · Fishing=Pesca · Firemaking=Arte do Fogo · Cooking=Cozinhar · Mining=Extração · Smithing=Trabalhos de Ferreiro · Thieving=Roubo · Fletching=Arco e Flecha · Crafting=Artesanato · Runecrafting=Criação de Runas · Herblore=Especialidade em Ervas · Agility=Agilidade · Astrology=Astrologia · Farming=Cultivo · Summoning=Invocação · Slayer=Assassino · Slayer Coins=Moedas de Assassino · Attack=Ataque · Strength=Força · Defence=Defesa · Hitpoints/HP=Pontos de Vida · Ranged=À Distância · Magic=Magia · Prayer=Oração · Combat=Combate · Mastery=Especialização · Mastery Pool=Conjunto de Especialização · Equipment=Equipamento · Shop=Loja · Bank=Banco · Bank Space=Espaço no Banco · GP=Peças de Ouro · Gold=Ouro · Level=Nível · Ore=Minério · Bar=Barra · Bones=Ossos · Food=Alimentos · Arrows=Setas · Rune Essence=Essência da Runa · Evasion=Evasão · Damage Reduction=Redução de Dano · Stealth=Ação Furtiva · Special Attack=Ataque Especial · Stun=Atordoamento · Poison=Veneno · Golbin=Golbin · Completion Log=Registo de conclusão · Statistics=Estatísticas · Settings=Definições · Save (botão)=Guardar · Options=Opções · Unlock=Desbloquear · Locked=Bloqueado · Cancel=Cancelar · Confirm=Confirmar · Items=Itens · Archaeology=Arqueologia · Cartography=Cartografia · Corruption=Corrupção · Coal/Charcoal=Carvão · Skill=Habilidade
(Para tudo o resto, consulte primeiro o glossário.)

## Termos novos do Melvor Idle 2 (fixados, use sempre)
Hunting=Caça · Ranching=Pecuária · Animal Husbandry=Criação de Animais · Beastcrafting=Artesanato Bestial · Toolbelt=Cinto de Ferramentas · Quest(s)=Missão(ões) · Recipe=Receita · Experience/XP=Experiência/XP · Pet=Mascote · Loot=Espólio · Dungeon=Masmorra · Monster=Monstro · Boss=Chefe · Miniboss=Subchefe · Area=Área · Potion=Poção · Rune=Runa · Seed=Semente · Logs=Toros · Max Hit=Golpe Máx. · Accuracy=Precisão · Charges=Cargas · Modifier=Modificador · Preservation=Preservação · Output Doubling=Duplicação de Produção · Mastery Guild=Guilda de Especialização · Technique=Técnica · Turn(s)=Turno(s) · Stack(s)=Acumulação(ões) · Ward=Barreira · Interval=Intervalo · Chance=Probabilidade · Damage=Dano · Upgrade=Melhoria (verbo: Melhorar) · Save (substantivo)=Jogo Guardado · Load=Carregar · Language=Idioma · Melvor Cloud=Melvor Cloud · Offline Progress=Progresso Offline · Gamemode=Modo de Jogo · Beastslayer=Mata-feras · Agility Marks=Marcas de Agilidade · Agility Obstacle=Obstáculo · Dawnsteel=Aço da Aurora · Mallet=Maço · Defender (escudo)=Defensora · Slime=Gosma · Wurm=Verme · Dracolith=Dracolith · Companion=Companheiro (para [Companion Name] use o nome)
Nomes próprios de lugares e pessoas sem significado ficam como no inglês (Azamire, Hirane, Talm); nomes com significado traduzem-se de forma consistente. Uma vez traduzido, reutilize exatamente.

## Nomes já fixados
(Acrescentar após cada ronda no formato English=Português.)
