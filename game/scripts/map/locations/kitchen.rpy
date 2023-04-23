screen kitchen():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        
        if monica_prologue == True:

            imagebutton auto "overlays/monica_kitchen_%s.webp":
                focus_mask True
                xpos image_button_offset
                ypos image_button_offset
                action Call("monica_prologue")
        
            imagebutton:
                focus_mask True
                xpos image_button_offset
                ypos image_button_offset
                hover "breakfast 1.webp"
                idle "breakfast 1.webp"
                action NullAction()
        
        imagebutton auto "overlays/kitchen_door_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", " Back Door")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("kitchen_door")

        if calendar.current_day_time == 0 and calendar.current_day > 1 and breakfasted == False:
            imagebutton auto "overlays/monica_kitchen_%s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("monica_kitchen_morning")
            
            imagebutton auto "overlays/girls_kitchen_%s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("girls_kitchen_morning")
    # sarah and monica
        if calendar.current_week_day != 6 and calendar.current_week_day != 0 and calendar.current_day_time == 2 and monica_sarah_invited == True:
            imagebutton auto "overlays/monica sarah kitchen %s.webp":
                focus_mask True
                xpos image_button_offset
                ypos image_button_offset
                action Call("sarah_monica_kitchen")
                #  check if show water cups
            if monica_sarah_water == True:
                imagebutton:
                    idle ("monica sarah friends/kitchen cops overlay.webp")
                    hover ("monica sarah friends/kitchen cops overlay.webp")
                    focus_mask True
                    xpos image_button_offset
                    ypos image_button_offset
                    action NullAction()
    imagebutton:
        xpos 0.5
        ypos 0.95
        xanchor 0.5
        hover im.Scale("gui/idle.png", 340, 47)
        idle im.Scale("gui/hover.png", 340, 47)
        hovered SetVariable("focus_location", "Living Room")
        unhovered SetVariable("focus_location", location_object.name)
        action Call("change_location_to", "Living Room")
    text "Living Room" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

            

    use top_screen()
    

label kitchen:
    if kitchen_first == True:
        show monica_kitchen_idle
        $ kitchen_first = False
        show breakfast 2
        lin_shout "Breakfast! BreakFast! BreakFast!"
        ash "Could you please stop that?"
        show breakfast 3
        lin "Could you please stop that?"
        show breakfast 4
        ash "Mooooom, this little imp is copying me."
        lin "Moooom this little imp is copying me."
        show breakfast 4
        mon "Girls girls, behave your selves."
        show breakfast 1
        ash "Ok mom."
        lin "Ok mom."
        scene
        call update_image
    return

label kitchen_before_enter:

    return

label kitchen_door:
    mc_thought "It has been a month since this door broke, I better get the right tools to fix it."
    return

label monica_kitchen_morning:
    if monica_morning_kitchen == True:
        mc_thought "I just talked to her."
        return
    $ monica_morning_kitchen = True
    show monica half talking
    mon "Oh, good morning [player.name]."
    mon "So good to see you are awake already."
    if renpy.random.randint(1,10) > 5:
        menu: 
            "So, are you going to show up on the Flower Fields today?"
            "Yes":
                show monica half talking2
                mon "I see, I will be waiting for you then."
            "No":
                show monica half talking2
                mon "Thats a pity....try to show up some other day then."
            "I dont know":
                show monica half talking2
                mon "I see, if you decide to go, please try to find me, we can collect flowers together if you want."
    else:
        menu:
            "How was your night?"
            "It was very good":
                show monica half talking2
                mon "Im glad to hear that."
            "I had nightmares":
                show monica half talking2
                mon "Oh my [mcmon] had nightmares, thats so bad."
                mon "You know you can call me anytime if you need help forgeting nightmares right?"
            "I had a dream with you":
                show monica half talking2
                mon "Is that so? How was it?"
                menu: 
                    "I dont remember":
                        show monica half talking3
                        mon "Thats a pity."
                    "Tell her the dream (courage > 7)":
                        show monica half talking3
                        "This part has not yet been developed yet."
                        pass
    hide monica
    return

    label girls_kitchen_morning:
        show breakfast girls1
        lin "Hey [mclin] eat with us, It will be fun, right Sis?"
        ash "I dont want him to.."
        mon_shout "..Ashley! be a good girl with your [mcash]!"
        ash "But Moom."
        mon "Ashley, dont make me go there little girl."
        show breakfast girls2
        ash "Ok, fine!"
        ash "Sit if you want to."
        show breakfast girls3
        lin "Breakfast Breakfast."
        show breakfast girls4
        lin "Breakfast with [player.name]."
        show breakfast girls3
        lin "Eat eat we will."
        menu:
            "You are so funny":
                pass
            "Thats a beautiful song linda":
                pass
        show breakfast girls5
        lin "Thank you [player.name]."
        lin "I know right? I think that Im going to be an artist when I finish school."
        show breakfast girls6
        mon "Well, our little artist needs to be good and eat healthy food to keep being cute and funny."
        lin_shout "Thanks mooom!"
        show breakfast girls7
        mon "No need to scream my little baby."
        lin "Ok ok, Waaaaaw this smells greeeeat Thaaaaaanks."
        show breakfast girls8
        mon "You are welcome dear."
        mon "And now."
        show breakfast girls9
        mon "To our big girl."
        ash "Thanks for the food mom."
        mon "Oh, its nothing dear, you have to keep eating in order to stay shiny and beautiful."
        show breakfast girls10 
        mon "And also."
        show breakfast girls11
        mon "To my dear [mcmon], [player.name]."
        menu:
            "Thanks Monica":
                mc "Oh thaanks Mon it looks very good."
            "...":
                mon "What do we say?"
                mc "Thanks mon you are the best."
        mon "Its nothing sweetie, always remember that you are also my big star, and you are very important to me."
        lin "Very important to us!!!, right sis?"
        ash "..."
        lin "Sis?"
        ash "Whatever."
        lin "Siiiiiiiiiis."
        ash "Let me eat in peace please."
        $ breakfasted = True
        scene
    return

