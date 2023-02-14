image image_to_show = im.Scale("maps/store test.png", 1920, 1080)
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

default player = Player("Almir", 0, 100)
default player_inventory = Inventoryx([])
default collected_items = Inventoryx([])

label start:
    $ start_inventory_items()
    call deactive_quick
    jump age_check
return
