screen bathroom():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))
        imagebutton auto "overlays/bathroom toilet %s.webp":
            focus_mask True
            xpos -5
            ypos -5
            action Call("toilet")

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
    use top_screen()
    
label bathroom:
    return

label bathroom_on_enter:
    if calendar.current_day_time == 2 and calendar.current_week_day != 5:
        call monica_bath
        return _return
    return

label monica_bath:
    mc "My breath is awful, I really need to brush my teeth."
    mc "Oh maaaan locked again? ashley is that you?"
    mon "No [player.name] its me, Monica."
    mc "I see, are you going to take long?"
    mon "Kind of, Im showering and washing my hair too."
    mon "Is this something that you NEED to do right now?"
    menu:
        mc "..."
        "Now would be good":
            mc "Right now would be really good indeed."
            mon "Okay, im going to open the door, wait a little."
            mc_thought "(Is she actually going to open the bathroom?)"
            mon "You can enter now."
        "No, not at all":
            mon "Ok than, I will tell you when I leave."
            mc "Okay, thanks mon."
            return False
    show bathroom monica1
    mc_thought "(Man this is so strange.)"
    mc_thought "(I mean, Im actually in the bathroom while monica is showering.)"
    mc_thought "(She is actually a few meters away from me, fully naked.)"
    mon "Hey [player.name] was it an emergency? Are you okay?"
    mc "Hey mon, I am much better now that you opened the door."
    mc_thought "(I better start doing my things before she sees me here standing still.)"
    show bathroom monica2
    mc_thought "(I never paid attention to it because I dont usually use the bathroom with other people in it but..)"
    mc_thought "(I can actually see her in there!, I mean, I cant see her but, I can a little, I guess thats a blur or something.)"
    mc_thought "(Still Im happy that Im here.)"
    show bathroom monica2
    mc_thought "(Man she has such a beautiful body....At least...I think she does.)"
    mc_thought "(I think I can see the outline of her boobs too.)"
    mc_thought "(I think they are bigger than I thought.)"
    mon "Hey [player.name]."
    mc_thought "(Omg did she notice me staring?)"
    show bathroom monica6
    mon "Do you think that..."
    mon "Do you think that Im a good Mom?"
    menu:
        mc "why is she asking me this?"
        "I think you are an excellent mom":
            pass
        "I think you are a very good person":
            pass
        "I think you do your best":
            pass
    show bathroom monica4
    mc "And because of that I really admire the way you handle things."
    mc "Even your daughers are reflection of your hard work."
    show bathroom monica7
    mon "Thank you [player.name], its very important for me that you say those things"
    mon "It makes me happy to know that people see me this way."
    show bathroom monica8
    mon "And its even better when it comes from you."
    mon "Because you are also family, dont you ever forget that."
    show bathroom monica5
    mc_thought "(I think she is a true angel.)"
    mc "Thanks mom."
    mon "What did you call me?"
    show bathroom monica7
    mc "Haaan, Nothing nothing."
    show bathroom monica6
    mc "I think I should go."
    call time_next
    hide bathroom
    return False

label toilet:
    menu:
        "Use the Toilet" :
            play sound "audio/toilet.ogg" volume 0.4
            return
        "Masturbate(in development)" if 1 > 2:
            return
        "Nothing":
            return
    return
        
    

        
    
    


