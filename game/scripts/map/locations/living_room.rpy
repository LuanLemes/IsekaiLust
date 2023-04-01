screen living_room():

    frame:
        yoffset 0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image)) 


        imagebutton:
            focus_mask True
            xpos -15
            hovered SetVariable("focus_location", "Monica Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to mom bedroom hover.webp")
            idle ("overlays/living room to mom bedroom.webp")
            action Call("change_location_to", "Monica Room")

        imagebutton:
            focus_mask True
            xpos -15
            ypos 0
            hovered SetVariable("focus_location", "Kitchen")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to kitchen hover.webp")
            idle ("overlays/living room to kitchen.webp")
            action Call("change_location_to", "Kitchen")

        imagebutton:
            focus_mask True
            xpos -15
            ypos 0.0
            hovered SetVariable("focus_location", "Room")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to secret room hover.webp")
            idle ("overlays/living room to secret room.webp")
            # action Call("change_location_to", "Kitchen")
            action Call("secret_room")

        imagebutton:
            focus_mask True
            xpos -15
            ypos 0.0
            hovered SetVariable("focus_location", "Leave")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/living room to map hover.webp")
            idle ("overlays/living room to map.webp")
            action Call("change_location_to", "Home")

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
        # event linda cards
        if calendar.current_week_day != 6 and calendar.current_week_day != 0 and calendar.current_week_day != 2 and calendar.current_week_day != 4 and calendar.current_day_time == 0 and calendar.current_day > 3 and breakfasted == True:
            imagebutton auto "overlays/linda cards morning %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("linda_cards")
        # ashley dancing event
        if calendar.current_week_day != 6 and calendar.current_week_day != 0 and calendar.current_day_time == 2:
            imagebutton auto "overlays/ashley monica overlay %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("ashley_dancing")

    use top_screen()
    
label linda_cards:
    show linda cards morning idle
    if linda_cards_first:
        $ linda_cards_first = False
        mc_thought "Is that linda? shouldnt she be at school?"

        mc "Hey Linda."
        mc_thought "Guess she didnt listen."
        show linda cards1
        mc "Linda?"
        lin "So maybe if I memorize then?"
        mc_thought "Man..she is very concentrated."
        mc_thought "Maybe if I get closer."
        show linda cards2
        lin "I think the black card is....taller?"
        mc "..."
        menu:
            "LINDA!!!!":
                mc_shout "LINDA!!!" with vpunch
            "(Stare)":
                mc "...."
        show linda cards3 with dissolve
        lin "Oh, hey [player.name]."
        mc "Hey."
        mc "Shouldnt you be at school?"
        lin "No because I passed and today is my first day on...."
        show linda cards4 with vpunch
        lin_shout "VACATION!!!!!" with vpunch
        lin_shout "YEEEEEEEEEEY!!" with vpunch
        mc "Oh, I see, thats good, congratulations."
        show linda cards5 
        lin "Thank you thank you, Im the legend."
        mc "Haha."
        mc "So, what are you doing?"
        lin "Oh, Im trying to get better at this game."
        mc "Huuu cool."
    lin "Do you want to play?"
    menu:
        "Yes I do":
            pass
        "Hmm not right now":
            lin "Why noooooot?!??!?!?"
            mc "I got things to do."
            lin "Just one little time pleeeeeease?"
            menu: 
                "Ok, I will play with you.":
                    pass
                "Not this time little linda":
                    lin "You are so meeeeeaaan."
                    return
    scene cards_bg
    show linda cards6
    show card_2_diamonds
    show card_4_diamonds
    show card_5_diamonds
    show card_a_diamonds
    show card_k_diamonds

    $ card_2_diamonds = True
    $ card_4_diamonds = True
    $ card_5_diamonds = True
    $ card_a_diamonds = True
    $ card_k_diamonds = True
    $ linda_game_over = False
    $ linda_floor_card = False
    $ count_linda_cards = 5
    menu:
        "Lets Start":
            lin "Ok then, you first."
            $ linda_games += 1
            call linda_play_cards
        "Explain the game":
            lin "Ok, this game is very very simple because its a LUCK game."
            lin "We got 5 cards here."
            show blue_card
            lin "All of them have a blue face."
            hide blue_card
            lin "Before the game start, without knowing witch card it is, we are going to change one card."
            show black_card
            lin "This card will be the black card."
            hide black_card
            lin "Then we are going to put then on the floor like they are right now."
            lin "And whoever chosses the black card first wins."
            call linda_play_cards
    return
    
