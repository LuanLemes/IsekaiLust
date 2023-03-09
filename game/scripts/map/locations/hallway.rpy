screen hallway():
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
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/hallway to bathroom hover.webp")
            idle ("overlays/hallway to bathroom.webp")
            action Call("change_location_to", "Bathroom")

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", " Ashley Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/hallway to big sister bathroom hover.webp")
            idle ("overlays/hallway to big sister bathroom.webp")
            action Call("change_location_to", "Ashley Room")

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", " Linda Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/hallway to little sister bedroom hover.webp")
            idle ("overlays/hallway to little sister bedroom.webp")
            action Call("change_location_to", "Linda Room")

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", "Your Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/hallway to your room hover.webp")
            idle ("overlays/hallway to your room.webp")
            action Call("change_location_to", "Bedroom")

        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 46)
            idle im.Scale("gui/hover.png", 340, 46)
            hovered SetVariable("focus_location", "Living Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Living Room")
        text "Living Room" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"
    use top_screen()


label hallway:
    if big_sister_prologue == True:
        $ big_sister_prologue = False
        $ only_location = "Living Room"
        $ only_location_message = ["I have to see Monica (She is on the Kitchen)"]
        $ prologue_to_living_room = True
        jump ashley_prologue
        window hide

label hallway_before_enter:
    return
