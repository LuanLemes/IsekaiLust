screen linda_room():

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
        # sleep pillow
        if calendar.current_day_time > 2:
            if pillow_removed == False:
                imagebutton auto "overlays/linda sleep pillow %s.webp":
                    focus_mask True
                    xpos image_button_offset
                    ypos image_button_offset
                    action Call("linda_sleeping_pillow")
            else:
                imagebutton auto "overlays/linda sleep no_pillow %s.webp":
                    focus_mask True
                    xpos image_button_offset
                    ypos image_button_offset
                    action Call("linda_sleeping_pillow")
        # looking for bear
        if witch_talk_first == True and calendar.current_week_day != 0 and calendar.current_week_day != 6 and calendar.current_day_time == 2:
                imagebutton auto "overlays/linda room %s.webp":
                    focus_mask True
                    xpos image_button_offset
                    ypos image_button_offset
                    action Call("linda_looking_for_bear")

    use top_screen()

label linda_room:
    if linda_room_first == True:
        $ linda_room_first = False
        mc "Thats Lindas room, well she sure keeps all the toys from her childhood."
        return
    return

label linda_looking_for_bear:
    if linda_bear_first == False:
        show linda room idle
        mc_thought "(Well, the book told me to ask Linda about the map so here I am.)"
        lin "Where is it?"
        mc_thought "(Wait, is she looking for something? Is it the map?)"
        menu:
            mc_thought "(Maybe I should)"
            "Talk to her":
                mc_thought "(Let me talk to her.)"
                show linda bedroom1
                mc "Linda."
                lin "I swear I put it here."
                mc_thought "(Why does she never hear the first time?)"

            "Observe and see what she is doing":
                mc_thought "(Maybe I wont even have to ask, I will just keep quiet and find out.)"
                show linda bedroom1
                lin "I swear I put it here."
                mc_thought "(I think she is looking for the map.)"
            "Not right now":
                mc_thought "(Hmmm, Im not in the mood right now. Maybe another time.)"
                hide linda
                return
        $ linda_bear_first = True
        show linda bedroom2
        mc_thought "(I dont know what shes doing, but Im not going to stop her now.)"
        show linda bedroom5
        lin "It should be here somewhere."
        mc_thought "(Man, if she is looking for the map it was easier than I thought.)"
        show linda bedroom6
        lin "Maybe here?"
        mc_thought "(Never thought Linda looking for the map would be so interesting.)"
        lin "I just have to find it."
        lin "That person trusted me with this and I cant lose it."
        mc_thought "(Is the person her father? it all makes sense.)"
        mc_thought "(Man Im 100\% sure its the map.)"
        show linda bedroom7
        lin_shout "Why cant I find it?!" with vpunch
        lin "Gi gi gi gi gi gi gi gi..."
        menu:
            mc_thought "(Oh maaaan is she crying?)"
            "Linda":
                pass
            "Hey there Linda":
                pass
        show linda bedroom15 with dissolve
        lin "gi gi gi gi, hey [player.name] gi gi gi gi gi..."
        menu:
            "Are you ok?":
                lin "gi gi gi Im not gi gi gi.."
            "Why are you crying?":
                lin "gi gi gi Because gi gi gi gi..."
            "What happened":
                lin "gi gi gi gi gi gi..."
        mc_thought "(Man she doesnt stop crying, even though she is kind of cute.)"
        mc_thought "(What would Monica do in these situations?)"
        mc_shout "LINDA!"
        lin "..."
        mc_thought "(Thats it, she stopped crying.)"
        mc "Linda look at me."
        show linda bedroom8 with dissolve
        lin "..."
        mc_thought "(I think its working.)"
        mc "Dont make me repeat myself little girl."
        show linda bedroom9 with dissolve
        lin "..."
        mc_thought "(I cant believe it worked.)"
        menu:
            mc_thought "(I need to gain her trust here)"
            "I will help you":
                mc "Hey Lin, Im your [mclin]."
                mc "Whatever happened, I will help you ok?"
                lin "Okay."
            "Im with you":
                mc "Hey Lin, Im your [mclin]."
                mc "Its ok now, Im with you ok?"
                lin "Okay."
        lin "Thank you."
        mc "Ok, now tell me what is happening."
        show linda bedroom8 with dissolve
        lin "So.."
        show linda bedroom12
        lin "There is this person that is very important."
        mc "I see."
        mc_thought "(Your father, I know it has to be him Linda.)"
        show linda bedroom13
        lin "Who gave me this something that is also very important."
        mc "Yes I understand."
        mc_thought "(The map, I also know it has to be the map Linda.)"
        show linda bedroom14
        lin "But I was looking for it.."
        lin "I looked everywhere....and..."
        show linda bedroom15 with dissolve
        mc "And..."
        lin "And I lost the bear gi gi gi gi gi gi gi."
        mc_shout "Did you lose the map?!?!?" with vpunch
        mc_thought "(Wait right there...)"
        show linda bedroom17 with dissolve
        mc "Linda, what did you lose?"
        lin "The teddy bear my aunt gave me."
        mc "A teddy bear?!?"
        mc_thought "(Doesnt she have the map? But I thought the book said...anyway... It seems like a dead end.)"
        lin "But you said you would help me right?"
        mc_thought "(Man...what did I get myself into?)"
        mc "Errrrr yes I guess I said that."
        mc_thought "(Come on, Im a man of my word!)"
        mc "Raise your head Linda, Im here to help you."
        show linda bedroom18 with dissolve
        lin "Really????"
        mc_thought "(I guess?)"
        mc "Yes I will."
        menu:
            mc "But first."
            "Wipe your tears.":
                pass
            "I want to see your smile.":
                pass
        show linda bedroom20 with dissolve
        lin "Ok [player.name]."
        mc_thought "(I havent become an adventurer yet, but this sure feels like Im on a quest.)"
        show linda bedroom20 with dissolve
        lin "Ok, I did it."
        mc "..."
        show linda bedroom19 with dissolve
        mc_thought "(No you didnt but...)"
        mc "Anyway, just wait and I will bring your teddy bear back ok?"
        lin_shout "OKAY!"
        mc_thought "(Right, I almost forgot.)"
        menu:
            mc "Oh Linda, one more thing before I leave."
            "Ask her about the map":
                pass
        lin "What is it [player.name]."
        mc "Have you seen a map here around the house?"
        lin "Yes."
        mc "You have?! Where is it?!"
        lin "I will tell you when you bring my bear back."
        mc_thought "(Damn she is smart.)"
        $ linda.book_phrase = "thats all for this update.."
        $ linda.phase = 1
        $ debbie.book_phrase = "talk to debbie about the bear."
        hide linda
        mc "So all I need to do is bring her teddy bear back? Easy enough."
        $ teddybear_grocery_store = True
        return
    if linda_bear_first == True and linda.phase < 3 :
        show linda talking1
        menu:
            lin "So, have you found the teddy bear yet?"
            "Not yet":
                lin "Its ok, I trust you [player.name] you will surely find it."
                hide linda
                return
            "Yes I did (Requires teddybear)" if player_inventory.item_exists(300) != -1:
                call bear_found
                return
    else:
        # show linda talking1
        "In development."
        # hide linda
        return
    return

