# Çeviri kuralları Melvor Idle 2 → Türkçe (tr_TR)

## Üslup
- Melvor Idle 1'in resmî Türkçe çevirisi gibi (`work/tr_TR/mi1.json`, üslup örnekleri). Doğal, akıcı oyun Türkçesi; kelimesi kelimesine çeviri değil.
- Oyuncuya **sen** diye hitap edilir (Melvor Idle 1 gibi): «Seç», «Emin misin?», «Kazandın», «Envanterin dolu». «Siz» ve «-iniz/-ınız» kullanma (birden fazla kişiye hitap eden diyaloglar hariç: «Siz ikiniz» yerine «İkiniz» de olur).
- Düğmeler ve kısa etiketler: emir kipi veya isim, noktasız ve kısa: «Kaydet», «Satın Al», «Kilidini Aç», «Onayla», «İptal».
- Başlıklar ve eşya/canavar/alan/görev adları Title Case ile (Melvor Idle 1 gibi): «Yakın Dövüş İsabet İksiri», «Meşe Kütüğü». Açıklamalar tam cümle ve noktalı.
- İngilizcede BÜYÜK HARF olan metinler Türkçede de büyük harf; Türkçe büyük harf kuralları: i → İ, ı → I («İPTAL», «AYARLAR»).
- Yüzde: Türkçede yüzde işareti sayıdan önce gelir: «%15», «+%10». Ama `{…}` yer tutucuları oyunun kendisi biçimlendirir, onlara dokunma (örn. `{Value:+0.##%}` olduğu gibi kalır).
- Ondalık ayırıcı virgül: «0,5 sn.».
- Tire, uzun tire (– —) ve « - » noktalama olarak yok; virgül, iki nokta, parantez veya üç nokta kullan.
- `work/glossary_tr_TR.tsv` (Melvor Idle 1 resmî, EN<TAB>TR) önceliklidir. Arama: `grep -P "^Terim\t" work/glossary_tr_TR.tsv`. Sözlükte olmayan terimleri `work/tr_TR/mi1.json` içinde ara.
- Aynı İngilizce ad her yerde aynı çeviri. Bir adı çevirmeden önce `work/tr_TR/*.json` içinde var mı diye bak.
- Oyuncu ve [Companion Name] cinsiyetsizdir. Türkçede «o» zaten cinsiyetsiz; İngilizce «she/her» dese bile «kadın», «kız», «hanım» gibi kelimeler ekleme. Oyuncuya «dostum», «kardeşim» gibi hitaplar ekleme (İngilizcede «friend» varsa atla veya «dostum» yerine cümleyi yeniden kur).
- Zaman: "{0} ago" = "{0} önce", "{0} remaining" = "{0} kaldı".

## Yer tutucular ve ekler (Türkçe için en önemli kural)
- `{…}` içine ek getirilemez ve ünlü uyumu bilinmez. `{ItemName}'ı`, `{0}'da` gibi ekler YAZMA. Cümleyi ekin gerekmeyeceği şekilde kur:
  - "Requires {Skill} level {0}" → «Gerekli: {Skill} seviyesi {0}» veya «{Skill} seviyesi {0} gerekir».
  - "Kill {0} {Monster}" → «{Monster} öldür: {0}» veya «{0} adet {Monster} öldür».
  - Gerekirse açıklayıcı bir isim ekle: «{ItemName} eşyasını», «{Skill} yeteneğinde», «{Entity} bölgesinde».
- Sayıdan sonra çoğul eki yok: «5 eşya», «10 dakika», «3 Tur».
- Çoğul (`en_plural`): bu dil tek biçim kullanır (`nplurals=1`). Her zaman tek elemanlı liste yaz: `["5 eşya"]` gibi, yani `{"id": ["metin"]}`.

## Dokunulmaz (yoksa `python -X utf8 tools/build.py --lang tr_TR --check` hata verir)
- `{…}` içindeki her şey karakteri karakterine aynı kalır, ör. `{Value:+0.##%;-#.##%}`, `{LocalContext.Item.DisplayName}`, `{0:N0}`. Cümledeki sırası değişebilir.
- İstisna: `{Value:cond:<0?Decreased|>=0?Increased}` içinde yalnızca `?` sonrasındaki kelimeler çevrilir: `{Value:cond:<0?Azaltıldı|>=0?Artırıldı}`.
- BBCode etiketleri `[b]`, `[/b]`, `[color=#…]`, `[img height=…]`, `[effectIcon/]`, `[ul]` vb.: aynı ve aynı sayıda.
- `[Companion Name]`, `[Player Name]`, `[Icon]`, `[seconds]`, `[pixels]`, `[Sighting]`, `[Observation]` ve köşeli parantez içindeki diğer kelimeler oyunun işaretleridir: çevirme.
- `\n` satır sonu sayısı aynı. Baştaki ve sondaki boşluklar korunur. `\n` öncesindeki ters eğik çizgi (`\\n`) kalır.
- Bozuk görünen kaynak metinler (ör. `{DungeonIcon[/img]`): olduğu gibi kopyala.

