default ui_show_top_screen = True
default ui_show_foward_time = False
default ui_show_time =  True
default ui_show_money = True
default ui_show_location = True
default ui_show_maps = True
default ui_can_change_map = False
default ui_show_inventory = True
default ui_can_inventory = True
default ui_can_book = True
default ui_show_book = True
default creation_tools = True

screen top_screen:
    default this_current_week_day = ""
    zorder 1
    add Solid("0000")
    if ui_show_top_screen == True:
        frame:
            background  Solid("0000")
            xpos 0 ypos 0
            xminimum 1920
            yminimum 75
            if ui_show_money:
                frame:
                    xsize 370
                    ysize 49
                    xalign 0.93
                    background Solid("0000")
                    add "button_hover" :
                        xsize 370
                        ysize 49
                    text " Money:[player.money]" xalign 0.5 yalign 0 yoffset 5 color "ffffff"
                    # text "test"
            if ui_show_maps:
                hbox:
                    xoffset 5
                    yoffset 3
                    spacing 10
                    if location_object.can_map == True and ui_can_change_map:
                        if location_object.is_inside == False:
                            imagebutton:
                                xoffset 9.5
                                hover im.Scale("icons/bed_hover.png",80,80)
                                idle im.Scale("icons/bed.png",80,80)
                                action Call("change_location_to", "Bedroom")
                        else:
                            imagebutton:
                                hover im.Scale("icons/map_hover.png", 90, 90)
                                idle im.Scale("icons/map.png", 90, 90)
                                action Call("change_location_to", "Forest Wall")
                    else:
                        if location_object.is_inside == False:
                            imagebutton:
                                xoffset 9.5
                                hover im.Scale("icons/bed disabled.png",80,80)
                                idle im.Scale("icons/bed disabled.png",80,80)
                                action NullAction()
                        else:
                            imagebutton:
                                hover im.Scale("icons/map disabled.png", 90, 90)
                                idle im.Scale("icons/map disabled.png", 90, 90)
                                action NullAction()
            if ui_show_location:
                vbox:
                    xalign 0.063 yoffset -7
                    frame:
                        background Solid("0000")
                        xsize 370
                        ysize 49
                        add "button_hover" :
                            xsize 370
                            ysize 49
                            # xalign 0.055
                            # yalign 0.057
                        text " [focus_location]" xalign 0.05 yoffset 4 color "ffffff"

                    frame:
                        background Solid("0000")
                        xsize 370
                        ysize 149
                        add "button_hover" :
                            xsize 270
                            ysize 49
                        # background im.Scale("gui/hover.png", 250, 45)
                        $ this_current_week_day = calendar.week_days[calendar.current_week_day]
                        # $ this_current_week_day = calendar.current_week_day
                        text "  [this_current_week_day]" yoffset 5 color "ffffff"

            if ui_show_time:
                vbox:
                    xalign 0.5
                    spacing 10
                    hbox:
                        spacing 1

                        vbox:
                            spacing 3
                            image "morning"

                            if calendar.current_day_time == 0:
                                image im.Scale("icons/ball_white.png", 30, 30) xoffset 7
                            else:
                                image im.Scale("icons/ball_blue.png", 30, 30) xoffset 7


                        vbox:
                            spacing 3
                            image "afternoon"

                            if calendar.current_day_time <=1:
                                image im.Scale("icons/ball_white.png", 30, 30) xoffset 7
                            else:
                                image im.Scale("icons/ball_blue.png", 30, 30) xoffset 7
                        vbox:
                            spacing 3
                            image "evening"
                            if calendar.current_day_time <= 2:
                                image im.Scale("icons/ball_white.png", 30, 30) xoffset 7
                            else:
                                image im.Scale("icons/ball_blue.png", 30, 30) xoffset 7
                        vbox:
                            spacing 4
                            image "dawn"
                            if calendar.current_day_time <= 3:
                                image im.Scale("icons/ball_white.png", 30, 30) xoffset 7
                            else:
                                image im.Scale("icons/ball_blue.png", 30, 30) xoffset 7
        frame:
            background Solid("0000")
            xalign 0.403
            yalign 0.01
            if location_object.can_foward_time and ui_show_foward_time:
                imagebutton:
                    xoffset 37
                    yoffset -18
                    hover im.Scale("icons/next_hover.png", 100,90)
                    idle im.Scale("icons/next.png", 100,90)
                    # action Call("time_next")
                    action [Return ("reload"), Call("time_next")]
                    # [ SetVariable("saved_game", True), Load("saved_game"), SetVariable("saved_game", False), Jump("start") ]

        frame:
            background Solid("0000")
            xalign 0.981
            yalign 0.02
            if ui_show_inventory == True:
                imagebutton:
                    xoffset 37
                    yoffset -18
                    hover im.Scale("icons/inventory_icon_hover.webp", 90,80)
                    idle im.Scale("icons/inventory_icon_idle.webp", 90,80)
                    action [Show("inventory"), MouseMove(170, 100, 0)]
                    # action Call("inventory")
        frame:
            background Solid("0000")
            xalign 0.981
            yalign 0.105
            if ui_show_inventory == True:
                imagebutton:
                    xoffset 37
                    yoffset -18
                    hover im.Scale("icons/book_hover.webp", 80,80)
                    idle im.Scale("icons/book.webp", 80,80)
                    action [Show("book")]
                    # action Call("inventory")