label linda_sleeping_pillow:
    if calendar.current_day_time == 4:
        if pillow_removed == True:
            show linda sleep no_pillow idle
        else:
            show linda sleep pillow idle
        mc_thought "(Im too tired to do anything right now.)"
        return

    show linda sleep pillow idle
    mc_thought "(I think linda is already sleeping.)"
    menu:
        mc_thought "(I should....)"
        "Get closer just to see if she needs something":
            pass
        "Let her sleep":
            mc_thought "(Good night little Linda, good night.)"
            scene
            return
    show linda pillow sleeping
    mc_thought "(She is so cute even when she is asleep.)"
    mc_thought "(She has such a nice ass but that pillow is in the way.)"
    mc_thought "(Wait...)"
    mc_thought "(Is that pillow?)"
    mc_thought "(Is that pillow going to fall on the floor?)"
    menu:
        mc_thought "(Is that pillow?)"
        "The pillow is too close to the edge":
            mc_thought "(That pillow is so close to the edge, maybe I should like....avoid it falling.)"
            mc_thought "(Yep, I should pick it up right now and put it in a safe place where it cant fall on the floor)"
        "Forget the pillow and go back to your room":
            mc_thought "(The pillow is ok, I think I will go back to my room.)"
            call time_next
            scene
            return
    show linda pillow sleeping2 with dissolve
    $ pillow_removed = True
    mc_thought "(The \"Pillow\" is safe and sound now hehehehe.)"
    mc_thought "(Oh man, so much better now!)"
    mc_thought "(Im the 'pillow saver!')"
    mc_thought "(And that ass sure is a life saver.)"
    menu:
        mc_thought "(Can I?)"
        "Can I get closer?":
            pass
        "Better leave before she wakes up":
            mc_thought "(If anyone would see me here it would be weird, time to go.)"
            call time_next
            scene
            return
    show linda pillow sleeping3
    mc_thought "(So better now.)"
    mc_thought "(Not only her ass but she has hot legs too.)"
    mc_thought "(But yes this is a nice ass.)"
    mc_thought "(Is she really sleeping?)"
    menu:
        mc_thought "(Let me check.)"
        "Get a better view to see if she is sleeping":
            pass
    mc_thought "(Just let me check if she is really sleeping, can never be too careful right?)"
    show linda pillow sleeping4
    mc_thought "(She is sleeping.)"
    mc_thought "(She looks so innocent.)"
    mc_thought "(Also the way she does everything without thinking is so cute.)"
    mc_thought "(Man I want to touch her so badly.)"
    show linda pillow sleeping3
    mc_thought "(Even though she is like family, this opportunity is too good for me to let it go.)"
    mc_thought "(Her ass is right here, Im not hurting anyone its just a little touch right?)"
    mc_thought "(Is like when we hug.)"
    menu:
        mc_thought "(I really need to decide)"
        "Touch her":
            mc_thought "(Just a little touch, I dont think it would be a bad thing.)"
            mc_thought "(Like...one second touch and I will be gone.)"
            mc_thought "(Right, one second and I will be gone.)"
            mc_thought "(Yes, one second touching her ass and thats it.)"
            show linda pillow sleeping5 with dissolve
            mc_thought "(Im getting there!)"
            mc_thought "(Why am I so afraid?)"
            mc_thought "(Is it the fear of getting caught?)"
            mc_thought "(What would Monica think?)"
            mc_thought "(Im not sure why...)"
            show linda pillow sleeping3 with dissolve
            mc_thought "(But I just cant do it yet.)"
            $ linda_touch_one = True
            call time_next
            scene
            return

        "Dont touch her":
            mc_thought "(I cant do this right now.)"
            mc_thought "(Its just...its just not right.)"
            call time_next
            scene
            return
    return

