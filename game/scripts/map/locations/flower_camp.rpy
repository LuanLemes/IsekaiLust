screen flower_camp():
    default this_screen_image = map_image
    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080
        background (str(this_screen_image))
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
        #  sarah on flower fields
        if calendar.current_day_time < 2 and calendar.current_week_day != 0 and calendar.current_week_day != 6 and calendar.current_week_day != 4 and calendar.current_day > 8:
            imagebutton auto "overlays/sarah flower field %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("sarah_flower_field")
        # monica flower fields
        if calendar.current_day_time < 2 and calendar.current_week_day != 0 and calendar.current_week_day != 6 and calendar.current_day > 0:
            if calendar.current_week_day != 3 and calendar.current_day >= 12:
                imagebutton auto "overlays/monica flower field %s.webp":
                    focus_mask True
                    xpos -5
                    ypos -5
                    action Call("monica_flower_field")
            if calendar.current_week_day and calendar.current_day < 12:
                imagebutton auto "overlays/monica flower field %s.webp":
                    focus_mask True
                    xpos -5
                    ypos -5
                    action Call("monica_flower_field")
        #  unkonown girl flower fields sex scenes
        if calendar.current_day_time == 3 and calendar.current_week_day == 4:
            if first_unknown_girl == True:
                imagebutton auto "overlays/unknown first %s.webp":
                    focus_mask True
                    xpos -5
                    ypos -5
                    action Call("sex_scene_with_unknown_girl")
            else:
                imagebutton auto "overlays/unknown girl %s.webp":
                    focus_mask True
                    xpos -5
                    ypos -5
                    action Call("sex_scene_with_unknown_girl_after")
    use top_screen()

label flower_camp_reload:
    if calendar.current_day_time < 2 and calendar.current_week_day != 0 and calendar.current_week_day != 6 and calendar.current_week_day != 4 and calendar.current_day > 8 and calendar.current_day_time == 0 and sarah_field_first == True:
        $ sarah_field_first = False
        call sarah_field_first
        return
    return

label flower_camp:
    if calendar.current_week_day == 4 and first_unknown_girl:
        mc_thought "(I dont know why....but I feel like going to the flower camp at dawn (Blue Moon) today.)"
        mc_thought "(Its just a feeling though.)"
    if flower_camp_first == True:
        $ flower_camp_first = False
        jump flower_camp_first
        return
    return

label monica_flower_field:
    show monica half overall talking
    mon "Hey, you are back."
    menu:
        "Collect flowers together":
            call collect_flowers_with_monica
        "Talk":
            call talk_with_monica
    return

label collect_flowers_with_monica:
    $ flowers_collected_monica += 1
    $ flowers_collected += 1
    call check_monica_flower_level
    call collect_flowers
    call time_next
    scene
    call update_image
    return

label collect_flowers_with_sarah:
    $ flowers_collected_sarah += 1
    $ flowers_collected += 1
    call check_sarah_flower_level
    call collect_flowers
    call time_next
    scene
    call update_image
    return

label talk_with_monica:
    show monica half overall talking
    menu:
        "Why did you choose to work with flowers?":
            show monica half overall talking2
            mon "Gardening is a great hobby for people like me, people who love plants."
            mc "Is that so?"
            show monica half overall talking3
            mon "Yes it is. It allows me to surround myself with the beauty of nature."
            mon "And experience the joy of watching plants grow and flourish."
            mc "I see you really like it."
            show monica half overall talking
            mon "And the best part is taking care of them you see, I love to water and sometimes..even sing for them."
            mc "Haha."
            show monica half overall talking2
            mon "What is it? Did I say something odd?"
            mc "Thats not it...its just...I found it kind of cute hearing you talk about plants with so much excitement in your eyes."
            show monica half overall shy
            mon "Stop it dear...as if you could find an old woman like me to be cute."
            menu:
                "Its not like that.":
                    mc "Its not like that."
                "I think I find you more cute than you realize.":
                    mc "I think I find you more cute than you realize."
            mon "Its ok, I know you are only saying that to try to make me feel better."
            mon "I know you probably see me as an old aunt or something like that."
            show monica half overall shy2
            mon "And its ok..."
            mon "I understand..."
        "When did you start garderning?":
            show monica half overall talking2
            mon "Well....I started garderning since I was seven."
            mc "That early?"
            show monica half overall talking3
            mon "Yes, I mean...it wasnt like a job or anything. You see, at that time my parents had a little garden in the back of our home."
            mon "So in the beginning for me it was all childs play."
            show monica half overall talking
            mon "It was all to make my family proud and have fun."
            show monica half overall talking2
            mon "It was my mom who taught me how to sing for plants"
            show monica half overall talking3
            mon "She said they hear us, and they deserve to be loved."
        "What is your favorite plant?":
            show monica half overall talking3
            mon "My favorite plant?"
            mc "Yes, which one is it?"
            show monica half overall talking2
            mon "It is a very rare plant that...I have only seen in pictures."
            mc "In pictures?"
            show monica half overall talking
            mon "Yeah, it is so rare that they call it an Acid-Leaf-Z"
            # acid leaf z the flower that make people get naked
            mon "I dreamed about finding one ever since I was a child.."
            mc "Well, If I ever see one, I will tell you ok?"
            show monica half overall talking2
            mon "Oh dear, please do so, I would be so happy if I ever saw one."
        "Nothing for now":
            mc "Ah, its nothing, thank you for your time"
            mon "Ah, ok then."
            hide monica
            return
    call talk_with_monica
    return

