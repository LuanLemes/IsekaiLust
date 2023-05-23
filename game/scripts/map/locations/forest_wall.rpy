screen forest_wall():
    use top_screen()
    $ show_subtitle = False
    text "Thats the map babe"

    frame:
        # xalign 0.0
        # yalign 0.0
        xpos 0.0
        ypos 0.0
        xsize 1920
        ysize 1080

        background (str(map_image))
        # background "maps/"+location +".webp"
        # background "maps/forest wall.webp"
        # background Solid("0000")
        # background "maps/forest wall/webp"

        for place in places:
            if place.is_active == True and place.map_to_show == 1:
                $ hover_name = place.avatar
                $ hover_name = hover_name.replace(".png", " hover.png")
                $ hover_name = hover_name.replace(" ", "_")
                $ idle_name = place.avatar
                $ idle_name = idle_name.replace(".png", " idle.png")
                $ idle_name = idle_name.replace(" ", "_")
                vbox:
                    xpos place.x
                    ypos place.y
                    imagebutton:
                        focus_mask True
                        hover im.Scale(hover_name, 100, 100)
                        hovered SetVariable("focus_location", place.name)
                        unhovered SetVariable("focus_location", location_object.name)
                        idle im.Scale(idle_name, 100, 100)
                        action Call("change_location_to", place.name)
    use top_screen()
    

label forest_wall:
    if flower_camp_first == True:
        $ only_location = "Flower Camp"
        $ only_location_message = ["(I should go help monica at the Flower Camps.)"]
        return
    if grocery_store_first == True:
        $ only_location = "Grocery Store"
        $ only_location_message = ["(Monica recomended the grocery store to sell these flowers.)"]
        return
    if calendar.current_day >= 1 and makoto_first == True and calendar.current_day_time <= 1:
        mc_thought "Today seems like a good day to go to the guild and see how to become a member."
        $ only_location = "Guild Gate"
        $ only_location_message = ["Today seems like a good day to go to the guild and see how to become a member."]
        return
    # if Place18.map_to_show == 1 and milk_farm_first == True:
    return

label forest_wall_reload:
    if Place18.map_to_show == 1 and milk_farm_first == True:
        if location_message == True:
            mc_thought "So, there is the location linda showed me."
            $ location_message = False
        $ only_location = "Milk Farm"
        $ only_location_message = ["I really think I should go to the milk farm."]
        return
    return
