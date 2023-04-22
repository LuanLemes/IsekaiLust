
image side aphrodite = "side/saphrodite.webp"
image side linda = "side/slinda.webp"
image side mc = "side/smc.webp"
image side monica = "side/smonica.webp"
image side debbie = "side/sdebbie.webp"
image side ashley = "side/sashley.webp"
image side sarah = "side/ssarah.webp"
image side makoto = "side/smakoto.webp"
image side book = "side/sbook.webp"
image side ung = "side/sung.webp"
image side lilith = "side/slilith.webp"

default all_girls = []
define narrator = Character('', what_color='#ffffff',namebox_background=AlphaMask(Solid("#ff7f7f00"), "gui/namebox.png"))
define dev = Character("Developer", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default monmc = "landlady"
default mcmon = "tenant"
default ashmc = "friend"
default mcash = "friend"
default linmc = "friend"
default mclin = "friend"

define unk = Character("?????", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#000000") ])

define boo = Character("Book of Aphrodite",image = "book", what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#433a02"), "gui/namebox.png") , what_outlines=[ (2, "#433a02") ])

default aphrodite = Girl(1, "Aphrodite", False, 0, "Goddes", "Your Boss", "Friendly", 0, all_for_this_update_phrase, 1, "?????", "She is nymphomaniac")
define aph = Character("Aphrodite",image = "aphrodite", what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png") , what_outlines=[ (2, "#540324ff") ])
define aph_shout = Character("Aphrodite", image = "aphrodite", what_color = "#e5e5e5",  what_size=43, namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"), what_outlines=[ (2, "#540324ff") ])
define aph_thought = Character("Aphrodite",  what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"), what_outlines=[ (2, "#540324ff") ])

default linda = Girl(2, "Linda", False, 0, "Half Elf", "Friend", "Friendly", 0, "1", 1, "Single", "She dreams to have a big brother")
define lin = Character("Linda", image = "linda", namebox_background=AlphaMask(Solid("#18454d"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#0f2a2f") ])
define lin_shout = Character("Linda", image = "linda", what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#0f2a2f") ])
define lin_thought = Character("Linda",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default monica = Girl(3, "Monica", False, 0, "Human", "LandLady", "Friendly", 0, "0", 1, "Married", "Her dream is to have a son")
define mon = Character("Monica",image = "monica", namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#2f1515") ])
define mon_shout = Character("Monica", image = "monica", what_size=43, namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#2f1515") ])
define mon_thought = Character("Monica",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"))
define mon_wisper = Character("Monica", image = "monica" ,what_size = 15,  namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#321d1d") ])

default ashley = Girl(4, "Ashley", False, 0, "Half Elf", "Friend", "Frenemy", 0, "2", 1, "Single", "She loves to be on comand")
define ash = Character("Ashley", image = "ashley", namebox_background=AlphaMask(Solid("#372657"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#372657") ])
define ash_shout = Character("Ashley", image = "ashley", what_size=43, namebox_background=AlphaMask(Solid("#372657"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#372657") ])
define ash_thought = Character("Ashley",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#372657"), "gui/namebox.png"))

default ayame = Girl(5, "Ayame", False, 0, "Human", "Adventurer/Ninja", "Neutral", 0, "0", 1, "Single", "She loves purple")
define aya = Character("Ayame", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define aya_shout = Character("Ayame",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define aya_thought = Character("Ayame",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default kagome = Girl(6, "Kagome", False, 0, "Human", "Guild Masters", "Neutral", 0, "0", 1, "Single", "She loves the sound of rain")
define kog = Character("Kagome", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define kog_shout = Character("Kagome",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define kog_thought = Character("Kagome",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default debbie = Girl(7, "Debbie", False, 0, "Human", "Acquaintance", "Neutral", 0, "0", 1, "Single", "Sarah´s daugher")
define deb = Character("Debbie", image = "debbie", namebox_background=AlphaMask(Solid("#19311c"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#152617") ])
define deb_shout = Character("Debbie", image = "debbie", what_size=43, namebox_background=AlphaMask(Solid("#19311c"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#152617") ])
define deb_thought = Character("Debbie", namebox_background=AlphaMask(Solid("#19311c"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#152617") ])

default anita = Girl(8, "Anita", False, 0, "Squirrel Girl", "Adventurer", "Neutral", 0, "0", 1, "Single", "She wants to become to become a powerfull warrior")
define ami = Character("Anita", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define ani_shout = Character("Anita",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define ani_thought = Character("Anita",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default makoto = Girl(9, "Makoto", False, 0, "Human", "Adventurer", "Neutral", 0, "Take the guild exam", 1, "Single", "She wants to become strong as her master" )
define mak = Character("Makoto", image = "makoto", namebox_background=AlphaMask(Solid("#3a180e"), "gui/namebox.png"), what_color = "#e5e5e5")
define mak_shout = Character("Makoto",  image = "makoto", what_size=43, namebox_background=AlphaMask(Solid("#3a180e"), "gui/namebox.png"), what_color = "#e5e5e5")
define mak_thought = Character("Makoto",  what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#3a180e"), "gui/namebox.png"))

default nina = Girl(10, "Nina", False, 0, "Human", "Friend", "Friendly", 0, "0", 1, "Single", "She loves chocolat")
define nin = Character("Nina", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define nin_shout = Character("Nina",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define nin_thought = Character("Nina",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default sarah = Girl(11, "Sarah", False, 0, "Human", "Friend", "Friendly", 0, "0", 1, "Single", "She loves chocolat")
define sar = Character("Sarah", image = "sarah" ,namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#321d1d") ])
define sar_shout = Character("Sarah", image = "sarah", what_size = 40, namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"),what_color = "#e5e5e5", what_outlines=[ (2, "#321d1d") ])
define sar_thought = Character("Sarah", image = "sarah", namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#3c2323")
define sar_wisper = Character("Sarah",what_size = 15,  namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#e5e5e5", what_outlines=[ (2, "#321d1d") ])

default shino = Girl(12, "Shino", False, 0, "?????", "Enemy", "Friendly", 0, "0", 1, "???????", "?????????")
define shi = Character("Shino", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define shi_shout = Character("Shino",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define shi_thought = Character("Shino",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

define ung = Character("Wolf Girl?",image = "ung", what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png") , what_outlines=[ (2, "#540324ff") ])
define ung_shout = Character("Wolf Girl?", image = "ung", what_color = "#e5e5e5",  what_size=43, namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"), what_outlines=[ (2, "#540324ff") ])
define ung_thought = Character("Aphrodite",  what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"), what_outlines=[ (2, "#540324ff") ])

default lilith = Girl(13, "Lilith", False, 0, "Succubus", "Enemy", "Friendly", 0, "0", 1, "???????", "?????????")
define lunk = Character("?????",image = "lilith", what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png") , what_outlines=[ (2, "#540324ff") ])
define lil = Character("Lilith",image = "lilith", what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png") , what_outlines=[ (2, "#540324ff") ])
define lil_shout = Character("Lilith", image = "lilith", what_color = "#e5e5e5",  what_size=43, namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"), what_outlines=[ (2, "#540324ff") ])
define lil_thought = Character("Lilith",  what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"), what_outlines=[ (2, "#540324ff") ])
define lil_command = Character("?????",image = "lilith", what_color = "#e5e5e5", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png") , what_outlines=[ (2, "#540324ff") ])


define notif = Character("Notification", what_color ="#000000cf")