label sarah_field_first:
    # show sarah half normal
    scene sarah first4 with dissolve
    mc "Anyway, one more day working at the flower field."
    show sarah first5 with dissolve
    sar "Hello Hello!!!"
    sar "So you are here too!!!"
    mc "Who is that?"
    show sarah first3 with dissolve
    camera:
            pos (-1046, -909) yzoom 1.0 zoom 2.16 
    mc_thought "(Are you fucking kidding me?)"
    mc_thought "(She is way too close and way too hot.)"
    call camera_reset
    sar "Are you...are you ok?"
    show sarah first6 with dissolve
    mc_thought "(Shit, I forgot to answer...)"
    mc_thought "(Damn she is so cute, What did she ask again?)"
    menu: 
        "I am":
            mc "I am."
            pass
        "I havent seen you":
            mc "I am but I havent seen you since that day at the store."
            pass
    show sarah first3 with dissolve
    sar "Well I havent shown up too much lately because the store had way too much work recently."
    show sarah first6 with dissolve
    mc "I imagine, I mean, running your own business seems like a lot of work."
    show sarah first3 with dissolve
    sar "It really is a lot of work, but things should be easier now that Debbie is helping out."
    show sarah first6 with dissolve
    mc_thought "(She has such a nice ass.)"
    show sarah first3 with dissolve
    sar "[player.name]?"
    show sarah first6 with dissolve
    mc_thought "(I...cant keep this conversation going..not like this anyway.)"
    mc_thought "(I need to get up or my eyes will betray me again and I will look like an idiot.)"
    menu:
        "Get up":
            show sarah first7 with dissolve
            mc "Man my legs are killing me."
            mc_thought "(Its better this way.)"
    show sarah first9 with dissolve
    sar "Dont tell me the squatting really made your legs hurt."
    show sarah first7 with dissolve
    mc "The pain is real."
    show sarah first9 with dissolve
    sar "Well, I think you will get used to it, with time your legs will get stronger."
    sar "I mean, look at my legs, they got really strong because of this."
    show sarah first7 with dissolve
    mc "They are really beautiful."
    show sarah first9 with dissolve
    sar "Wait, I said strong, not beautiful."
    show sarah first7 with dissolve
    mc "Oh, I....."
    show sarah first9 with dissolve
    sar "Haha, just kidding silly, I will take that as a compliment."
    show sarah first7 with dissolve
    mc "It was a compliment."
    show sarah first9 with dissolve
    sar "Your legs will also grow strong with time" 
    sar "And I dont know maybe it will, help you in your guild test."
    show sarah first7 with dissolve
    mc "Yeah, maybe, I guess."
    mc "Wait, how did you know that I wanted to take the guild test?"
    show sarah first9 with dissolve
    sar "Me and monica are best friends and we tell each other EVERYTHING."
    show sarah first7 with dissolve
    mc "I see..."
    show sarah first9 with dissolve
    sar "Dont be like that, girls like to talk, silly, its just normal."
    sar "Anyway, see you in the fields."
    show sarah first1 with dissolve
    mc "The flower camp, just got a little more interesting."
    $ sarah.book_phrase = "Spend time with Sarah at the fields."
    scene
    call time_next
    call update_image
    return

label sarah_flower_field:
    show sarah half normal
    menu:
        "Collect flowers together":
            call collect_flowers_with_sarah
        "Talk":
            dev "In development."
            hide sarah
            return
            call talk_with_sarah
    return

label sarah_flowers_level_1:
    show sarah first0 with dissolve
    mc "Today Sarah taught me a lot of things about plants."
    return

