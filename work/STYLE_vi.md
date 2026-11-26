# Quy tắc dịch tiếng Việt (vi)

Dịch Melvor Idle 2 (game idle phong cách RuneScape) từ tiếng Anh sang tiếng Việt với chất lượng bản địa hóa game chuyên nghiệp. Không có bản dịch chính thức để làm mẫu, vì vậy tính nhất quán giữa các người dịch là quan trọng nhất: trước khi dịch một tên, luôn tìm bản dịch đã có trong `work/vi/*.json` và dùng đúng hình thức đó.

## Văn phong
- Xưng hô với người chơi bằng "bạn". Câu ngắn gọn, tự nhiên, đúng ngữ pháp tiếng Việt; dịch ý, không dịch từng chữ.
- Nút bấm, tiêu đề, tên gọi: ngắn, không có dấu chấm cuối. Mô tả: câu hoàn chỉnh, có dấu chấm.
- Viết hoa: chỉ viết hoa chữ cái đầu của nút/tiêu đề/tên vật phẩm ("Kiếm sắt", "Cài đặt âm thanh"); tên riêng giữ nguyên cách viết hoa.
- Không thêm, không bớt: điều kiện, mục tiêu, con số, phủ định, chiều tăng/giảm phải được dịch đầy đủ.
- Không dùng dấu gạch ngang (–, —) và " - " làm dấu câu; thay bằng dấu phẩy, dấu hai chấm, dấu ngoặc hoặc dấu chấm lửng (…). Dấu gạch nối trong khoảng số ("1 - 5") giữ như bản gốc.
- Không để lại từ tiếng Anh, trừ: placeholder, Melvor Cloud, RuneScape, Steam, Discord, XP, phím tắt (Ctrl, Shift…), tên riêng không mang nghĩa.
- Lời thoại: giọng tự nhiên theo nhân vật. Giữa các NPC có thể dùng đại từ thân mật (tôi, cậu, ta, ngươi…) phù hợp ngữ cảnh; khi nói với người chơi dùng "bạn" hoặc cách xưng hô của nhân vật nhưng nhất quán trong cùng một đoạn.
- Giới tính: theo đúng bản gốc (she = cô ấy, he = anh ấy/ông ấy, they = họ). Người chơi và [Companion Name] khi bản gốc không nói giới tính: dùng tên hoặc lược chủ ngữ, không tự thêm "anh ấy/cô ấy".
- Thời gian: "{0} ago" = "{0} trước", "{0} remaining" = "còn {0}", "in {0}" = "sau {0}".

## Kỹ thuật (bắt buộc)
- Placeholder {…}, thẻ BBCode […], `[Companion Name]`, `[Player Name]`, số lần xuống dòng, khoảng trắng đầu/cuối phải giống hệt bản tiếng Anh. Không dịch nội dung trong {…} hay tên thẻ.
- Chuỗi có dấu gạch chéo ngược ngay trước \n (\\n) giữ nguyên chuỗi đó.
- Tiếng Việt chỉ có một dạng số nhiều: mục có en_plural viết thành danh sách MỘT phần tử ["…"], placeholder theo en_plural. Không thêm "các/những" vào tên vật phẩm ("Thỏi sắt", không phải "Các thỏi sắt").
- Tên vật phẩm phải NGẮN (giao diện cửa hàng hiển thị "+1 000 <tên>" trên một dòng, tối đa khoảng 30 ký tự cho tên).

## Thứ tự trong tên ghép
Tiếng Việt: danh từ chính đứng trước, bổ ngữ đứng sau. "Iron Sword" = "Kiếm sắt", "Fire Staff" = "Gậy lửa", "Gold Sapphire Ring" = "Nhẫn vàng ngọc lam", "Super Fishing Potion" = "Thuốc câu cá siêu cấp", "Blue Dragonhide Body" = "Áo da rồng xanh". Cùng một loạt luôn dùng cùng một mẫu. Cấp bậc La Mã giữ ở cuối ("Mũ thợ săn quái III"); "(u)" = "(nâng cấp)".

