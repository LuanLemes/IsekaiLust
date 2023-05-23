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

        imagebutton auto "overlays/bed_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            action Call("bed")
    use top_screen()
label bedroom_reload:
    if int(debbie.phase) > 0 and flowers_monica_level > 1 and flowers_sarah_level > 1 and lilith.phase == 0 and calendar.current_day_time == 3:
        mc_thought "I cant sleep with this noise on the roof."
        mc_thought "I think there are cats walking out there."
        mc_thought "I better go take a look."
    if calendar.current_week_day == 6 or calendar.current_week_day == 0:
        dev "The game weekend has not been created yet so the game is going to skip the weekend for now, (updates are coming.)"
        call sleep
        return
    return

label bedroom:
    if sleep_when_enter == True:
        $ sleep_when_enter = False
        call sleep
        return
    if linda_prologue == True:
        $ only_location = "Hallway"
        scene bedroom morning
        $ only_location_message = ["I should go see what Monica has to say.", "I really should go see my Monica downstairs", "Not time to go there yet"]
        $ ui_show_top_screen = False
        mc "I really should see what monica has to say."
        $ linda_prologue = False
        $ ui_show_top_screen = True
        window hide
    return

label bedroom_before_enter:
    return

label bedroom_exit_check:
    return True

label bed:
    if prologue == True:
        mc_thought "I shouldnt go to sleep now, I have more important things to do."
        return
    menu:
        "teste da cena":
            show lilith roff23
            "oh yeah"
            $scene1.completion_check()
        "Sleep":

            jump sleep
        "Take a Nap":
            jump take_a_nap
    return

label sleep:
    if first_sleep == True:
        $ first_sleep = False
        $ ui_show_foward_time = True
    call day_next
    scene black with dissolve
    if sleeping_phrase == True:
        mc "That was a really good night sleep."
        $ sleeping_phrase == True

    if renpy.get_screen("say"):
        pass
    else:
        call change_location_to("Bedroom")
    call check_character_updates
    call wake_up
    return

label wake_up:
    return

label take_a_nap:
    if calendar.current_day_time != 4:
        mc "Oh man, that was a good nap."
    else: 
        "Oh...I slept all night."
    call time_next
    return

label check_character_updates:
    return

label wake_naked_1:
    $ wake_naked_1 = True
    $ can_buy_teddy = True
    show bedroom1 monica1 with dissolve
    mc_thought "(Hun, one more morning.)"
    mc "Oh Gosh!"
    mc "Im alive!!!!" with vpunch
    mc "I didnt die!!!"
    mc_thought "(I never thought I would be so happy only because I woke up.)"
    mc_thought "(Wait, what is this?)"
    show bedroom1 monica2 with dissolve
    mc_thought "(Is this....a note?)"
    mc_thought "Its writen: \"I cant stand to live anymore. Even with my beautiful gigantic and enormous cock, that can make any girl, even a SUCCUBUS VERY HAPPY. I give up. My last wish is to be burried with an open coffin and using no underwear so all the girls may know the best part of me. [player.name].\""  
    mc_thought "What the fuck did I just read?!?"
    show bedroom1 monica3
    mon_shout "Good morning!!!!"  with hpunch
    mc "What the fuck?!?"
    mon "You wont believe who was at the door asking for you this morning."
    mc "Monica."
    show bedroom1 monica4
    mon "It was Deb and she said..."
    mc "Monica I was just about to..."
    show bedroom1 monica8
    mon "Oh my..."
    mc "Get dressed."
    mon "Oh..."
    mon "My..."
    mc "..."
    show bedroom1 monica5 
    mon "Im s-sorry!" with vpunch
    mon "I didnt know you were in such a b-b-big."
    mon "Private moment!"
    show bedroom1 monica6
    mon "Im s-sorry!" with vpunch
    menu:
        mon "Oh this is so embarassing..."
        "You didnt do it on purporse":
            pass
        "Its fine dont worry":
            pass
        "Im the one who sould be embarassed":
            pass
    show bedroom1 monica9
    mon "Im used to living with Ashley and Linda so..."
    mon "Well I didnt pay any attention to it when you got here."
    mon "I would never look at my [mcmon] naked on purpose."
    mon "Im your [monmc] and I respect you very much."
    show bedroom1 monica10
    mon "Im so sorry!" with vpunch
    mc_thought "(Now I know why Linda talks that way.)"
    mc "Its alright."
    mon "I will always knock before entering,"
    show bedroom1 monica6
    mon "Does that sound ok with you?"
    menu:
        "No need to do that":
            mc "Its your house after all."
    show bedroom1 monica9
    mon "If you are ok with it."
    show bedroom1 monica6
    mon "But I think I will knock."
    mc_thought "(Damn if she doesnt stop shaking that ass I will get hard.)"
    mc_thought "(I need to get her out of here soon.)"
    show bedroom1 monica10
    mon "Anyway, Debbie was here a while ago asking for you."
    mc "Debbie? Sarahs Daughter?"
    mon "Yes."
    mc_thought "Man, Im naked and she is right in front of me, I want to fuck her so badly."
    mon "She said the teddybear arrived, she said you would understand."
    mc "I understand, Thanks mom."
    mon "Oh sweet!"
    show bedroom1 monica11
    mon "You called me mom!"
    mc "..."
    show bedroom1 monica5 
    mon "I did it again?" with vpunch
    show bedroom1 monica6
    mon "I think I..."
    mon "I better leave."
    mon "Good morning [player.name]."
    show bedroom1 monica7 with dissolve
    mc_thought "*Laughs*"
    mc_thought "(Cmon... it was kind of funny.)"
    mc_thought "(Well, I often fantasize of seeing Monica naked and not the other way around.)"
    mc_thought "(At least she saw my cock on a good day.)"
    mc_thought "(Oh come on its Monica Im talking about, she probably didnt even noticed my cock there.)"
    ash "Good morning Mom."
    mon "Good COCK my darling."
    ash "What did you just say?"
    mon "Oh. g-good LOCK of this door here."
    ash "O..kay."
    mc_thought "(Or maybe she did noticed it, he he.)"
    $ sleeping_phrase = False
    $ debbie.phase = 2
    call sleep_from_where
    return