label sarah_flowers_level_2:
    if sarah_flowers_level_2_first == False:
        $ sarah_flowers_level_2_first = True
        $ sarah.book_phrase = "Thats all for this update."
        show sarah level21
        sar "Ok [player.name], just one more flower and thats it."
        show sarah level21
        sar "This one, this one is so cute, it will be easy peasy."
        show sarah level22
        mc "The yellow one?"
        show sarah level23
        sar "Yes, I will show you how its done."
        mc "..."
        sar "grrrr"
        mc "Sarah are you ok?"
        show sarah level25
        sar "Yes, yes im ok."
        mc "..."
        show sarah level24
        sar "Its just that..."
        mc "..."
        sar_shout "It wont move, not even a little!!!" with vpunch
        sar_shout "AHHHHHHH!"
        show sarah level26
        menu:
            "What are you doing? help me out?"
            "how?":
                mc "How would I do that?"
            "What do you want?":
                mc "What do you want me to do?"
        sar "I dont know, think of something...pull me from behind."
        show sarah level27
        mc "Ok."
        mc "I mean...What?"
        show sarah level28
        sar "Just go ahead and help me pull this flower out ok?"
        mc "Ok then."
        show sarah level29
        mc_thought "(Aphrodite...I dont know how this situation happened but I give you my thanks.)"
        mc "Like this?"
        sar "Yeah, it could work I think."
        sar "But you have to be more firm."
        mc "Like this?"
        show sarah level210 with vpunch
        sar_shout "Ahhh!" with vpunch
        mc_thought "(Maybe it was too much?)"
        mc "Im sorry."
        sar "Not a problem, pull!"
        mc "Ok!"
        sar "Ahhh Its not working!"
        mc "What do we do?"
        sar "I dont know Im already giving it my all, if only we could use a sword or something."
        mc "We dont have one here."
        sar "Then try grabbing some other place, I dont know."
        show sarah level211 with vpunch
        sar "Hey!"
        mc "What?"
        sar "Nothing..just...pull ok?"
        mc "Ok, on three."
        sar "Ok (taking a deep breath)"
        menu:
            "Count until tree":
                mc "One, two....THREE."
                show sarah level213 with vpunch
                mc_shout "Pull!" with vpunch
            "TREE!":
                show sarah level213 with vpunch
                mc_shout "Three!!!!!" with vpunch
                sar_shout "Ahhhhh!!" with vpunch
                sar_shout "Why did you do that?"
                mc "What?"
                sar "You went straight to three."
                mc "I dont know, it felt right in the moment."
                sar "..."
                sar "Anyway..."
        sar "I think it moved a little."
        # show sarah level213 with vpunch
        mc_thought "(Man I can feel her entire ass pressing against me, this is way too good.)"
        mc "Your idea is working sarah, we will get it in no time."
        sar "I dont think I can take it much longer..."
        sar "This position is..."
        sar "Its way too much..."
        show sarah level212 
        menu:
            "Stop worrying":
                mc "Stop worrying, we will get it out, Im here to help you."
            "Its ok its ok":
                mc "Its ok, its ok, forget about the position"
        sar "Ok lets do it again then."
        menu:
            "TREE!":
                show sarah level214 with vpunch
                mc_shout "Three!!!!!" with vpunch
                sar_shout "Ahhhhh!!" with vpunch
                mc "What is it now?"
                sar_shout "Gosh, count to three before you pull me that hard ok?"
                mc "Ok ok."
                mc "Did it move?"
        sar "Yes, I felt it move again."
        mc_thought "(Man, the feeling in this position, its almost like I own her.)"
        mc "Very good then."
        sar "I think....I think I want to stop."
        mc "Are you giving up?"
        sar "Thats not it..."
        mc "What is it then?"
        sar "You see..."
        mc "What?"
        sar "Its just that this position..."
        mc "This position what?"
        mc "The only thing I see here is two people working on the flower field, thats it."
        sar "Ok ok, lets do it."
        menu:
            "Count one and then go three.":
                mc "One..."
                sar "..."
            "TREE!":
                pass
        show sarah level215 with vpunch
        mc_shout "Three!!!!!" with vpunch
        sar_shout "Ahhhhh!!" with vpunch
        mc_thought "(Man...Im going to slowly start moving my hands up, and If she doesnt say anything Im going to touch her boobs just to \"help\" her.)"
        mc "Sarah?"
        sar "hm."
        mc "Everything ok?"
        sar "Um hum."
        mc "Ok then, one more time ok?"
        sar "..."
        mc "Sarah?"
        sar_wisper "What?"
        mc_thought "(She is like...whispering? thats cute.)"
        menu:
            "Count till three and smash her!!!":
                pass
        mc "One.."
        sar "..."
        mc "Two..."
        sar "..."
        mc_thought "(I never thought this would be so much fun, I can even feel her breath in this position, I think she is a little anxious.)"
        mc "And..........."
        sar "..."
        mc_thought "(I know the thrill is killing her.)"
        show sarah level216 with vpunch
        mc_shout "Three!!!!!" with vpunch
        mc_shout "HAAAAAAAAA!!"
        sar_shout "HAAAAAA!!!!"
        scene black with dissolve
        $ renpy.notify("You can press \'H\' anytime to hide or show the dialogue box.")
        sar "We did it we did it!!!"
        $ renpy.notify("You can press \'H\' anytime to hide or show the dialogue box.")
        show sarah level217
        sar "Such a beautiful flower."
        sar "A rare one, just as I thought."
        show sarah level218 
        mc "...ahn..."
        sar "What beautiful colors."
        mc_thought "(What happened?)"
        show sarah level219 
        $ renpy.notify("You can press \'H\' anytime to hide or show the dialogue box.")
        sar "Its so shiny."
        show sarah level220 
        mc_thought "(I see now, I think we fell and she landed on top of me.)"
        mc_thought "(Such a good place for her to land.)"
        show sarah level221
        sar "The smell is so good too."
        mc_thought "(She is so happy with that flower that she doesnt even realize where she is sitting.)"
        mc_thought "(Such a beautiful ass.)"
        mc_thought "(I think Im in heaven.)"
        show sarah level222
        camera:
                pos (-94, -729) zoom 1.74 
        mc_thought "(Oh no..)"
        mc_thought "(I think Im...I think Im getting a boner.)"

        show sarah level223
        sar "I dont think I will sell this one... I mean...its such a beautiful flower."
        mc_thought "(Im definitely getting a boner.)"
        mc_thought "(I cant hold on....the feeling of her ass sitting on me is just so good.)"
        call camera_reset
        mc_thought "(Has she noticed?)"
        mc_thought "(No...I dont think so...)"
        sar "I think im going to put it in my house."
        camera:
            pos (-94, -729) zoom 1.74 
        sar "I will put it in a place where I can see it when I wake up."
        mc_thought "(But if this situation goes on much longer.)"
        mc_thought "(She will notice I am sure of it.)"
        call camera_reset
        menu:
            "If I say something she might get up and I dont want that."
            "say nothing":
                pass
            "say nothing":
                pass
            "say nothing":
                pass
        camera:
            pos (-94, -729) zoom 1.74 
        mc_thought "(Even so I dont think I will say anything.)"
        mc_thought "(Thats it...whatever happens happens.)"
        sar "Maybe take some pictures of this flower too."
        sar "And also I would like to...."
        show sarah level224 with vpunch
        mc_thought "(Thats it....there is no way shes not feeling it now.)"
        mc_thought "(I can literally feel my dick touching her ass.)"
        # call camera_reset
        mc_thought "(But...she is not saying anything.)"
        mc_thought "(She stopped talking, she literally can feel my dick right now.)"
        mc_thought "(This would be so good if this wasnt so bad.)"
        show sarah level225
        window hide
        pause(2.0)
        camera:
                pos (-869, -1036) zoom 2.28 
        mc_thought "(Such a nice feeling, I would like this moment to last forever.)"
        call camera_reset
        mc_thought "(Well...maybe she just stopped talking, it doesnt mean she is feeling my dick or anything.)"
        show sarah level226
        mc_thought "(She looked!.)" with vpunch
        mc_thought "(Shit, she is not even looking at it, she is looking right into my eyes.)"
        mc_thought "(Why wont she stop looking?)"
        mc_thought "(Such... such beautiful eyes, she is so sexy)"
        camera:
            pos (-869, -1036) zoom 2.28 
        with vpunch
        mc_thought "(Its growing again!!!)" with vpunch
        call camera_reset
        mc_thought "(I think....I should say something.)"
        mc_thought "(What do I say what do I say what do I say?)"
        menu:
            "Say something right now!"
            "Banana":
                pass
            "Ass":
                pass
            "Milk":
                pass
            "Cum":
                pass
        mc_thought "(What did I just say?!?!?!)" with vpunch
        mc_thought "(Im an idiot, thats it, I accept everything thats coming... its over for me)"
        show sarah level225
        mc_thought "(She...just turns again?)"
        show sarah level227
        mc_thought "(I see....she is getting up.)"
        show sarah level229 with dissolve
        mc "Sarah...."
        sar "...."
        show sarah level228 with dissolve
        mc_thought "(Is she trying to look at my dick without me knowing?)"
        sar "I think...."
        show sarah level229 with dissolve
        sar "I think its time for me to go...."
        sar "See you [player.name]."
        scene black with dissolve
        return
    elif sarah_flowers_level_2_first == True:
        $ phrase = renpy.random.randint(1,7)
        $ phrase = renpy.random.randint(1,7)
        if phrase == 1:
            show sarah level210
        if phrase == 2:
            show sarah level211
        if phrase == 3:
            show sarah first6
        if phrase == 4:
            show sarah first0
        if phrase == 5:
            show sarah level217
        if phrase == 6:
            show sarah first5
        if phrase == 7:
            show sarah first9
        mc "Today I collected flowers with Sarah."
        return

