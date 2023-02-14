screen bedroom():

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
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Hallway")
        text "Hallway" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

label bedroom:
    if linda_prologue:
        $ only_location = "Hallway"
        $ only_location_message = ["I should go see what Monica has to say.", "I really should go see my Monica downstairs", "Not time to go there yet"]
        $ linda_prologue = False
    return

label bedroom_before_enter:
    return

label bedroom_exit_check:
    "i dont know how i got here"
    "This is the exit check, you can´t leave this room, now get to work you bitch."
    return True
