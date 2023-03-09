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
    use top_screen()
    
label flower_camp:
    if flower_camp_first == True:
        call flower_camp_first
        return
    menu:
        "Colect flowers":
            call collect_flowers
        "Colect herbs":
            "collect herbs"
        "Explore the Field":
            "explore field"
    return

label flower_camp_check:  
    return

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
    return


    label flower_camp_first:
        # monica appears
        scene flower camp morning
        show monica half overall talking
        with dissolve
        mon "Oh hi [player.name], Im so glad you came."
        menu:
            "Anything for the one who saved me":
                mc "Of course, I would do anything for the one who saved me."
                show monica half overall talking2
                with dissolve
                mon "Oh dont talk like that, I only did what any one else would´ve done."
                mc "Well, thanks even so."
            "Dont be like that":
                mc "Dont be like that, I only did what you asked me to."
                show monica half overall talking2
                with dissolve
                mon "Im glad even so."
                mc "haha"
        mc "Back to the subject, So this is the flower field where you work han? got to say, thats much bigger than I expected."
        mon "Yes, Its here, here we have all kind of plants herbs and even some rare flowers."
        mc "Thats wonderfull, but... why did you called me for?"
        show monica half overall talking3
        with dissolve
        mon "Oh Dear [player.name]. I Know Your dream is to become an adventurer and I wont take that from you. But I wanted you to have some way of earning money."
        mon "So Im going to teach you how to identify and collect flowers and earn money with it."
        mc "Collect flowers?"
        mon "Yes, I mean...If thats ok with you of course."
        mc_thought "Man...What I really want is to be an adventurer, and also Im THE aphrodite champion!...But It would be nice to have some money for a change..."
        mc_thought "Also...I cant take the guild entrance exam without any money so...."
        mc "Yes, yes of course Its ok with me, please teach me how to do it."
        show monica half overall talking
        mon "Im so glad you agreed, It will be a nice experience teaching to my [mcmon]."
        mc "Im glad you like it, so.... how do we start?"
        show linda half happy:
                pos (-472, 166) zoom 0.93 
        with dissolve
        lin "[player.name] you are here!!!"
        show monica half overall left
        with dissolve
        mon "Linda, what are you doing here?" 
        lin "I was looking for Debbie, but...I seem to find her anywhere."
        mon "Linda what did I tell you about the Flower Fields?"
        show linda half avoiding:
                pos (-472, 166) zoom 0.93 
        with dissolve
        lin "\"That it is too dangerous\" moooom."
        mon "Then I think you should be going home little girl."
        show linda half sad
        with dissolve
        lin "But I Want to find Debbie, and she said she likes to play in the fields then I thought...."
        mon "..Linda, Im friend with Debbies Mons, And I know she wouldnt let Debbie play here in the fields."
        lin "I know that."
        show linda half sad right
        with dissolve
        lin "But moooooom, I want to collect flowers too."
        mon "Go home now, we will talk about this later."
        lin "Ok mon...."
        hide linda with dissolve
        mc "..."
        show monica half overall talking with dissolve
        mon "Sorry about that, Im a mom after all.... "
        mc "No problem at all."
        show monica half overall talking2 with dissolve
        mon "Where Was I again?"
        mc "You were saying where we would start."
        show monica half overall talking3 with dissolve
        mon "Yes yes.....We start by exploring the field and looking for flowers, let me take a look..."
        hide monica with dissolve
        mc_thought "I think I should go..."
        menu:
            "Explore the field":
                pass
            "Look for monica":
                pass
        show monica flower with dissolve
        pause 1.5
        mc_thought "(She just stood there for a time, It was like that flower was very important to her in a way I just couldn´t comprehend.)"
        mc_thought "(Never noticed that before but....damn she is hot..her body is just beautifull....Look at the flower all you want monica, while im going to look at you)"
        mc_thought "(I think I need a better angle.)"
        mc_thought "(Even her boobs, were they always that big?)"
        show monica flower2 with dissolve
        mon "Dont you want to take a closer look?"
        mc "Heh what?"
        mon "Dont you want to look at the flower?"
        mc "Ahh the flower, yes, yes I want."
        mon "Came on then."
        show monica flower3 with dissolve
        mc "Ok..."
        show monica flower3 with dissolve
        mc_thought "I think Im going slowsly So I can enjoy the view a little more."
        show monica flower4 with dissolve
        mon "This flower is here since she was a little seed, the earth and the rain helped this flower to grown until now."
        show monica flower5 with dissolve
        mon "And now, we are taking it away from its home for our own good and survival."
        show monica flower6 with dissolve
        mon "Im sorry little one..."
        mc_thought "How can someone be so pure and so hot? Damn."
        menu:
            "Its ok":
                mc "Its ok Monica, the earth has plenty more."
            "Say Nothing":
                mc "...."
        show flower camp morning
        show monica half overall talking with dissolve
        mon "Im sorry, sometimes Im too sentimental, but, thats how you find and collect flowers, now try to find some flowers and see how you go."
        call collect_flowers
        show monica half overall talking2 with dissolve
        mon "Very good [player.name], never thought it would be so fun to do that with you."
        mon "If you have any doubts, Im here every morning so we can collect flowers together if you want to."
        mc "Alright.."
        mon "Now you can {color=#FFAA00}sell the flowers on the grocery store {/color}, they usually pay for flowers, thats the easy way."
        $ flowers_cap_first = False
        jump flower_camp
        return