## Thuật ngữ cố định
Kỹ năng: Woodcutting=Đốn gỗ · Fishing=Câu cá · Firemaking=Đốt lửa · Cooking=Nấu ăn · Mining=Khai khoáng · Smithing=Rèn · Thieving=Trộm cắp · Fletching=Chế tác cung tên · Crafting=Chế tác · Runecrafting=Chế tác phù văn · Herblore=Thảo dược · Agility=Nhanh nhẹn · Astrology=Chiêm tinh · Farming=Trồng trọt · Summoning=Triệu hồi · Hunting=Săn bắn · Ranching=Chăn nuôi · Beastcrafting=Chế tác da thú · Attack=Tấn công · Strength=Sức mạnh · Defence=Phòng thủ · Hitpoints=Máu · Ranged=Tầm xa · Magic=Phép thuật · Prayer=Cầu nguyện · Slayer=Diệt quái · Combat=Chiến đấu

Hệ thống: Mastery=Tinh thông · Mastery Guild=Hội Tinh thông · Bank=Ngân hàng · Shop=Cửa hàng · Equipment=Trang bị · Loadout=Bộ trang bị · Toolbelt=Thắt lưng công cụ · Inventory=Túi đồ · Quest=Nhiệm vụ · Main Quest=Nhiệm vụ chính · Level=Cấp · Total Level=Tổng cấp · Skill XP=XP kỹ năng · Completion Log=Nhật ký hoàn thành · Statistics=Thống kê · Settings=Cài đặt · Language=Ngôn ngữ · Save=Bản lưu (danh từ) / Lưu (động từ) · Cloud Save=Bản lưu đám mây · Offline Progress=Tiến độ ngoại tuyến · Unlock=Mở khóa · Upgrade=Nâng cấp · Recipe=Công thức · Ingredients=Nguyên liệu · Drop Table=Bảng rơi đồ · Chance=Tỉ lệ · Interval=Thời gian thực hiện · Preservation=Bảo toàn · Doubling=Nhân đôi · Charges=Lượt dùng · Modifier=Hiệu ứng cộng thêm · Bonuses=Thưởng · Companion=Bạn đồng hành · Slayer Task=Nhiệm vụ diệt quái · Slayer Master=Bậc thầy diệt quái · Dungeon=Hầm ngục · Enemy=Kẻ địch · Boss=Trùm · Miniboss=Trùm nhỏ · Area/Zone=Khu vực · Location=Địa điểm · Gold (tiền)=Vàng · Currency=Tiền tệ · Notification=Thông báo · Guild=Hội · Plot (Farming)=Ô đất · Compost=Phân bón · Enclosure=Chuồng · Journal=Nhật ký · Course (Agility)=Đường vượt chướng ngại · Obstacle=Chướng ngại vật · Shortcut=Lối tắt · Technique=Kỹ thuật · Constellation=Chòm sao · Imbuement=Thấm phép · Spell=Phép · Stance=Tư thế · Element=Nguyên tố · Distraction=Mồi nhử đánh lạc hướng · Bait=Mồi · Trap=Bẫy · Rare Species=Loài hiếm · Variant=Biến thể

Chiến đấu: Max Hit=Sát thương tối đa · Damage=Sát thương · Accuracy Rating=Chỉ số chính xác · Evasion Rating=Chỉ số né tránh · Armour=Giáp · Resistance=Kháng · Melee=Cận chiến · Stab=Đâm · Slash=Chém · Block=Đỡ · Stun=Choáng · Sleep=Ngủ · Freeze=Đóng băng · Poison=Trúng độc · Burn=Bỏng · Bleed=Chảy máu · Lifesteal=Hút máu · Auto Eat=Tự động ăn · Food=Thức ăn · Heal=Hồi máu · Turn=Lượt · Stack=Tầng · Effect=Hiệu ứng · Kill=Hạ gục · Flee=Bỏ chạy · Special Attack=Đòn đặc biệt

Vật liệu: Copper=Đồng · Bronze=Đồng thiếc · Iron=Sắt · Steel=Thép · Silver=Bạc · Gold=Vàng · Mithril=Bí ngân · Adamant/Adamantite=Tinh kim · Runite (kim loại)=Phù thạch · Rune (vật phẩm phép)=Phù văn · Dragon/Dragonite (kim loại)=Long thạch · Dawnsteel=Thép Bình Minh · Ironsteel=Thép sắt · Meteorite=Thiên thạch · Ore=Quặng · Bar=Thỏi · Logs=Gỗ · Leather=Da · Dragonhide=Da rồng · Gem=Đá quý · Sapphire=Ngọc lam · Emerald=Ngọc lục bảo · Ruby=Hồng ngọc · Diamond=Kim cương · Opal=Ngọc mắt mèo · Seed=Hạt giống · Herb=Thảo dược · Potion=Thuốc · Fragment=Mảnh

