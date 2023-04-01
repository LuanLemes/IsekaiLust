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
    if calendar.current_week_day == 6 or calendar.current_week_day == 0:
        dev "The game weekend has not yet prepared so the game is going to skip the weekend, (Im so very sorry updates are coming.)"
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
        "I shoudn´t go to sleep now, I have more important things to do."
        return
    menu:
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
    mc "That was a really good night sleep."
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