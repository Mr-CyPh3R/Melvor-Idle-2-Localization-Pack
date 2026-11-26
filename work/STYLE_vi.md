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