label collect_flowers:
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
            str_items_found = "Good, we found "
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
        renpy.say(mc, "We found [str_pre_0]{color=#FFAA00}[str_rarity_0]{/color}[str_item_0][str_pre_1]{color=#FFAA00}[str_rarity_1]{/color}[str_item_1][str_pre_2]{color=#FFAA00}[str_rarity_2]{/color}[str_item_2][str_pre_3]{color=#FFAA00}[str_rarity_3]{/color}[str_item_3][str_pre_4]{color=#FFAA00}[str_rarity_4]{/color}[str_item_4][str_pre_5]{color=#FFAA00}[str_rarity_5]{/color}[str_item_5][str_pre_6]{color=#FFAA00}[str_rarity_6]{/color}[str_item_6]")
        # player_inventory.list_items()
    return


    label flower_camp_first:
        # monica appears
        scene flower camp morning
        show monica half overall talking
        with dissolve
        menu:
            mon "Oh hi [player.name], Im so glad you came."
            "Anything for the one who saved me":
                mc "Of course, I would do anything for the one who saved me."
                show monica half overall talking2
                with dissolve
                mon "Oh dont talk like that, I only did what anyone else wouldve done."
                mc "Well, still thanks."
            "Dont be like that":
                mc "Dont be like that, I only did what you asked me to do."
                show monica half overall talking2
                with dissolve
                mon "Im glad even so."
                mc "haha"
        mc "Back to the subject, So this is the Flower Field where you work? got to say, its much bigger than I expected."
        mon "Yes, Its here, here we have all kinds of plants herbs and even some rare flowers."
        mc "Thats wonderful, but... why did you call me?"
        show monica half overall talking3
        with dissolve
        mon "Oh Dear [player.name]. I know Your dream is to become an adventurer and I wont take that from you. But I wanted you to have some way of earning money."
        mon "So Im going to teach you how to identify and collect flowers so that you can earn money from it."
        mc "Collect flowers?"
        mon "Yes, I mean...If thats ok with you of course."
        mc_thought "(Man...What I really want is to be an adventurer, and also Im THE Aphrodite Champion!...but it would be nice to have some money for a change...)"
        mc_thought "(Also...I cant take the guild entrance exam without any money so....)"
        mc "Yes, yes of course its ok with me, please teach me how to do it."
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
        lin "I was looking for Debbie, but...I cant seem to find her anywhere."
        mon "Linda what did I tell you about the Flower Fields?"
        show linda half avoiding:
                pos (-472, 166) zoom 0.93 
        with dissolve
        lin "\"That it is too dangerous\" moooom."
        mon "I think you should be going home little girl."
        show linda half sad
        with dissolve
        lin "But I Want to find Debbie, and she said she likes to play in the fields then I thought...."
        mon "..Linda, Im friends with Debbies mom, And I know she wouldnt let Debbie play here in the fields."
        lin "I know that."
        show linda half sad right
        with dissolve
        lin "But moooooom, I want to collect flowers too."
        mon "Go home now, we will talk about this later."
        lin "Ok mom...."
        hide linda with dissolve
        mc "..."
        show monica half overall talking with dissolve
        mon "Sorry about that, Im a mom after all.... "
        mc "No problem at all."
        show monica half overall talking2 with dissolve
        mon "Where was I again?"
        mc "You were saying where we should start."
        show monica half overall talking3 with dissolve
        mon "Yes yes.....we start by exploring the field and looking for flowers, let me take a look..."
        hide monica with dissolve
        menu:
            mc_thought "(I think I should go...)"
            "Explore the field":
                pass
            "Look for Monica":
                pass
        show monica flower with dissolve
        pause 1.5
        mc_thought "(She just stood there for awhile, It was like that flower was so important to her.. in a way I just couldnt comprehend.)"
        mc_thought "(Never noticed this before but....damn she is so hot..her body is just beautiful....look at the flower all you want Monica, while I look and admire you)"
        mc_thought "(I think I need a better angle.)"
        mc_thought "(Even her boobs, were they always that big?)"
        show monica flower2 with dissolve
        mon "Dont you want to take a closer look?"
        mc "Heh what?"
        mon "Dont you want to look at the flower?"
        mc "Ahh the flower, yes, yes I do."
        mon "Came on then."
        show monica flower3 with dissolve
        mc "Ok..."
        show monica flower3 with dissolve
        mc_thought "(I think Im going to walk slowly so I can enjoy the view a little more.)"
        show monica flower4 with dissolve
        mon "This flower has been here since it was a little seed, the earth and the rain helped this flower grow up until now.."
        show monica flower5 with dissolve
        mon "And now, we are taking it away from its home for our own good and survival."
        show monica flower6 with dissolve
        mon "Im sorry little one..."
        menu:
            mc_thought "(How can someone be so pure and so hot? Damn.)"
            "Its ok":
                mc "Its ok Monica, the earth has plenty more."
            "Say nothing":
                mc "...."
        show flower camp morning
        show monica half overall talking with dissolve
        mon "Im sorry, sometimes Im overly sentimental, but, thats how you find and collect flowers, now try to find some flowers and see how you do."
        call collect_flowers
        show monica half overall talking2 with dissolve
        mon "Very good [player.name], never thought it would be so much fun to do this with you."
        mon "If you have any doubts, Im here every morning so we can collect flowers together if you want."
        mc "Alright.."
        mon "Now you can {color=#FFAA00}sell the flowers at the grocery store {/color}, they usually pay for flowers, thats the easy way."
        $ flowers_cap_first = False
        hide monica with dissolve
        call time_next
        call update_image
        return

