screen grocery_store():
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
            hovered SetVariable("focus_location", "Village")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Forest Wall")
        text "Village" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

label grocery_store:
    menu:
        "Talk to Sally":
            call talk_to_sally
        "Do Nothing":
            jump reload_location
    window hide
    return

label talk_to_sally:
    show image_to_show
    $ ui_show_foward_time = False
    $ ui_show_time =  False
    $ ui_show_money = False
    $ ui_show_maps = True
    $ ui_show_location = True
    $ ui_can_change_map = False
    $ ui_can_inventory = False
    call screen grocery_store_screen
    hide screen grocery_store_screen
    $ ui_can_inventory = True
    $ ui_show_foward_time = True
    $ ui_show_time =  True
    $ ui_show_money = True
    $ ui_show_maps = True
    $ ui_show_location = True
    $ ui_can_change_map = True
    $ ui_can_inventory = True

    jump grocery_store
    return
