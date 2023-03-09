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
            self.show_name = show_name
            self.add_to_places()

        def add_to_places(self):
            is_on_list = False
            for item in places:
                if item.ID == self.ID:
                    is_on_list = True
            if is_on_list == False:
                places.append(self)


        @property
        def avatar(self):
            icon = "locations/" + self.name.lower() + ".png"
            return(icon)