default location = "Map"
$ exit_map = False
define status_function = "x"
define map_image = ""
# define location_object = Place()
label enter_map:
    call change_location_to("Forest Wall")
    return


label change_location_to(new_location):
    scene
    hide screen expression location
    $ location = new_location
    python:
        for place in places:
            if location == place.name:
                location_object = place
            # $location_object = place

    $ low_location = str(location.lower())
    $ screen_name = low_location.replace(" ", "_")
    call update_image
    call expression screen_name
    call focus_location_to(location)
    $ renpy.call_screen(screen_name)
    jump reload_location
    return

label update_image:
    $ list_of_images_bool = [False, False, False, False, False]
    $ list_of_images_sufix = ["", " afternoon", " night", " dawn", " late_dawn"]

    if renpy.has_image(location.lower(), exact=True):
        $ list_of_images_bool[0] = True
        $ map_image = str("maps/" + location.lower() + ".webp")
        # "has day"

    if renpy.has_image(location.lower() + " afternoon" , exact=True):
        $ list_of_images_bool[1] = True
        # "has afternoon"

    if renpy.has_image(location.lower() + " night", exact=True):
        $ list_of_images_bool[2] = True
        # "has night"

    if renpy.has_image(location.lower() + " dawn", exact = True):
        $ list_of_images_bool[3] = True
        # "has dawn"
    if renpy.has_image(location.lower() + " late_dawn", exact = True):
        $ list_of_images_bool[4] = True
        # "has dawn"

    $ image_found = False
    $ image_to_select = -1
    $ count = -1
    while image_found == False:
        $ count = count +1
        # "count is[count]"
        # "calendar [calendar.current_day_time]"
        if list_of_images_bool[calendar.current_day_time - count] == True:
            # "count is[count]"
            $ image_to_select = calendar.current_day_time - count
            $ map_image = str("maps/" +location + list_of_images_sufix[image_to_select] + ".webp")
            $ image_found = True
    show expression map_image

    return

label reload_location:
    call change_location_to(location)
    return

label focus_location_to(new_value):
    $ focus_location = new_value
