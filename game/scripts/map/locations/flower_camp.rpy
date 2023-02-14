screen flower_camp():

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

label flower_camp:
    menu:
        "Colect flowers":
            call collect_flowers
        "Colect herbs":
            "collect herbs"
        "Explore the Field":
            "explore field"
    # jump flower_camp
    window hide
    return

label flower_camp_check:
        if flowers_cap_first == True:
            $ enter_label_event = "flower_camp_first"

label collect_flowers:
    mc "Well then, lets collect some flowers!"
    default string_to_talk = ""
    $ random_strings = ["happy", "new", "year"]
    python:
        str_pre = ["", "", "", "", "", "", ""]
        str_item = ["", "", "", "", "", "", ""]
        str_rarity = ["", "", "", "", "", "", ""]

        collected_items.clear_all()
        flowers_found = 0
        random_number = 200
        while flowers_found < max_flowers_can_find:
            random_number = renpy.random.randint(1,100)
            if random_number <= 30  and renpy.random.randint(1,100)<70:
                random_number = renpy.random.randint(1,100)
            random_number = check_rarity(random_number)
            # mc ("[random_number]")
            for item in all_items:
                if item.type == "Flower":
                    if random_number == item.rarity:
                        if renpy.random.randint(1,10) <= 5:
                            collected_items.add_item(item.id, 1)
                            flowers_found += 1
                            break
            number_of_single_items_found = len(collected_items.items)
            str_items_found = ""
            str_items_found = "Good, I found "
            counter = 0
            string_counter = 1
            for item in collected_items.items:
                if string_counter == number_of_single_items_found:
                    str_items_found = str(str_items_found + "and " + str(item.quantity) + " "  + rarity_list[item.get_item().rarity] + " " + item.get_item().name + ".")
                    str_pre[counter] = str("and " + str(item.quantity) + " ")
                    str_rarity[counter] = str(str(rarity_list[item.get_item().rarity]))
                    str_item[counter] = str(" " + item.get_item().name + ".")

                elif counter + 1 == (number_of_single_items_found - 1):
                    str_items_found = str(str_items_found + str(item.quantity) + " " + rarity_list[item.get_item().rarity]  + " " + item.get_item().name + " ")
                    str_pre[counter] = (str(item.quantity) + " ")
                    str_rarity[counter] = str(rarity_list[item.get_item().rarity])
                    str_item[counter] = str(" " + item.get_item().name + " ")
                else:
                    str_items_found = str(str_items_found + str(item.quantity) + " " + rarity_list[item.get_item().rarity]  + " " + item.get_item().name + ", ")
                    str_pre[counter] = str(str(item.quantity) + " ")
                    str_rarity[counter] = str(rarity_list[item.get_item().rarity])
                    str_item[counter] = str(" " + item.get_item().name + ", ")
                string_counter += 1
                counter += 1
        str_pre_0 = str_pre[0]
        str_pre_1 = str_pre[1]
        str_pre_2 = str_pre[2]
        str_pre_3 = str_pre[3]
        str_pre_4 = str_pre[4]
        str_pre_5 = str_pre[5]
        str_pre_6 = str_pre[6]
        str_rarity_0 = str_rarity[0]
        str_rarity_1 = str_rarity[1]
        str_rarity_2 = str_rarity[2]
        str_rarity_3 = str_rarity[3]
        str_rarity_4 = str_rarity[4]
        str_rarity_5 = str_rarity[5]
        str_rarity_6 = str_rarity[6]
        str_item_0 = str_item[0]
        str_item_1 = str_item[1]
        str_item_2 = str_item[2]
        str_item_3 = str_item[3]
        str_item_4 = str_item[4]
        str_item_5 = str_item[5]
        str_item_6 = str_item[6]
        collected_items.transfer_all(player_inventory)
        renpy.say(mc, "Look I found [str_pre_0]{color=#FFAA00}[str_rarity_0]{/color}[str_item_0][str_pre_1]{color=#FFAA00}[str_rarity_1]{/color}[str_item_1][str_pre_2]{color=#FFAA00}[str_rarity_2]{/color}[str_item_2][str_pre_3]{color=#FFAA00}[str_rarity_3]{/color}[str_item_3][str_pre_4]{color=#FFAA00}[str_rarity_4]{/color}[str_item_4][str_pre_5]{color=#FFAA00}[str_rarity_5]{/color}[str_item_5][str_pre_6]{color=#FFAA00}[str_rarity_6]{/color}[str_item_6]")
        # player_inventory.list_items()
    jump flower_camp
    

















    return