Trang bị: Sword=Kiếm · 2H Sword=Kiếm hai tay · Dagger=Dao găm · Scimitar=Mã tấu · Battleaxe=Rìu chiến · Mace=Chùy · Spear=Giáo · Helmet=Mũ giáp · Hat=Mũ · Hood=Mũ trùm · Platebody=Giáp ngực · Body=Áo · Platelegs=Giáp chân · Bottoms=Quần · Boots=Giày · Gloves=Găng tay · Shield=Khiên · Bow=Cung · Crossbow=Nỏ · Arrow=Mũi tên · Bolt=Tên nỏ · Staff=Gậy phép · Wand=Đũa phép · Robe=Áo choàng phép · Cape=Áo choàng · Amulet=Bùa hộ mệnh · Ring=Nhẫn · Pickaxe=Cuốc chim · Axe (công cụ)=Rìu · Fishing Rod=Cần câu · Skillet=Chảo · Rod (vũ khí phép)=Trượng

Tên riêng: tên người và địa danh một từ giữ nguyên (Azamire, Hirane, Melvor, Talm, Era). Địa danh, tên quái vật và danh hiệu có nghĩa thì dịch nghĩa, viết hoa từng âm tiết chính ("Broken Pass" = "Đèo Gãy", "Sleeping Stone" = "Tảng Đá Ngủ"). Đã dịch một lần thì dùng lại y hệt.

## Tên đã thống nhất
(Bổ sung sau mỗi vòng dịch theo dạng English=Tiếng Việt.)

Vòng 1 (gói 000–023):
- Staff (chung)=Gậy phép; gậy nguyên tố=Gậy gió/nước/đất/lửa; Battlestaff=Gậy chiến · Battlewand=Đũa chiến · Sceptre=Quyền trượng · Mageshield=Khiên pháp sư
- Ward=Kết giới (mọi chỗ, kể cả "Maximum Ward"=Kết giới tối đa, Ward Breaker=phá kết giới) · Defender=Khiên phụ · Mallet=Búa vồ · Boomerang=Bumerang · Javelin=Lao · Arrowtips=Đầu mũi tên · Throw Hammer=Búa ném · Twin Blades=Song đao · Morning Star=Chùy gai · Katana=Katana
- Vambraces=Hộ cổ tay · Cowl=Mũ trùm · Chaps=Quần da · Chainmail=giáp xích · Studded=đính đinh · Hard Leather=da cứng · Camo=ngụy trang · (u)=(nâng cấp) · (Lit)=(đã thắp) · (Damaged)=(hư hỏng)
- Gỗ: Normal=thường · Oak=sồi · Willow=liễu · Teak=tếch · Maple=phong · Mahogany=gụ · Yew=thủy tùng · Magic=ma thuật (Gỗ ma thuật, Cung ma thuật) · Redwood=gỗ đỏ · Hard Oak=sồi cứng
- Đá quý: Topaz=hoàng ngọc · Jadestone=ngọc bích · Black Opal=ngọc mắt mèo đen · Uncut=… thô
- Phù văn: Air/Mind/Water/Earth/Fire/Chaos/Body/Death/Decay/Blood/Soul = gió/tâm trí/nước/đất/lửa/hỗn mang/thể xác/tử thần/mục rữa/máu/linh hồn
- Vật liệu/tiền tố: Dawnsteel=thép Bình Minh (trong tên ghép viết thường "thép") · Refined=tinh luyện · Astral=tinh tú (đứng cuối) · Dragonrune=long văn · Nightscale=vảy đêm · Moonscale=vảy trăng · Nightreed=sậy đêm · Shadowflame=hắc diễm · Ivory Athanaeum=học viện ngà · Mystic=huyền bí · Infernal=hỏa ngục · Blackstone=Đá Đen · Dragon Bone=xương rồng (Cactus=cây xương rồng)
- Bậc: Basic/Reinforced/Fortified=cơ bản/gia cố/kiên cố · Novice/Intermediate/Adept/Elite=sơ cấp/trung cấp/trung cấp/tinh nhuệ · "X Rank N"=X bậc N · Hội: Initiate=Nhập môn, Apprentice=học việc, Journeyman=lành nghề, Skilled=thành thạo, Veteran=lão luyện, Prime=thượng thừa
- Thuốc: "Thuốc <kỹ năng> P1-A", Super=… siêu cấp ("Thuốc câu cá siêu cấp P1-A")
- Sinh vật: Elk=nai · Caribou=tuần lộc · Wildebeast=linh dương đầu bò · Phantom=bóng ma · Spectre=u linh · Harpy=yêu điểu · Raptor=mãnh cầm · Griffin=sư điểu · Wurm=giun khổng lồ · Wyvern=phi long · Drake=tiểu long · Stonehopper=Châu Chấu Đá · Soulsmith=Thợ Rèn Hồn · Golbin, Dracolith, Kraken giữ nguyên
- Chiến đấu/hệ thống: Power Rating=chỉ số uy lực · Protection Rating=chỉ số bảo vệ · critical hit=chí mạng · Crush=Đập · Accurate=Chuẩn xác · Powerful=Uy lực · Long-Range=Tầm dài · Stealth=độ ẩn nấp · Fortune=vận may · Tracking=truy dấu · Trapping=đặt bẫy · Knowledge (Chiêm tinh)=tri thức · Junk=rác · Gold Pieces=Vàng · Slayer Coins=Xu diệt quái · Prayer Points=Điểm cầu nguyện · Set Bonus=Thưởng bộ · Toolbelt slot=ô thắt lưng công cụ · Geode=Hốc tinh thể · Lantern=Đèn lồng · "Act 1 - X"=Hồi 1: X

