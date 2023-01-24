init python:

    class Place(object):
        def __init__(self, ID, name, x, y, is_active, is_inside, map_to_show, can_foward_time, can_map, show_name):
            self.ID = ID
            self.is_active = is_active
            self.name = name
            self.x = x
            self.y = y
            self.is_inside = is_inside
            self.map_to_show = map_to_show
            self.can_foward_time = can_foward_time
            self.can_map = can_map
            self.name = show_name
        @property
        def avatar(self):
            icon = "locations/" + self.name.lower() + ".png"
            return(icon)

    places = []
    t = 0
    while t < 500:
        t += 1
        places.append(Place(-1, "", 0, 0, False, False, 0, False, False, ""))

    places[0] = Place( 0, "Selling Point",700, 500, True, True, 0, False, True, "Selling Point" )
    places[1] = Place( 1, "Home",910, 410, True, True, 1, False, True, "Home")
    places[2] = Place( 2, "Bedroom", 710, 820, False, True, 1, True, True, "Bedroom" )
    places[4] = Place( 4, "Flower Camp", 950, 219, True, True, 1, True, True, "Flower Camp")
    places[5] = Place( 5, "Forest Wall", 1200, 100, False, False, 1, True, True, "Forest Wall" )
    places[6] = Place( 6, "Hallway", 1200, 100, False, True, 1, False, True, "Hallway" )
    places[7] = Place( 7, "Bathroom", 1200, 100, False, True, 1, False, True, "Bathroom" )
    places[8] = Place( 8, "Linda Room", 1200, 100, False, True, 1, False, True, "Linda Room" )
    places[9] = Place( 9, "Ashley Room", 1200, 100, False, True, 1, False, True, "Ashley Room" )
    places[10] = Place( 10, "Living Room", 1200, 100, False, True, 1, False, True, "Living Room" )
    places[11] = Place( 11, "Secret House", 1230, 10, False, True, 1, False, True, "Secret House" )
    places[12] = Place( 12, "Grocery Store", 1047, 510, True, True, 1, False, True, "Grocery Store" )
    places[13] = Place( 13, "Forest", 750, 90, True, True, 1, False, True, "Forest" )
    places[14] = Place( 14, "Trees", 1200, 100, False, True, 1, False, True, "Trees" )
    places[15] = Place( 15, "Kitchen", 1200, 100, False, True, 1, False, True, "Church" )
    places[16] = Place( 16, "Monica Room", 1200, 100, False, True, 1, False, True, "Monica Room" )
    places[17] = Place( 17, "Guild Gate", 710, 820, True, True, 1, False, True, "Guild Gate" )


    location_object = Place(-1, "", 0, 0, False, False, 0, False, False, "")
