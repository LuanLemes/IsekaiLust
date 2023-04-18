screen home():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", " Enter House")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/house to living room hover.webp")
            idle ("overlays/house to living room.webp")
            action Call("change_location_to", "Living Room")

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

            #   monica and sarah talking scene at fridays
        if calendar.current_day_time == 2 and calendar.current_week_day == 5 and monica_sarah_invited == False:
            imagebutton auto "overlays/sarah monica house %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("monica_sarah_talking_home")
    use top_screen()

label home_check:
    if calendar.current_day_time == 0:
        $ can_enter = False
        $ not_enter_message = "Now its morning and you cant go home."
    elif calendar.current_day_time >= -1:
        $ can_enter = False
        $ not_enter_message = "You you cant go home now."
    return can_enter



label home:
    window hide
    return

label monica_sarah_talking_home:
    show monica_sarah home1 with dissolve
    menu:
        mc_thought "Wow, the two of them here like this."
        "Say \'Hey\'":
            pass
        "Let them chat":
            hide monica_sarah
            return
    mc "Hey."
    show monica_sarah home5
    mon "Hi [player.name]."
    sar "Oh, Hey [player.name]."
    if monica_sarah_talking_first == True:
        show monica_sarah home7 with dissolve
        sar "Now, thats something strange."
        sar "Hmmmm."
        show monica_sarah home15
        mon "Now, whats so strange?"
        sar "I knew you lived with Monica but, I kind of, forgot you lived here."
        show monica_sarah home9
        mon "Ha ha ha, oh Sarah thats so you."
        show monica_sarah home8 
        sar "Im sorry, the last two months were kind of harsh"
        mon "Yeah, It was indeed."
        show monica_sarah home5
        mon "Anyway [player.name]..."
        show monica_sarah home5
    menu:
        mon "How are you this evening?"
        "Im fine thanks.":
            show monica_sarah home11
            mon "Oh dear thats good to hear."
        "Im very good thanks.":
            show monica_sarah home11
            mon "Good thing dear."
    if flowers_sarah_level <= 1 or flowers_monica_level <= 1:
        mc_thought "I think its better to leave, girls sometimes need these moments alone."
        mc "So, I feel like Im in the middle of a \'girl thing\' here, so Im going to leave."
        mc "Good night girls."
        show monica_sarah home5
        mon "Good night [player.name]."
        sar "Good night."
        hide monica_sarah
        return
            
    sar "Anyway."
    show monica_sarah home14
    mon "..."
    mc "..."
    show monica_sarah home15
    sar "We were just talking about you."
    mc "You..."
    mc "You were?"
    show monica_sarah home16
    mon "Whaaat."
    mon "Dont say that Sarah."
    show monica_sarah home17
    sar "Oh mon mon its ok."
    mon_wisper "Sarahhh..."
    sar "What?"
    mon_wisper "..I...I didnt want him to..."
    sar "Its ok Mon."
    show monica_sarah home18
    sar "Everything will be all right."
    menu:
        mc_thought "..."
        "Leave them alone":
            mc_thought "For some reason Monica is not comfortable with this conversation."
            mc "Well girls."
            mc "I think I will let you two talk alone."
            mc "Thank you for the conversation."
            hide monica_sarah
            return
        "Invite them to go inside":
            mc "I think its starting to get darker, we better go inside."
            mc "Maybe, you should get inside?"
            mc "You know, just to be safer"
            show monica_sarah home20
            mon "Good idea [player.name]!"
            mon "We should get inside."
            mon "Im going in now."
            sar "Im going too."
            show monica_sarah home6
            mc_thought "Man, this place is too good for me."
            mc "You two can go ahead."
            $ monica_sarah_invited = True
            mc "Im right behind you."
            hide monica_sarah
            return

            
        "What were you two talking about?":
            mc "Oh yeah? what were the two of you talking about?"
            sar "Oh we were just talking about how you have a bi..."
            show monica_sarah home20
            mon_shout "Nothing!" with vpunch
            mc "..."
            mon "Ahn, we were talking about nothing."
            mc_thought "DAMN, I really want to know..."
            mc "Ok, I think its a \'girls talk\'."
            mc "I will leave you two to it then."
            hide monica_sarah
            return


    # random question later
    
    
    


    

    return