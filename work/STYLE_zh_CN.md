# 简体中文翻译规范

以游戏自带的简体中文译文（`work/zh_CN/game.json`）为准：名称、术语、句式都与它保持一致。只翻译尚缺的文本。

- 称呼玩家用“你”。按钮、标题、名称要短，句末不加句号；描述句用完整句子并加句号（。）。
- 使用全角标点（，。：；！？“”（））。英文数字与中文之间不加空格，占位符周围也不加空格（原译文有图标时如 `[effectIcon/] {0}` 保留空格）。
- 不使用破折号（——、–、—）和“ - ”，改用逗号、冒号、句号、括号或省略号（……）。
- 不增不减：条件、目标、数字、否定、增减方向都要译出。译文要自然，不要逐字直译。
- 不留英文（占位符、Melvor Cloud、RuneScape、Steam、XP、快捷键如 Ctrl + A 除外）。
- 占位符 {…}、BBCode 标签 […]、`[Companion Name]`、换行数、首尾空格必须与英文完全一致。
- 中文只有一种复数形式：有 en_plural 的条目写成只含一个元素的列表 ["…"]，占位符以 en_plural 为准。
- 性别不明的人物避免“他/她”；[Companion Name] 用名字或省略主语。

## 固定术语（官方译文）
Woodcutting=伐木 · Fishing=钓鱼 · Firemaking=生火 · Cooking=烹饪 · Mining=采矿 · Smithing=锻造 · Thieving=扒窃 · Fletching=弓匠 · Crafting=制造 · Runecrafting=符文锻造 · Herblore=草药学 · Agility=灵巧 · Astrology=星象学 · Farming=农务 · Summoning=召唤 · Attack=攻击 · Strength=力量 · Defence=防御 · Hitpoints=生命值 · Ranged=远程 · Magic=魔法 · Prayer=祝祭 · Slayer=屠杀者 · Hunting=狩猎 · Ranching=畜牧 · Beastcrafting=兽工造物 · Combat=战斗 · Mastery=精通 · Bank=仓库 · Shop=商店 · Equipment=装备 · Toolbelt=工具带 · Quest=任务 · Level=等级 · Max Hit=最大伤害 · Accuracy Rating=精准值 · Evasion=躲避 · Stun=晕眩 · Poison=中毒 · Burn=燃烧 · Bleed=流血 · Settings=设置 · Completion Log=完成情况 · Statistics=数据 · Potion=药水 · Melee=近战 · Stance=姿态 · Lifesteal=吸血 · Companion=同伴 · Unlock=解锁 · Dragon (金属)=龙岩 · Rune (金属)=符文 · Dawnsteel=黎明钢 · Adamant=精金 · Mithril=秘银 · Iron=铁制 · Copper=铜制 · Language=语言

名称的同一系列用同一格式（铁制剑、铜制大锤、火焰法杖、蓝宝石金戒指）。术语表没有的词，先在 `work/zh_CN/*.json` 里按英文搜索句中用法（Chance、Preservation、Charges、Ward、Protection 等），沿用相同译法。