label linda_play_cards:
    if linda_game_over:
        return
    menu:
        "The 2 diamonds::card_2_diamonds":
            $ card_k_diamonds = False
            hide card_2_diamonds
            call is_the_card

        "The 4 diamonds::card_4_diamonds":
            hide card_4_diamonds
            $ card_4_diamonds = False
            call is_the_card
        
        "The 5 diamonds::card_5_diamonds":
            hide card_5_diamonds
            $ card_5_diamonds = False
            call is_the_card

        "The A diamonds::card_a_diamonds":
            hide  card_a_diamonds
            $ card_a_diamonds = False
            call is_the_card

        "The K of diamonds::card_k_diamonds":
            hide card_k_diamonds
            $ card_k_diamonds = False
            call is_the_card
    call linda_play_cards
    return

label is_the_card:
    $ phrase = renpy.random.randint(1, 100) 
    $ phrase = renpy.random.randint(1, 100) 
    "[phrase]"
    $ count_linda_cards -= 1
    if count_linda_cards <= 1:
        $ phrase = 100
    if phrase < 80:
        call linda_turn_card
        return
    else:
        # mc wins
        mc_shout "HUUUUUUUUUU I WOOOON!!!" with vpunch
        if count_linda_cards == 4:
            show linda cards8 with dissolve
        else:
            show linda cards7 with dissolve
        lin "Thats not faiiiiir."
        if count_linda_cards == 4:
            lin "I didnt even get a chance to try....."
            mc_thought "She is really sad."
            mc "Its not like that, it was only luck."
        mc "Hey Linda dont be sad, we can play again some other time right?"
        show linda cards7 with dissolve
        lin "Hmmm..."
        mc "What is it?"
        lin "You promisse?"
        menu:
            "Yes I promisse.":
                pass
            "I...Will do my best":
                pass
        lin "Okay then, thank you...[player.name]."
        mc_thought "Wow she usually is so childish and all of sudden so mature."
        show linda cards9 with vpunch
        lin_shout "BUT IM SURE GOING TO WIN NEXT TIME!!!"
        mc_thought "Now thats the linda I know."
        mc "Okay then see ya."
        scene
        $ linda_game_over = True
        return
    return        

label linda_turn_card:
    lin "YES! Its not this card, so now its my turn."
    show linda cards7 with dissolve
    lin "Let me see...what I think Im going to pick..."
    if count_linda_cards == 2:
        lin "Ok...maybe if I...."
        show linda cards10
        $ linda_floor_card = True
        mc "Linda...."
        mc "Linda is this allowed in the rules?"
        lin "I created this game so Im going to say...yes it is."
        if renpy.random.randint(1,100) < 50:
            show ashley card1
            ash "What in the harry potter are you doing?"
            lin "Just a second Ash, Im going to win no matter what it takes."
            ash "Mom wont be happy if she sees you on the floor like this."
            lin "If I win, its worth it!"
            hide ashley

    if card_2_diamonds == True:
        lin "I chosse the card 2 diamonds."
        $ card_2_diamonds = False  
        hide card_2_diamonds  
    elif card_4_diamonds == True:
        lin "I chosse the card 4 diamonds."
        $ card_4_diamonds = False    
        hide card_4_diamonds
    elif card_5_diamonds == True:
        lin "I chosse the card 5 diamonds."
        $ card_5_diamonds = False    
        hide card_5_diamonds
    elif card_a_diamonds == True:
        lin "I chosse the card A diamonds."
        $ card_a_diamonds = False    
        hide card_a_diamonds
    elif card_k_diamonds == True:
        lin "I chosse the card K diamonds."
        $ card_k_diamonds = False    
        hide card_k_diamonds
    
    $ count_linda_cards -= 1
    $ phrase = renpy.random.randint(1, 100) 
    $ phrase = renpy.random.randint(1, 100) 
    if count_linda_cards <= 1:
        $ phrase = 100
    if phrase < 80:
        lin "Noooo!"
        if linda_floor_card == False:
            show linda cards6
        mc "Not your card, now its my turn."
        if count_linda_cards == 1:
            lin "I have a bad feeling about this..."
    else:
        show linda cards9
        lin_shout "YES YES YES!!!" with vpunch
        lin_shout "I woooooooon!!!" 
        mc "Maybe next time around."
        $ linda_game_over = True
        menu:
            "Im going to win next time you will see!":
                lin "I will be waiting for you."
            "You are the best player.":
                lin "Yes I ammm!"
        return

