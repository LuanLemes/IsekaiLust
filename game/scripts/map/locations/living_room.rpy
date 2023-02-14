screen living_room():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", "Monica Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to mom bedroom hover.webp")
            idle ("overlays/living room to mom bedroom.webp")
            action Call("change_location_to", "Monica Room")

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", "Kitchen")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to kitchen hover.webp")
            idle ("overlays/living room to kitchen.webp")
            action Call("change_location_to", "Kitchen")

        imagebutton:
            focus_mask True
            xpos 0.0
            ypos 0.0
            hovered SetVariable("focus_location", "Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to secret room hover.webp")
            idle ("overlays/living room to secret room.webp")
            action Call("change_location_to", "Kitchen")

        imagebutton:
            focus_mask True
            xpos 0.0
            ypos 0.0
            hovered SetVariable("focus_location", "Leave")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to map hover.webp")
            idle ("overlays/living room to map.webp")
            action Call("change_location_to", "Home")

        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Hallway")
        text "Hallway" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

label living_room:
    if prologue_to_living_room == True:
        $ only_location = "Kitchen"
        $ only_location_message = ["I have to see Monica (She is on the Kitchen)"]
        $ prologue_to_living_room = False

label living_room_before_enter:

    return