label kitchen_on_exit:
    if monica_prologue == True:
        mc_thought "(I should talk to Monica before leaving.)"
        return False
    return

label sarah_monica_kitchen:
    if monica_sarah_water == True:
        show kitchen cops overlay
        show monica sarah kitchen idle
    if monica_looked:
        mc_thought "Im a little ashamed, better not get near Monica right now."
        return
        hide kitchen cops overlay
        hide monica sarah kitchen idle
    if talked_to_girls:
        mc_thought "I just talked to them."
        return
        hide kitchen cops overlay
        hide monica sarah kitchen idle
    show monica sarah kitchen idle
    mc_thought "(Man, they are still talking.)"
    mc_thought "(I dont think I could talk that much even in one entire week.)"
    menu:
        "They are probably thirsty."
        "Offer them a drink":
            show monica_sarah kitchen3
            mon "No way, you got to be kidding me!"
            sar "Im telling you!!!"
            mc "Hey girls, want something to drink?"
        "Leave them be":
            hide monica
            return
    show monica_sarah kitchen5
    sar "Oh Please yes, something cold."
    mon "For me too dear please."
    mc "Right away!"
    show monica_sarah kitchen6 with dissolve
    mc "Lets see, what do we have here..."
    menu:
        "Water":
            mc_thought "I think this time I will go with water."
        "Beer (Requires Beer - in development)" if 1> 2:
            return
        "Wine(Requires Wine - in development)" if 1 > 2:
            return
    show monica_sarah kitchen4 with dissolve
    mc_thought "And they are still talking."
    show kitchen cups with dissolve
    mc "Here you go."
    show monica_sarah kitchen5
    sar "You are so cute."
    mon "Yes he is, he is my dear [mcmon]."
    sar "Dont you want to stay with us?"
    menu:
        "I dont want to interrupt a \'girls night\'.":
            mc "No, I dont want to interrupt a \'girls night\'."
            mc_thought "I think I will sit at the table and enjoy the view for a while."
    hide kitchen cups
    show monica_sarah kitchen7
    mc_thought "Thats it, thats all I needed a nice view of a nice ass in some tight short while I chill."
    mon "So, last year we were thinking about having a little birthday."
    mc_thought "...And they are still talking."
    mc_thought "Damn, how can a girl have an ass like that?"
    mc_thought "Is like.. its just too big, too perfect."
    show monica_sarah kitchen8
    mc_thought "I want to slap that ass so badly?"
    sar "Ha ha ha ha ha, OMG you didnt."
    show monica_sarah kitchen9
    sar "Wait, is there a fly on this glass?"
    mon "Is there?"
    mc_thought "No, there isnt a fly on the glass I checked it."
    mc_thought "But if there were a day that a fly landed on that ass I would kill it myself."
    mc_thought "What a big slap I would give, I can only imagine."
    show monica_sarah kitchen8
    mc_thought "I dont know what to think, I guess I will just stare at that ass and thats it."
    mc_thought "Monica you sure know how to find some cute best friends."
    show monica_sarah kitchen10
    mc_thought "Or at least the best asses."
    mc_thought "Wait..oh nooo not again!!!"
    mc_thought "Why does she always have to look?"
    show monica_sarah kitchen11
    mc_thought "Yes, she saw me no doubt about that."
    sar "Monica, are you alright?"
    mon "Me?"
    sar "Yes, you are acting strange all of sudden."
    mon "Oh, Im super okay."
    sar "Are you?"
    show monica_sarah kitchen12
    mon "I am"
    mc_thought "Im not going to stay and spoil the fun."
    mc_thought "Better to leave, I was thinking about {color=#FFAA00}masturbating in the bathroom{/color}
     anyway."
    $ monica_looked = True
    $ monica_sarah_water = True
    $ talked_to_girls = True
    hide monica_sarah
    return



