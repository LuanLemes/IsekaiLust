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
            

    def function_update_image():
        list_of_images_bool = [False, False, False, False, False]
        list_of_images_sufix = [" morning", " afternoon", " night", " dawn", " late_dawn"]


        if renpy.has_image(location.lower() + " morning" , exact=True):
            list_of_images_bool[0] = True
            # $ map_image = str("maps/" + location.lower() + ".webp")
            # "has afternoon"
        if renpy.has_image(location.lower() + " afternoon" , exact=True):
            list_of_images_bool[1] = True
            # "has afternoon"

        if renpy.has_image(location.lower() + " night", exact=True):
            list_of_images_bool[2] = True
            # "has night"

        if renpy.has_image(location.lower() + " dawn", exact = True):
            list_of_images_bool[3] = True
            # "has dawn"
        if renpy.has_image(location.lower() + " late_dawn", exact = True):
            list_of_images_bool[4] = True
            # "has dawn"
        image_found = False
        image_to_select = -1
        count = -1
        while image_found == False:
            count = count +1
            if list_of_images_bool[calendar.current_day_time - count] == True:
                image_to_select = calendar.current_day_time - count
                map_image = str("maps/" +location + list_of_images_sufix[image_to_select] + ".webp")
                image_found = True
        map_image = str(map_image.lower())
        return map_image