label check_sarah_flower_level:
    # update collect var
    # check if it is at max level already
    if len(sarah_flower_levels) == flowers_sarah_level:
        $ level_up_expression =  ""
        $ level_up_expression =  str("sarah_flowers_level_") + str(flowers_sarah_level)
        call expression level_up_expression
        return
    #  if it is 0 flowers till the next level - if it is it means there was an update and this save game hasnt the ne level yet, so the game will update it
    if flowers_to_next_level_sarah == 0:
        $ flowers_to_next_level_sarah = sarah_flower_levels[flowers_sarah_level]
    $ flowers_to_next_level_sarah -= 1
    # em caso de evoluir de level 
    if flowers_to_next_level_sarah == 0:
        # "level uped"
        $ flowers_sarah_level += 1
        if len(sarah_flower_levels) == flowers_sarah_level:
            pass
            # "returned because there arent more levels"
        if len(sarah_flower_levels) > flowers_sarah_level:
            # "added the next level objective"
            $ flowers_to_next_level_sarah = sarah_flower_levels[flowers_sarah_level]
    $ level_up_expression =  ""
    $ level_up_expression =  str("sarah_flowers_level_") + str(flowers_sarah_level)
    call expression level_up_expression
    return

label check_monica_flower_level:
    # update collect var
    # check if it is at max level already
    if len(monica_flower_levels) == flowers_monica_level:
        $ level_up_expression =  ""
        $ level_up_expression =  str("monica_flowers_level_") + str(flowers_monica_level)
        call expression level_up_expression
        return
    #  if it is 0 flowers till the next level - if it is it means there was an update and this save game hasnt the ne level yet, so the game will update it
    if flowers_to_next_level_monica == 0:
        $ flowers_to_next_level_monica = monica_flower_levels[flowers_monica_level]
    $ flowers_to_next_level_monica -= 1
    # em caso de evoluir de level 
    if flowers_to_next_level_monica == 0:
        # "level uped"
        $ flowers_monica_level += 1
        if len(monica_flower_levels) == flowers_monica_level:
            pass
            # "returned because there arent more levels"
        if len(monica_flower_levels) > flowers_monica_level:
            # "added the next level objective"
            $ flowers_to_next_level_monica = monica_flower_levels[flowers_monica_level]
    $ level_up_expression =  ""
    $ level_up_expression =  str("monica_flowers_level_") + str(flowers_monica_level)
    call expression level_up_expression
    return

label monica_flowers_level_1:
    show monica flower2
    mc "There are days that Monica is just too cute."
    return

label monica_flowers_level_2:
    if monica_flowers_level_2 == True:
        scene monica flower6
        mc "Today was a very good day to collect flowers."


    if monica_flowers_level_2 == False:
        $ monica.tips = "Thats all for this update."
        mc_thought "(Monica is so good to me, today im going to give her a surprise.)"
        show monica red flower with dissolve
        mc "Hey Monica, look at what I found."
        mon "What is it dear?"
        show monica red flower2 with dissolve
        mon "!!!!!!!!!!!" with vpunch
        mc "Beautiful isnt it?"
        mon "Where did you find that?"
        mc "I found it in the forest, so...what do you think?"
        


        show monica red flower2 with dissolve:
            blur 2.0
        mon "Throw it away now!" with vpunch

        show monica red flower2 with dissolve:
            blur 4.0
        mc "But why? Its such a beautiful flo...."
        show monica red flower3 with dissolve:
            blur 8.0
        mon "Omg [player.name] are you ok?"
        mc "Oh, Im oka....."
        scene black with Dissolve(3.0)
        mon "[player.name]!!!"
        mc "..."

        show monica red flower5 with Dissolve(2.5)
        mon "Oh [player.name], you are such a good boy, such a good [mcmon]." 
        mon "Everything will be ok."
        show monica red flower5 with dissolve
        mon "He is so warm even though he is asleep."
        show monica red flower6 with dissolve
        mc "What... ha..happened?"
        show monica red flower7 with dissolve
        mon "[player.name], you are awake!"
        mc "Huh, The only thing I remember is that I wanted to give you a special flower as a gift and everything went black."
        mon "Oh [player.name], that flower had poisonous thorns, you can only pick it wearing gloves."
        mc "\"Poison\"? Am I going to die?"
        mon "No silly."
        mon "These flower are very rare and paralize whoever touches its poisonous thorns...temporarily"
        mon "But, everything will be ok, just wait a little, I will be here with you until you get better ok?"
        show monica red flower8
        mc_thought "(She is so kind as always.)"
        mc "Thank you Monica."
        mc "How long until the effect wears off?"
        mon "Hun...It depends the time may change from person to person."
        mc "..."
        mon "Lets see."
        show monica red flower9
        mon "Try moving your feet"
        menu:
            "Move your feet":
                pass
        mc "Did it move?"
        show monica red flower8
        mon "Yeah...hmm maybe."
        mon "Either way I will be here with you until you get better."
        mc "Thank you [monmc]."
        mon "You are so cute."
        show monica red flower9
        mon "Now, one more time!"
        mon "try moving it again!"
        show monica red flower10
        mc_thought "(WOW...I never had seen Monicas boobs so close before.)"
        mc_thought "(They are so beautiful.)"
        mc_thought "(Where are the powers Aphrodite promised me when I need them?.)"
        mon "[player.name]... are you trying?"
        show monica red flower8
        mc "Im sorry I got distracted a bit"
        mon "Ok, now...on \'3\'"
        show monica red flower9
        mc "Ok."
        mon "1 2 3...."
        show monica red flower12 with vpunch
        mon "MOVE!"
        show monica red flower13
        mc "Am I moving?"
        mc "Monica?"
        show monica red flower14
        mon_shout "Ahhhhhhh!!!!" with vpunch
        mc "What, what is it?"
        mc "What is happening? Did I move? Did something Happen?"
        mon_shout "Ahhhhh its huge!!!!" with vpunch
        mc "What? what is huge? I cant move my head, I cant see a thing!"
        show monica red flower15
        mon "Oh dear, Im sorry, I forgot you cant see, nor feel..."
        mon "I saw a very very big snake."
        mc "A snake?"
        mon "Yes, it a huge snake, the biggest I ever seen, but its ok now."
        mc "Monica, since I cant move."
        menu:
            "Shouldnt we be worried?":
                mon "No, not to worry, everything will be ok."
            "Shouldnt we call Sarah just in case so you two can help each other in case the snake decides to attack?":
                mon_shout "No I dont want my best friend to!!" with vpunch
                mc "...."
                mon "...I mean...I dont want my best friend to be in danger just because of me."
        mon "If the snake cames back again I will handle it myself."
        mc "You are very brave Monica, thank you."
        mon "No..Thank YOU."
        mc "..."
        show monica red flower16
        mon "Now, close your eyes dear, you need to rest."
        mc "Ok."
        mon "Dream about angels."
        mon "My {b}Big{/b} [player.name]."
        $ monica_flowers_level_2 = True
        $ herbology += 1
        notif "You gained 1 point of Herbology"
        $ max_flowers_can_find += 1
        notif "You can now collect more flowers at once."
        $ monica.book_phrase = "2"
        $ monica.phase = 2
        return
    return
    