label living_room:
    if prologue_to_living_room == True:
        show linda running livingroom 
        lin_shout "Out of the way pleeeeease!!!!!" with vpunch
        mc "What?"
        lin_shout "Moooom Im Hungry!!!!"
        hide linda with dissolve
        mc "I guess, she is hungry."
        $ only_location = "Kitchen"
        $ only_location_message = ["I have to see Monica (She is on the Kitchen)"]
        $ prologue_to_living_room = False
label living_room_before_enter:
    return


label secret_room:
    mc "This room is locked since the day I got here, no idea whats in there."
    return

label ashley_dancing:
    show ashley monica overlay idle
    mc_thought "Is Ashley exercising or something?"
    menu:
        "Go to the sofa":
            mc_thought "Im a simple man, I see a girl wearing gym clothes, I smile."
            mc_thought "This seems like a good moment to spend some time on sofa with everyone."
        "Do nothing":
            mc_thought "Anyway."
            return
    scene monica ashley sofa1
    ash_shout "WHAT ARE YOU DOING?!?" with vpunch
    menu:
        "Chilling?":
            mc "I am....chilling?"
            ash_shout "Go chill somewhere else!"
        "Am I doing something?":
            mc "Am I doing something?"
            ash_shout "Yes you are!!!!" with vpunch
    mc_thought "Man...she is hiding her body like Im some kind of...wow,..dat legs....ok maybe she is right."
    mon "Ashley..."
    show monica ashley sofa2
    ash "Mom, he is only in the sofa to see me training."
    mon "Ashley its not like that."
    show monica ashley sofa3
    ash "Mom, dont you see it? its obivious!"
    mon "What is obvious linda?"
    show monica ashley sofa2
    ash "Im wearing gym clothes and he is a man!"
    mon "..."
    show monica ashley sofa3
    ash "He is a man!"
    show monica ashley sofa2
    mon "My star, I love you so much."
    mon "But you cant just expel people out of the living room because what you think they are thinking."
    ash "But Mooom...he is ...he is..."
    show monica ashley sofa3
    mon "No buts little girl, you are going to train and you are going to let people be."
    ash "Then where can I train to the cheerleader test?"
    show monica ashley sofa2
    mon "Just keep training as you were, If we are distracting you its just not to pay attention to us."
    ash "..."
    mon "Thats how I trained when I was a cheerleader."
    mc "..."
    show monica ashley sofa4
    ash "Fine!"
    mc_thought "Man...monica is cute and ashley seems like a wild tiger. But I have to say Monica always have the upper hand."
    show monica ashley sofa5
    mc_thought "Hm interesting."
    mc_thought "I never paid attention but..ashley has indeed a nice ass."
    
    $ ashley_poses_count = 0
    call ashley_train
    return

    label ashley_train:
    "point"
    $ phrase = renpy.random.randint(5,21)
    $ phrase = renpy.random.randint(5,21)
    
    if phrase == 5:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Man, I could slap that ass."
    if phrase == 6:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Indeed I could slap that ass."
    if phrase == 7:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "This one is very important to your elbows."
    if phrase == 8:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought  "Oh yeah, you dont want to leave that one out."
    if phrase == 9:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought  "Very good angle."
    if phrase == 10:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "You know, I dont think I will ever get tired of this short."
    if phrase == 11:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Now to the left."
    if phrase == 12:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Yes, make that body fell the heat Ashley."
    if phrase == 13:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "This side is good too."
    if phrase == 14:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Such beautifull socks."
    if phrase == 15:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "I really like her legs."
    if phrase == 16:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "I could fuck that ass right now."
    if phrase == 17:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Yes, open that arms."
    if phrase == 18:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Yes, balance its a very important thing."
    if phrase == 19:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "I didnt know she could do that."
    if phrase == 20:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "I wonder how long can she do that."
    if phrase == 21:
        show expression "monica ashley sofa"+str(phrase)
        mc_thought "Seeing her do this gimme some ideas."
    $ ashley_poses_count += 1

    if ashley_poses_count == 4:
        call awake_night_sofa
    if ashley_poses_count ==3:
        mc_thought "I think Im getting very sleepy."
    if ashley_poses_count < 4:
        call ashley_train
    return