label linda_teddy_delivery:
    return

label bear_found:
    mc "Yes I did."
    menu:
        "Give her the teddy bear":
            pass
    mc "Here it is."
    show linda teddy1
    lin_shout "TIIIIMBERS!!!" with vpunch
    show linda teddy2
    lin "Timbers I will never lose you again."
    show linda teddy3
    lin "I swear I wont."
    show linda teddy2
    lin "I will take care of you."
    show linda teddy3
    lin "And tell you stories."
    show linda teddy6
    lin "And you are going to sleep with me, yes yes yes."
    mc_thought "Linda is so cute."
    mc_thought "Im happy because she is happy."
    show linda teddy3
    lin "Wait..."
    mc_thought "Oh no, did she realize it?"
    lin "Hmmm..."
    show linda teddy4
    lin "This"
    show linda teddy5
    lin "This is not Timbers...is it?"
    menu:
        "Tell her the truth":
            mc "Look linda, I looked everywhere"
            mc "And I didnt find it so I bought a new one for you"
        "Lie":
            mc "Look linda, I saw this guy that stole your bear."
            mc "Turns out he is a international teddy bear stealer."
            mc "He is wanted in several countries."
            mc "I knew he was around here."
            mc "But, to mess with My Linda? My [linmc]?"
            mc "No no! that he can not do?"
            mc "So I went after him."
            mc "After several days looking for him."
            mc "I found his hideout."
            mc "There was in fact a whole gang of bear stealers."
            mc "We had a reeeeeally huge fight"
            mc "Sometimes I was getting beaten by them."
            mc "Sometimes they were getting beaten by me."
            mc "And so it was.."
            mc "After hours of fighting that the leader jumped out with two bears in his hand."
            mc "And as he faded into the dark I was able to grab one of the bears from his hand."
            mc "I wished it was Timbers, but it was this one."
    mc "Im sorry Linda I did my best."
    lin "Waw, did you go through all this trouble for me?"
    lin "Why would you do such a thing?"
    show linda teddy7
    mc_shout "BECAUSE THATS WHAT HEROES DO." with vpunch
    show linda teddy8
    lin "You are my hero [player.name]!"
    mc "Wow Linda"
    lin "I had to demonstrate my gratitude."
    mc "I see but.."
    show linda teddy9
    lin "I always wanted to have someone like you."
    mc "Someone like me?"
    lin "Thanks for taking care of me."
    lin "You really are my [mclin]."
    show linda teddy10
    lin "*Kiss*"
    mc "Okay you won." with fade
    show linda teddy11
    mc "Now, tell me about the map, you promised."
    show linda teddy12
    lin "Ok, but first name my bear."
    show linda teddy11
    mc "Name your bear?"
    show linda teddy12
    lin "Yes, name it!"
    show linda teddy11
    mc "Ok, then his name will be:"
    $ teddy_name = renpy.input("The name of the bear will be", length = 21, default = "Mr Pickles" )
    show linda teddy12
    lin "Ok then his name will be [teddy_name] then."
    show linda teddy11
    mc "Now tell me about the map"
    show linda teddy12
    lin "Ok."
    lin "The last time I saw the map was a week ago."
    show linda teddy11
    mc "Where?"
    show linda teddy12
    lin "It was inside Ashleys room."
    show linda teddy11
    mc "Ashleys room?"
    show linda teddy12
    lin "Yes, I saw it in there, but please dont tell her. She cant know I go in there."
    show linda teddy11
    mc "Okay I wont."
    mc "Thanks Linda."
    show linda teddy12
    lin "Thank you [player.name], thanks to you I now have [teddy_name]."
    hide linda
    $ linda.phase = 3
    $ player_inventory.remove_item(300,1)
    return