label sex_scene_with_unknown_girl:
    stop music
    hide unknown first idle
    if first_unknown_girl:
        $ first_unknown_girl = False
        show unknown first idle
        play music "audio/nature sounds.ogg"
        mc_thought "(Wait...what is that?)"
        mc_thought "(Is that a person?)"
        menu:
            mc "...?"
            "Who is there?":
                mc "Hello? Whos there?"
            "Monica?":
                mc "Monica is that you?"
        play audio "audio/wolf howl.ogg"  
        mc_thought "(Nothing...)"
        mc_thought "(A howl?)"
        mc_thought "(I never been so confused.)"
        mc_shout "Hey you should get out of the field, there may be a wolf nearby!"
        show unknown girl idle with Dissolve (2.0)
        ung "Human human, good smell good smell."
        mc "What?"
        mc "Is she?"
        ung "GRRRR!."
        mc "The \"Wolf\"."
        mc_shout "No!"
        hide unknown
        show unknown_girl_running
        pause 0.50
        scene black
        play audio "audio/Punch.ogg"
        "..."
        mc "What happened?"
        ung "Hmmmm!"
        show unknown girl sex1 with dissolve
        mc_shout "WhaAAAAt?" with vpunch
        mc_thought "(Is she really?)"
        mc_thought "(NAKED? naked and on top of me.)"
        mc_thought "(I think im dreaming.)"
        show unknown girl sex2 with dissolve
        mc_thought "(Is she???!?)"
        mc_thought "(Going to do this??)"
        menu:
            mc_thought "(Man Im trembling. is it really going to?)"
            "Who are you?":
                pass
            "Why are you doing this?":
                pass
            "Aaahn...":
                pass
        mc_thought "(She doesnt answer...)"
        
        ung "Hmmmm!"
        mc_shout "HEY YOU, TALK WITH M....HAAAAAAAAAA!!!!"
        show unknown girl sex3 with dissolve
        play sound "audio/Single Moan 1.ogg"
        pause 1.0
        show unknown girl sex4 with dissolve
        ung "Ahhh!"
        mc_shout "HAAAAAAAAAA!!!!"
        mc_thought "(Omg, this is definitely NOT a dream.)"
        mc_thought "(This is happening, this is really happening isnt it?)"
        mc_thought "(Its like my dick is in heaven!)"
        mc_thought "(Man she is so warm and tight, Im not sure if I can handle it.)"
        stop sound
        play sound "audio/slow sex moan2.ogg" loop volume 5.1
        show unknown girl sex5 with dissolve
        mc_thought "(She started moving.)"
        mc "Ahhh its so good!"
        mc_thought "(She is doing it so smoothly, its like my dick is finally complete inside her pussy.)"
        mc_thought "(And her hair its so close to my face, and has such a nice smell.)"
        mc_thought "(I have never been in love, but I think this is it.)"
        menu:
            mc "Ahhh its so good."
            "Look at her":
                mc_thought "(I need to see her face.)"
                show unknown girl sex6 with dissolve
                mc_thought "(I know it could just be because she is sitting on my dick.)"
                mc_thought "(But I dont think I have ever seen a girl as beautiful as her before.)"
            "Just keep enjoying the view":
                mc_thought "(No, I really want to see my dick inside of her as she sits on it.)"
                mc_thought "(There is nothing more beautiful than that.)"
        menu:
            mc_thought "(I need to say something)"
            "You are beautiful":
                pass
            "You are cute":
                pass
            "You are hot!":
                pass
        mc_thought "(I think she is about to say something.)"
        mc_thought "(I feel it!)"
        stop sound
        play sound "audio/slow sex moan3.ogg" loop volume 5.1
        show unknown girl sex7 with dissolve
        mc_thought "(Can we do it in this position too?)"
        mc_shout "Ahhh your pussy is so good!"
        mc_thought "(She does things on command like a wild animal!)"
        mc_thought "(Damn she is hot...I dont think I can do it any longer in this position.)"
        mc_thought "(Wait...if I cum will she gets pregnant?)"
        menu:
            mc_thought "(I need to tell her.)"
            "Hey, be careful I think I am about to cum.":
                pass
        stop sound
        play sound "audio/sex sound fast 1.ogg" loop volume 5.0
        show unknown girl sex8 with dissolve
        mc_shout "Ahhh!"
        mc_thought "(What?!?!?!?)"
        mc_thought "(Its like she wants me to cum!)"
        mc "Hey didnt you hear me?"
        mc_thought "(I can see by her face she is close too.)"
        mc_thought "(Her pussy is so gooood!)"
        mc "Why dont you say anything?"
        ung "grrrr!"
        mc_thought "(Am I really going to cum that fast.)"
        menu:
            mc_thought "(Its my first time, I cant cum too fast.)"
            "Hold it":
                pass    
            "Hold it":
                pass    
            "Hold it":
                pass    
        mc_thought "(She is like an animal!)"
        mc_thought "(I try to endure it but she just keeps on going.)"
        mc_thought "(She is just too beautiful.)"
        mc_thought "(I dont know how much longer I can...)" with vpunch
        show unknown girl sex9 with dissolve
        mc_shout "I am!!!" with vpunch
        stop sound
        play sound "audio/cum sound 1.ogg" loop volume 5.2
        play audio "audio/girl orgasm 1.ogg" 
        show unknown girl sex10 with dissolve
        mc_shout "IM CUMMING!" with vpunch
        ung "AHHHHHH!" with vpunch
        mc_thought "(Im cumming and she isnt getting off me.)"
        mc_shout "Ahhhh!!!"
        stop sound
        play sound "audio/after cum non loop.ogg"
        show unknown girl sex11 with dissolve
        mc "...."
        mc_thought "(Its the best sensation on the world...)"
        mc_thought "(Im very tired....)"
        mc_thought "(Her pussy is full of cum.. my cum.)"
        mc_thought "(And at the same time I feel like I..)"
        mc_thought "(I just have to do it again!)"
        mc_thought "(She is also very tired.)"
        show unknown girl sex12 with dissolve
        mc_thought "(Well, she just took my virginity without even asking.)"
        menu:
            mc_thought "(So I dont need to ask either.)"
            "Fuck her from behind!":
                pass
        mc "Thats it."
        stop sound
        play sound "audio/Moan 1.ogg" loop
        show unknown girl sex13 with dissolve
        mc_thought "(I dont care who she is.)"
        mc_thought "(She started this so now she has to finish.)"
        menu:
            "You are my slut now!":
                pass
            "You are my bitch now!":
                pass
        show unknown girl sex14 with dissolve
        mc_thought "(She has such a beautiful body.)"
        mc_thought "(If I could I would fuck her like this every week.)"
        show unknown girl sex17 with dissolve
        mc "It seems like you are exhausted already."
        mc "Such a cute girl..."
        mc "Too bad, Im not exhausted."
        show unknown girl sex15 with dissolve
        mc "Im going to enjoy this moment all I want."
        mc "In every way I can."
        mc "Because its not every day that a girl comes looking for free sex."
        menu:
            "Isnt that right little wolf?":
                pass
            "Isnt that right big ass wolf?":
                pass
            "Isnt that right tight pussy wolf?":
                pass
        mc_thought "(Her moans are so beautiful.)"
        stop sound
        play sound "audio/Moan 2.ogg" loop
        show unknown girl sex16 with dissolve
        mc "Now show me what a wolf girl can do!"
        mc "Show me how much your pussy can take."
        mc "Im going to fuck you until you cant walk anymore."
        show unknown girl sex19 with dissolve
        mc_thought "(Man she is drooling all over herself.)"
        mc "You seem like you are about to faint."
        mc "But this is my day! so dont faint yet!"
        mc "You have to endure a little more!"
        mc_thought "(Ah...your body is just so beautiful.)"
        mc "Im going to cum!"
        menu:
            "Cum inside her pussy":
                stop sound
                play sound "audio/cum sound 1.ogg" loop volume 5.2
                play audio "audio/girl orgasm 1.ogg" 
                mc "You look so tired."
                show unknown girl sex20 with dissolve
                mc "Just relax while while your little pussy is being filled with my cum."
                mc "Can you feel your pussy getting filled?"
                ung "Yes."
                mc "Just like that, good girl."
            "Cum on her ass":
                stop sound
                play sound "audio/cum sound 1.ogg" loop volume 5.2
                mc_shout "Do as I tell you, face down and bring your ass up NOW!"
                ung "Yes."
                show unknown girl sex21 with dissolve
                mc "Good girl, good girl."
        stop sound
        mc "You are such a good girl."
        show unknown girl sex26 with dissolve
        mc "Man, look at this, you are such a mess."
        ung "Grrr."
        mc "Yes...thats a beautiful view, I would take a photo right now if I had a camera"
        show unknown girl sex22 with dissolve
        # remove image 22 later 
        mc "Seriously, you are dripping cum everywhere, Im kind of proud."
        mc "Hey, are you going to be ok?"
        ung "Grrrrrrrr!"
        play audio "audio/wolf howl.ogg"
        show unknown girl sex23 with dissolve
        mc "Another wolf?"
        ung "Agrrrr!"
        show unknown girl sex24 with dissolve
        mc_thought "(And just like that.)"
        show unknown girl sex25 with dissolve
        mc_thought "(The girl that took my virginity is gone.)"
        $ first_unknown_girl = False
        stop music
        play music "audio/Adolescence.ogg"
        call time_next
        return
    return

