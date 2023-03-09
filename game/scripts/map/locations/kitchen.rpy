screen kitchen():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))
        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Living Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Living Room")
        text "Living Room" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"
        
        if monica_prologue == True:
            imagebutton auto "overlays/monica_kitchen_%s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("monica_prologue")
        
        imagebutton auto "overlays/kitchen_door_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", " Back Door")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("kitchen_door")
    use top_screen()
    

label kitchen:
    return
    # if monica_prologue == True:
        # $ monica_prologue = False
        # call monica_prologue

label kitchen_before_enter:

    return

label kitchen_door:
    mc_thought "There is a month since this door broke, I better get the right tools to fix it."