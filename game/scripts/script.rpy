
image picture_1 = im.Scale("bg cave.jpg", 1920, 1080)
image picture_2 = im.Scale("bg panorama.webp", 1920, 1080)
image picture_3 = im.Scale("bg whitehome.jpg", 1920, 1080)
image ball_blue = "icons/ball_blue.png"
image ball_white = "icons/ball_white.png"
image morning = "icons/morning.png"
image afternoon = "icons/afternoon.png"
image evening = "icons/evening.png"
image dawn = "icons/dawn.png"
image temp_bed = "coolbedroom"
define show_calendar = False
image button_hover = Frame ("gui/hover.png",40,40,40,40, tile=True)
image money_icon = "icons/money.png"
define focus_location = ""
define config.menu_include_disabled = True
define config.layers = ["under_bg", "under_gui", 'master', 'transient', 'screens', 'overlay' ]
default player = Player("Almir", 0, 10)

default player_inventory = Inventoryx([])
default collected_items = Inventoryx([])

default places = []
default location_object = Place(-1, "", 0, 0, False, False, 0, False, False, "")

define defined = "this is defined3"
default defaulted = "this is defaulted3"

default Place1 = Place( 0, "Selling Point",700, 500, True, True, 0, False, True, "Selling Point" )
default Place2 = Place( 1, "Home",910, 410, True, True, 1, False, True, "Home")
default Place3 = Place( 2, "Bedroom", 710, 820, False, True, 1, True, True, "Bedroom" )
default Place4 = Place( 4, "Flower Camp", 950, 219, True, True, 1, True, True, "Flower Camp")
default Place5 = Place( 5, "Forest Wall", 1200, 100, False, False, 1, True, True, "Forest Wall" )
default Place6 = Place( 6, "Hallway", 1200, 100, False, True, 1, False, True, "Hallway" )
default Place7 = Place( 7, "Bathroom", 1200, 100, False, True, 1, False, True, "Bathroom" )
default Place8 = Place( 8, "Linda Room", 1200, 100, False, True, 1, False, True, "Linda Room" )
default Place9 = Place( 9, "Ashley Room", 1200, 100, False, True, 1, False, True, "Ashley Room" )
default Place10 = Place( 10, "Living Room", 1200, 100, False, True, 1, False, True, "Living Room" )
default Place11 = Place( 11, "Secret House", 1230, 10, False, True, 1, False, True, "Secret House" )
default Place12 = Place( 12, "Grocery Store", 1047, 510, True, True, 1, False, True, "Grocery Store" )
default Place13 = Place( 13, "Forest", 750, 90, False, True, 1, False, True, "Forest" )
default Place14 = Place( 14, "Trees", 1200, 100, False, True, 1, False, True, "Trees" )
default Place15 = Place( 15, "Kitchen", 1200, 100, False, True, 1, False, True, "Kitchen" )
default Place16 = Place( 16, "Monica Room", 1200, 100, False, True, 1, False, True, "Monica Room" )
default Place17 = Place( 17, "Guild Gate", 710, 820, True, True, 1, False, True, "Guild Gate" )
default Place18 = Place( 18, "Milk Farm", 1020, 275, True, True, 0, False, False, "Milk Farm" )
default Place19 = Place( 19, "Bath House", 1020, 275, False, True, 0, False, True, "Bath House" )

label start:
    $ start_inventory_items()
    call deactive_quick
    jump age_check
return