label sex_scene_with_unknown_girl_after:
    show unknown girl idle
    mc_thought "(She is there again, she hasnt seen me yet.)"
    mc_thought "(For some reason I think she comes here every week)"
    mc_thought "(Maybe I should go there again...you know...I need to know more of this world after all.)"
    menu:
        mc_thought "(should I go there?)"
        "Yes":
            mc_thought "(Well, I want what I want.)"
            mc "Hey there wolf girl!!!"
        "No":
            mc_thought "(I better stay away from her then.)"

            hide unknown
            return
    show unknown girl sex30
    mc_thought "She is looking!"
    show unknown girl sex29
    mc_thought "I think she is....waiting for me."
    menu:
        "Fuck her doggy style":
            call unknown_girl_doggy
            return
        "Let her go on top( in developtment)" if 1> 2:
            call unknown_girl_doggy_style
            return
    return

label unknown_girl_doggy:
    stop sound
    play sound "audio/Moan 1.ogg" loop
    show unknown girl sex13 with dissolve
    mc "Damn its nice to use your pussy."
    mc "You are more wet than last time."
    mc "Your ass is bigger too, are you going to the gym or something?"
    ung "GRRRR!"
    mc "\"Gr\" all you want im going deep in your pussy."
    show unknown girl sex14 with dissolve
    mc "Oh Im getting better at this."
    mc "It seems like you are managing better than the last time too right?"
    ung "Grrr!!"
    menu:
        mc ""
        "Maybe I should go a little harder on you.":
            pass
            mc "Maybe I should go a little harder on you."
            ung "Grrr!!"
        "Maybe I should go easy this time.":
            mc "I think I will go easy on you this time."
            ung "Hmmmg!!"
    mc "Such a cute girl."
    mc "With such a sweet little pussy."
    menu:
        "Fuck her more!":
            pass
        "Cum on her ass.":
            call unkown_girl_cum_ass
            return
        "Cum inside her pussy":
            call unkown_girl_cum_inside
            return
    mc "Since you like to be fucked so much."
    mc "Im going to fuck you like a little wolf every single week."
    show unknown girl sex17 with dissolve
    mc "It will be our little secret."
    mc "You will come here like a little obedient wolf and then I will fuck you."
    ung "Grrrrrr!!!"
    mc "Dont try to lie to me."
    mc "If you didnt like it you wouldnt come back here since the day we first met."
    menu:
        "You are my little wolf now":
            mc "You are my little wolf now."
        "You like to be fucked in a public field":
            mc "You like to be fucked in a public field."
    mc "Such nice tities you have, I think Im going to try sucking them sometime."
    ung "Grrrr!"
    menu:
        "Fuck her more!":
            pass
        "Cum on her ass.":
            call unkown_girl_cum_ass
            return
        "Cum inside her pussy":
            call unkown_girl_cum_inside
            return
    show unknown girl sex15 with dissolve
    mc "Damn I love this view."
    mc "Its like shes surrendered to me and only me."
    mc_thought "I dont know why but I really feel like I want to cum inside every girl I met."
    mc_thought "And she is not an exception."
    mc_thought "Is like as I fuck her..I begin to feel a huge urge to cum in her or cum on her."
    stop sound
    play sound "audio/Moan 2.ogg" loop
    show unknown girl sex16 with dissolve
    ung "Aaaaah!!"
    mc "I know you are tired little wolf, but I want you to remember this tomorrow."
    mc "So im going to fuck you some more."
    menu:
        "Fuck her more!":
            pass
        "Cum on her ass.":
            call unkown_girl_cum_ass
            return
        "Cum inside her pussy":
            call unkown_girl_cum_inside
            return
    show unknown girl sex19 with dissolve
    ung "Huuuun!!!"
    mc "Yes like that."
    mc "Man Im enjoying this!"
    ung "Haaaaa!!"
    mc "Do you want me to cum?"
    ung "Yeeeeeees!!!"
    mc "So you talk after all."
    menu:
        "Fuck her more!":
            pass
        "Cum on her ass.":
            call unkown_girl_cum_ass
            return
        "Cum inside her pussy":
            call unkown_girl_cum_inside
            return
    mc "I think you cant take more."
    ung "Grrrrr I can not Grrrrr."
    mc "You will even so."
    mc_thought "(Damn...I dont think even I can take it much longer now.)"
    mc_thought "Just now she was speaking.."
    mc "Who are...."
    ung "Grrr!"
    mc_thought "I want to talk but ...thats it, thats my limit. I need to cum"
    $ wolf_girl_fucked1 = True
    menu:
        "Cum on her ass.":
            call unkown_girl_cum_ass
            return
        "Cum inside her pussy":
            call unkown_girl_cum_inside
            return
    return

