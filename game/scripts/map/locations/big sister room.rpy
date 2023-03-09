screen ashley_room():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))
        use top_screen()
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
    use top_screen()
    
label ashley_room:
    return

label ashley_room_check:
    if ashley_room_locked == True:
        $ not_enter_message = "(The door is locked...)"
        return False
