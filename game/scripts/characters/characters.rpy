# define z = Character("xman", color="FD97E2")
# define e = Character("Eileen", color="FD97E2")
# define d = Character("Dave")
default all_girls = []

default monmc = "landlady"
default mcmon = "tenant"
default ashmc = "friend"
default mcash = "friend"
default linmc = "friend"
default mclin = "friend"

default unk = Character("?????", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default aphrodite = Girl(1, "Aphrodite", False, 0, "Goddes", "Your Boss", "Friendly", 0, "0", 1, "Single", "She is nymphomaniac")
define aph = Character("Aphrodite", what_color = "#c02566ff", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"))
define aph_shout = Character("Aphrodite", what_color = "#c02566ff",  what_size=43, namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"))
define aph_thought = Character("Aphrodite",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#c02566ff"), "gui/namebox.png"))

default linda = Girl(2, "Linda", False, 0, "Half Elf", "Friend", "Friendly", 0, "1", 1, "Single", "She dreams to have a big brother")
define lin = Character("Linda", namebox_background=AlphaMask(Solid("#18454d"), "gui/namebox.png"), what_color = "#1b4c55", )
define lin_shout = Character("Linda",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define lin_thought = Character("Linda",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default monica = Girl(3, "Monica", False, 0, "Human", "LandLady", "Friendly", 0, "0", 1, "Married", "Her dream is to have a son")
define mon = Character("Monica", namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"), what_color = "#943131",)
define mon_shout = Character("Monica",  what_size=43, namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"), what_color = "#943131",)
define mon_thought = Character("Monica",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#943131"), "gui/namebox.png"))

default ashley = Girl(4, "Ashley", False, 0, "Half Elf", "Friend", "Frenemy", 0, "1", 1, "Single", "She loves to be on comand")
define ash = Character("Ashley", namebox_background=AlphaMask(Solid("#372657"), "gui/namebox.png"), what_color = "#372657",)
define ash_shout = Character("Ashley",  what_size=43, namebox_background=AlphaMask(Solid("#372657"), "gui/namebox.png"), what_color = "#372657",)
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
define deb = Character("Debbie", namebox_background=AlphaMask(Solid("#203e23"), "gui/namebox.png"), what_color = "#203e23",)
define deb_shout = Character("Debbie",  what_size=43, namebox_background=AlphaMask(Solid("#203e23"), "gui/namebox.png"), what_color = "#203e23",)
define deb_thought = Character("Debbie",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#203e23"), "gui/namebox.png"))

default anita = Girl(8, "Anita", False, 0, "Squirrel Girl", "Adventurer", "Neutral", 0, "0", 1, "Single", "She wants to become to become a powerfull warrior")
define ami = Character("Anita", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define ani_shout = Character("Anita",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define ani_thought = Character("Anita",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default makoto = Girl(9, "Makoto", False, 0, "Human", "Adventurer", "Neutral", 0, "0", 1, "Single", "She wants to become the st")
define mak = Character("Makoto", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define mak_shout = Character("Makoto",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define mak_thought = Character("Makoto",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default nina = Girl(10, "Nina", False, 0, "Human", "Friend", "Friendly", 0, "0", 1, "Single", "She loves chocolat")
define nin = Character("Nina", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define nin_shout = Character("Nina",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define nin_thought = Character("Nina",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

default sarah = Girl(11, "Sarah", False, 0, "Human", "Friend", "Friendly", 0, "0", 1, "Single", "She loves chocolat")
define sar = Character("Sarah", namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#3c2323")
define sar_shout = Character("Sarah", what_size = 40, namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#3c2323")
define sar_thought = Character("Sarah", namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#3c2323")
define sar_wisper = Character("Sarah",what_size = 15,  namebox_background=AlphaMask(Solid("#3c2323"), "gui/namebox.png"), what_color = "#3c2323")

default shino = Girl(12, "Shino", False, 0, "?????", "Enemy", "Friendly", 0, "0", 1, "???????", "?????????")
define shi = Character("Shino", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define shi_shout = Character("Shino",  what_size=43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
define shi_thought = Character("Shino",  what_color = "#96989E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))

define notif = Character("Notification", what_color ="#000000cf")