label awake_night_sofa:
    mc_thought "I think Im going to..."
    scene black with Dissolve(2.0)
    mc_thought "..."
    scene monica ashley sofa22 with Dissolve(2.0)
    mc_thought "I think I ended up sleeping."
    mc_thought "Ashley is gone."
    mc_thought "Wait...is that Monica?"
    menu:
        "Take a look.":
            "Lets see..."
            scene monica ashley sofa23
        "Go back to sleep.":
            mc_thought "Im too sleepy for anything right now."
            show monica ashley sofa33
            mc_thought "I sleept too much, everybody is gone, I better go to my bed."
            $ sleep_when_enter = True
            $ dont_show_map_image = True
            call change_location_to("Bedroom")
            # be sure it works
            scene black with dissolve
            return
    mc_thought "She is sleeping too."
    mc_thought "Is that?"
    mc_thought "Is that?!?"
    scene monica ashley sofa25
    mc_thought "Her panties?!?!" with vpunch
    mc_thought "No doubt about that..."
    mc_thought "Its only a tiny tiny bit of her panties but yes...I can see Monica´s panties."
    scene monica ashley sofa23
    mc_thought "Damn she is hot."
    mc_thought "I think she is moving...I think she is moving."
    mc_thought "Is she waking up? not, thats not it."
    scene monica ashley sofa24 with dissolve
    mc_thought "She moved."
    mc_thought "She is changing her position a little."
    mc_thought "Thankfully she didnt wake up, I can enjoy the view a little more."
    show monica ashley sofa26
    mc_thought "I can see even more of her panties right now!!!!" with vpunch
    mc_thought "They are beautiful!!!"with vpunch
    mc_thought "I could be here the whole night."
    mc_thought "Man...my dick is so hard right now."
    mc_thought "Maybe I could..."
    menu: 
        "Masturbate looking at her. (Require courage/Wait for the next updates)" if 1 > 2:
            pass
        "Just look for now":
            pass
    show monica ashley sofa24 with dissolve
    mc_thought "Wait...I think someone is coming."
    show monica ashley sofa27 with dissolve
    mc_thought "Oh, Its linda."
    lin "Mooooom."
    mc_thought "What is she doing?"
    lin "Hey Mooom."
    mc_thought "You are going to wake her up."
    mc_thought "Im having a good time."
    mc_thought "dont do it!" with vpunch
    show monica ashley sofa28 with dissolve
    mc_thought "Not gonna lie, she is waking monica but damn she has nice ass."
    mc_thought "I love these sleeping clothes she uses."
    show monica ashley sofa29 with dissolve
    lin "Heeeeeey Mooooom wake up."
    mc_thought "She pulled her skirt up?!!?!?" with vpunch
    mc_thought "I think...."
    camera:
            pos (-1089, -343) xzoom 1.01 zoom 2.34 
    mc_thought "I think Im in heaven." with vpunch
    call camera_reset
    mc_thought "Linda my little [linmc] and Monica my [monmc]."
    mc_thought "Both of them here this way."
    mc_thought "Im happy."
    lin "Mooooom."
    show monica ashley sofa30
    mon "Hun?"
    mon "Hey my little star."
    show monica ashley sofa31
    lin "Mom I had a nightmare, I cant sleeeeeep."
    mc_thought "Linda is so cute, and Monica is such a good mom for her."
    mc_thought "And they are both so hot...thats cute and hot."
    lin "I cant sleep mom."
    mon "Oh my baby dear I will...."
    show monica ashley sofa32
    mon "..."
    mc_thought "She is looking at me!!" with vpunch
    menu:
        "!She is looking at me!"
        "Close your eyes!":
            pass
        "Close your eyes!":
            pass
        "Close your eyes!":
            pass
        "Close your eyes!":
            pass
    
    scene black with Dissolve(2.5)
    mc_thought "Man...did she see my erection? I dont think so..I mean, its too dark I think."
    lin "Mom?"
    mon "...Im sorry dear I just...got lost in my thoughts for a momment."
    mon "Do you want to sleep here in the sofa with me?"
    mc_thought "Are they going to sleep on the sofa?"
    mc_thought "Please say yes please say yes please say yes."
    lin "I want you to tell me a story so I can sleep on my room."
    mon "Are you sure you dont want to stay? the sofa is so confy my baby."
    lin "Not today mom."
    mon "Ok, then lets go to your room, I will tell you the story of the big snake."
    lin "Big snake?"
    mon "Yes, but its a good snake she is a....."
    mc_thought "I think they are gone."
    menu: 
        "Open your eyes":
            pass
    show monica ashley sofa33 with Dissolve(2.5)
    
    mc_thought "They are gone, Its too late, I think I should go to my bed sleep too."
    # call change_location_to("")
    $ sleep_when_enter = True
    $ dont_show_map_image = True
    call change_location_to("Bedroom")
    return

        










    
    
