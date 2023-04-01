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
        
            imagebutton:
                focus_mask True
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
        ash "Mooooom, this little imp is repeating me."
        lin "Moooom this little imp is repeating me."
        show breakfast 4
        mon "Girls girls, behave your selves."
        show breakfast 1
        ash "Ok mon."
        lin "Ok mon."
        scene
        call update_image
    return

label kitchen_before_enter:

    return

label kitchen_door:
    mc_thought "There is a month since this door broke, I better get the right tools to fix it."
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
            "so, are you going to show up on the flower fields today?"
            "Yes":
                show monica half talking2
                mon "I see, I will be waiting for you then."
            "No":
                show monica half talking2
                mon "Thats a pity....try to show up some other day then."
            "I dont Know":
                show monica half talking2
                mon "I see, if you decide to go, please try to find me, we can collect flowers together if you want to."
    else:
        menu:
            "How was your night?"
            "It was very good":
                show monica half talking2
                mon "Im glad to hear that."
            "It had nightmares":
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
                        "this part has not yet been developed yet."
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
            "Thats a beautifull song linda":
                pass
        show breakfast girls5
        lin "Thank you [player.name]."
        lin "I know right? I think that Im going to be an artist when I finish school."
        show breakfast girls6
        mon "Well, our little artist needs to be good and eat healthy food to keep being cute and funny."
        lin_shout "Thanks mooom!"
        show breakfast girls7
        mon "No need to scream my little Baby."
        lin "Ok ok, Waaaaaw this smells greeeeat Thaaaaaanks."
        show breakfast girls8
        mon "You are welcome dear."
        mon "And now."
        show breakfast girls9
        mon "To our big girl."
        ash "Thanks for the food mom."
        mon "Oh, its nothing dear, you have to keep eating in order to being shiny and beautiful."
        show breakfast girls10 
        mon "And also."
        show breakfast girls11
        mon "To my dear [mcmon], [player.name]."
        menu:
            "Thanks Monica":
                mc "Oh thaanks Mon it looks very good."
            "...":
                mon "How do we say?"
                mc "Thanks mon you are the best."
        mon "Its nothing sweet, always have in mind that you are also my big star, and you are also very important to me."
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
        mc_thought "I should talk to monica before leaving."
        return False
    return