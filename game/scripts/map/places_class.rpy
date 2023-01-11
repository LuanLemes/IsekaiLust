init python:

    class Place(object):
        def __init__(self, ID, name, x, y, is_active, is_inside, map_to_show, can_foward_time, can_map):
            self.ID = ID
            self.is_active = is_active
            self.name = name
            self.x = x
            self.y = y
            self.is_inside = is_inside
            self.map_to_show = map_to_show
            self.can_foward_time = can_foward_time
            self.can_map = can_map
        @property
        def avatar(self):
            icon = "locations/" + self.name.lower() + ".png"
            return(icon)

    places = []
    t = 0
    while t < 50:
        t += 1
        places.append(Place(-1, "", 0, 0, False, False, 0, False, False))

    places[0] = Place( 0, "Home Garage",700, 500, True, True, 0, False, True)
    places[1] = Place( 1, "Home",950, 470, True, True, 1, False, True)
    places[2] = Place( 2, "Home Bedroom", 710, 820, True, True, 1, False, True)
    places[4] = Place( 4, "Map", 1200, 100, False, False, 0, True, False)
    places[5] = Place( 5, "Forest Wall", 1200, 100, False, True, 1, True, False)
    location_object = Place(-1, "", 0, 0, False, False, 0, False, False)