## Temel terimler (Melvor Idle 1 resmî, tr)
Woodcutting=Odunculuk · Fishing=Balıkçılık · Firemaking=Ateş Yakma · Cooking=Aşçılık · Mining=Madencilik · Smithing=Metal İşleme · Thieving=Hırsızlık · Fletching=Menzilli Silah Yapımı · Crafting=Zanaat · Runecrafting=Run Zanaatı · Herblore=İksir Zanaatı · Agility=Çeviklik · Astrology=Astroloji · Farming=Tarım · Summoning=Çağırma · Slayer=Katliam · Slayer Coins=Katliam Sikkesi · Attack=Saldırı · Strength=Kuvvet · Defence=Savunma · Hitpoints=Sağlık Puanı · Ranged=Menzilli Dövüş · Magic=Büyü · Prayer=Lütuf · Combat=Savaş · Melee=Yakın Dövüş · Mastery=Ustalık · Mastery Pool=Ustalık Havuzu · Mastery Token=Ustalık Nişanı · Equipment=Ekipman · Shop=Mağaza · Bank=Depo · Bank Space=Depo Alanı · GP=AP (Altın Para) · Gold=Altın · Level=Seviye · Skill=Yetenek · Skill XP=Yetenek DP'si · XP=DP · Skill Level=Yetenek Seviyesi · Ore=Cevher · Bar=Külçe · Bones=Kemik · Food=Yiyecek · Arrows=Oklar · Bolts=Arbalet Okları · Rune=Run · Rune Essence=Run Özü · Evasion=Kaçınma · Accuracy=İsabet · Accuracy Rating=İsabet Oranı · Damage=Hasar · Damage Reduction=Hasar Azaltma · Stealth=Gizlenme · Special Attack=Özel Saldırı · Stun=Sersemletme · Poison=Zehir · Bleed=Kanama · Lifesteal=Sağlık Çalma · Regeneration=Sağlık Yenileme · Golbin=Golbin · Completion Log=Tamamlama Günlüğü · Statistics=İstatistikler · Settings=Ayarlar · Save (düğme)=Kaydet · Options=Seçenekler · Unlock=Kilidini Aç · Locked=Kilitli · Cancel=İptal · Confirm=Onayla · Items=Eşyalar · Archaeology=Arkeoloji · Cartography=Haritacılık · Corruption=Yozlaşma · Corrupted=Yozlaşmış · Abyssal=Cehennemî · Township=Kasaba İdaresi · Pet=Hayvan (Boss Pet=Baş Düşman Hayvanı) · Loot=Ganimet · Dungeon=Zindan · Monster=Canavar · Boss=Baş Düşman · Area=Alan · Potion=İksir · Seed=Tohum · Logs=Kütük (Normal Logs=Normal Kütük, Oak Logs=Meşe Kütüğü) · Charges=Şarj · Modifier=Niteleyici · Preservation=Tasarruf · Upgrade=Geliştirme (fiil: Geliştir) · Language=Dil · Offline=Çevrimdışı · Gamemode=Oyun Modu · Recipe=Tarif · Turn=Tur · Interval=Aralık · Chance=Olasılık · Stack=Birikme · Shard=Parçacık · Barrier=Bariyer · Herb=Şifalı Ot · Gem=Değerli Taş · Weapon=Silah · Armour=Zırh
Eşyalar: Staff=Değnek · Crossbow=Arbalet · Platebody=Göğüs Zırhı · Platelegs=Bacak Zırhları · Helmet=Miğfer · Boots=Botlar · Gloves=Eldivenler · Shield=Kalkan · Amulet=Tılsım · Ring=Yüzük · Cape=Pelerin · Pickaxe=Kazma · Axe=Balta · Fishing Rod=Olta · Sword=Kılıç · 2H Sword=İki Elli … Kılıç · Dagger=Hançer · Scimitar=Pala · Javelin=Mızrak · Anvil=Örs · Furnace=Fırın · Bronze=Bronz · Iron=Demir · Steel=Çelik · Mithril=Mithril · Adamantite=Adamantit · Runite=Runit · Dragonite=Ejderit · Wizard=Büyücü · Elite=Elit/Seçkin (sözlüğe bak) · Raw=Ham · Burnt=Yanık
(Geri kalan her şey için önce sözlüğe, sonra mi1.json'a bak.)

## Melvor Idle 2'nin yeni terimleri (sabit, hep bunları kullan)
Hunting=Avcılık · Ranching=Hayvancılık · Animal Husbandry=Hayvan Yetiştiriciliği · Beastcrafting=Canavar Zanaatı · Toolbelt=Alet Kemeri · Toolbelt Slot=Alet Kemeri Yuvası · Quest(s)=Görev(ler) · Main Quest=Ana Görev · Side Quest=Yan Görev · Experience=Deneyim · Miniboss=Ara Baş Düşman · Max Hit=Maks. Vuruş · Output Doubling=Üretimi İkiye Katlama · Mastery Guild=Ustalık Loncası · Technique=Teknik · Ward=Koruma · Save (isim)=Kayıt · Load=Yükle · Melvor Cloud=Melvor Cloud · Offline Progress=Çevrimdışı İlerleme · Companion=Yol Arkadaşı ([Companion Name] için adı kullan) · Agility Obstacle=Engel · Loadout=Donanım Seti · Coming Soon=Yakında · Rank=Rütbe · Charm=Tılsım Taşı · Enclosure=Ağıl · Tracking=İz Sürme · Starfall=Yıldız Yağmuru · Dawnsteel=Şafak Çeliği · Slime=Balçık · Wurm=Solucan · Dracolith=Dracolith · Spear=Kargı (Javelin=Mızrak, MI1)
Anlamı olmayan özel yer ve kişi adları İngilizce kalır (Azamire, Hirane, Talm, Gol); anlamı olan adlar tutarlı biçimde çevrilir. Bir kez çevrildiyse aynen tekrar kullan.
Kısa zaman: "--h --m --s" = "-- sa -- dk -- sn" (id 10542), "/h" = "/sa" (id 09853).

## Sabitlenmiş adlar
(Her turdan sonra «English=Türkçe» biçiminde eklenir.)