label unkown_girl_cum_inside:
    stop sound
    play sound "audio/cum sound 1.ogg" loop volume 5.2
    play audio "audio/girl orgasm 1.ogg" 
    mc "Now, bend over for me my little wolf"
    show unknown girl sex20 with dissolve
    mc "Feel my cum fill every inch of your pussy."
    ung "Grrrrr."
    mc "Be a good girl and obey!"
    ung "Hmm..."
    mc "Good girl."
    call unknown_girl_after_cum
    return

label unkown_girl_cum_ass:
    stop sound
    play sound "audio/cum sound 1.ogg" loop volume 5.2
    mc_shout "Do as I tell you, and bring your ass up NOW!"
    ung "Yes."
    show unknown girl sex21 with dissolve
    mc "Good girl, good girl."
    call unknown_girl_after_cum
    hide unknown with dissolve
    return

label unknown_girl_after_cum:
    show unknown girl sex28 with dissolve
    mc_thought "(So beautiful.)"
    mc "I never get tired of this view."
    play sound "audio/wolf howl.ogg"
    mc "And there she goes again."
    mc "Bye...again..."
    mc "Mysterious wolf girl."
    call time_next
    hide unknown with dissolve

    return

label unknown_girl_doggy_style:
    return

image unknown_girl_running:
    animation
    pause 0.10
    "SexUnknownGirl/unknown running1.webp"
    pause 0.10
    "SexUnknownGirl/unknown running2.webp"
    pause 0.10
    "SexUnknownGirl/unknown running3.webp"
    pause 0.10
    "SexUnknownGirl/unknown running4.webp"
    pause 0.10
    "SexUnknownGirl/unknown running5.webp"
    pause 0.10
return