Vòng 2 (gói 024–038):
- Viết hoa: tên vật phẩm chỉ viết hoa chữ đầu ("Nanh bão"); tên kẻ địch/trùm viết hoa từng âm tiết ("Nanh Bão", "Thạch Nhân"); danh hiệu trùm sau dấu phẩy ("Kythiss, Nữ Hoàng Nọc Độc"); "Phase N" = "(giai đoạn N)".
- Nhanh nhẹn: chướng ngại vật "<Đường> N, chướng ngại vật đơn giản/nâng cao K" · Climbing=Leo trèo · Jumping=Nhảy · Evading=Né tránh · Balancing=Giữ thăng bằng · Rappelling=Đu dây
- Chiêm tinh: Starfall=Sao rơi (cả trong tên vật phẩm) · Blue Moon=Trăng xanh · Blood Moon=Trăng máu · Sighting=Phát hiện · Observation=Quan sát · Rare Event=Sự kiện hiếm · "X's Pathway"=Lối đi của X · Astral Learning=Học vấn tinh tú · tên chòm sao giữ nguyên
- Chiến đấu: "A vs. B"=A khắc B · Neutral=Trung tính · Normal Damage=Sát thương thường · Golem=Thạch Nhân · Amalgamation=Hợp Thể · Elemental=Nguyên Tố
- Trồng trọt: Allotment=Ruộng rau · Herb plot=Ô thảo dược · Tree plot=Ô cây · Orchard=Vườn cây ăn quả · Compost Bin=Thùng ủ phân · "X Tree"=Cây X · Potency=Hiệu lực
- Đốt lửa/khai khoáng: "X Bonfire"=Lửa trại gỗ X · Brazier=Chậu lửa · Vein=Mạch · Fallen Star=Ngôi sao rơi
- Săn bắn: Tracking Stick=Gậy truy dấu · Binoculars=Ống nhòm · Animal Whistle=Còi gọi thú · Spirit Lantern=Đèn lồng linh hồn · Air/Water/Earth/Fire Spirit=Tinh linh gió/nước/đất/lửa · Alpha X=X đầu đàn · Tame=thuần hóa · Wild=hoang
- Cá: Trout=Cá hồi vân (Raw Trout=Cá hồi vân sống); món nấu chín mang đúng tên vật phẩm
- Địa danh/nhân vật: the capital=kinh đô · Windswept Shores=Bờ Gió Quật · Windy Coastline=Bờ Biển Lộng Gió · Lifebinder Pool=Hồ Kết Sinh · Lemvor Pier=Bến Tàu Lemvor · Spiced Honey Tavern=Quán rượu Mật Ong Gia Vị · Slayers Guild=Hội Diệt quái · Blackthorn Sisters=Chị em nhà Blackthorn · Archivist=Người giữ văn khố · Hacksmith=Thợ Rèn Vụng · Dwarf=Người lùn · Harvest Festival=Lễ hội mùa gặt
- Xưng hô đã dùng: Gol tự xưng "Gol", gọi người chơi "bạn hiền", lời kể gọi "gã" · Whudgrath: ta/ngươi, "nhóc", lời kể "ông ấy" · Lira: tôi/bạn, người chơi gọi "cô" · Hapren, Morlin, Dixon: "ông" (Dixon gọi người chơi "cậu") · Magnavous: "cô", gọi Lira "chị" · Petal là chị, Clove là em
- Địa danh (vòng 039 đến 062): The Sealed Grove=Khu Rừng Phong Ấn · Soothsayer's Grove=Khu Rừng Tiên Tri · Elder Grove=Khu Rừng Cổ Thụ · Ringleader's Fortress=Pháo Đài Thủ Lĩnh · Old Northern Road=Đường Bắc Cũ · Foggy Canyon=Hẻm Núi Sương Mù · Heartroad=Đường Huyết Mạch · Clearwater=Thanh Thủy · Flinkcrest Highlands=Cao Nguyên Flinkcrest · Broken Pass=Đèo Gãy · Sleeping Stone=Tảng Đá Ngủ · Perilous Peaks=Dãy Núi Hiểm Nguy ("the Peaks"=Dãy Núi) · Bridge of Kings=Cầu Quân Vương · Ivory Athenaeum (địa danh)=Học Viện Ngà · Riverbend=Khúc Sông · Rimeriver Crevice=Khe Sông Sương Giá · Tidebreak=Sóng Vỡ · Gloomstone=Đá U Ám · Respite=Chốn An Nghỉ · the Dream=Giấc Mộng · Stoneway=Đường Đá · Stoneway Station=Ga Đường Đá · Nalidasi Archives=Văn khố Nalidasi · Royal Archives=Văn khố Hoàng gia · Koganusan giữ nguyên
- Nhóm/sinh vật: Ringleader=Thủ lĩnh · Ent=người cây (ent guardians=thần cây hộ vệ) · Militia=đội dân quân · Militia Captain=Đội trưởng dân quân · Lifebinders=tộc Kết Sinh · Fateseekers=tộc Truy Mệnh · Dreamers=Người Mộng · Titan=Người Khổng Lồ · Titan Wars=Chiến tranh Người Khổng Lồ · thrall=xác nô · Soulsmiths=Thợ Rèn Hồn · Soulsmith Elites=Thợ Rèn Hồn Tinh Nhuệ · Summoner=Triệu hồi sư · Yeti=người tuyết · Rockwolf=Sói Đá · Stonehopper=Châu Chấu Đá · Sea Griffon=Sư Điểu Biển · golem trong lời kể=thạch nhân · Nalidasi/Flamberian Dwarves=người lùn Nalidasi/Flamberian
- Khác: talisman=bùa chú · rock bolt=chốt neo đá · Slabglider=Xe Trượt Phiến Đá · Stoneglider=Xe Trượt Đá · Linking=Lễ Nối Liền · the Hauling=Hội Kéo Lưới · Sightsmoke=Khói Thấu Thị · vision=linh ảnh · magical barrier=rào chắn phép thuật (Kết giới chỉ cho Ward) · Divination=Tiên tri · Stonemelon=Dưa đá · Cobblestone Soup=Súp đá cuội
- Tên nhiệm vụ: Fishin' for Trouble=Câu Phải Rắc Rối · Dwarf Blood=Dòng Máu Người Lùn · Stoneway Yourway=Đường Đá Đường Ta · Prince Procurement=Giải Cứu Hoàng Tử · Repairing What Remains=Sửa Chữa Những Gì Còn Lại · Slug Slayer=Kẻ Diệt Sên; "Tiêu đề - Mô tả" viết thành "Tiêu đề: Mô tả"
- Xưng hô (039 đến 062): người chơi và bạn đồng hành: mình/tôi và cậu, "chúng ta/bọn mình" · Jass: tôi/cậu, được gọi "cô" · Gloob: tôi, lời kể "nó" · Talm: "anh ta", được gọi "anh"; ở Chốn An Nghỉ Talm và Era xưng "ta", Talm gọi "ngươi", Era gọi "con" · Era: "cô ấy", được gọi "cô" · Curo: tôi/hai vị · Vua người lùn và Người giữ văn khố: ta/các vị, được gọi "ngài" · Redilok: tôi/hai người · Zotty: ta/các cậu · Kajc: ta/các bạn · Thủ lĩnh: mày/lũ người
