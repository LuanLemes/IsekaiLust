screen grocery_store():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080

        background (str(map_image))
        if show_grocery_debbie == True:
            imagebutton auto "overlays/debbie grocery %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("talk_to_debbie_store")
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
    

label grocery_store:
    # menu:
    #     "Talk to Sally":
    #         call talk_to_sally
    #     "Do Nothing":
    #         jump reload_location
    # window hide
    # return
    return

label grocery_store_on_enter:
    if calendar.current_day_time >=2:
        mc_thought "The grocery store is closed at night."
        return False
    if grocery_store_first == True:
        $ grocery_store_first = False
        call grocery_store_first
        return True
    if debbie.phase == 4:
        call grocery_talk_about_milk
        return

    return

label grocery_store_first:
    mc_thought "Well, I think this is the place."
    scene grocery store morning
    show grocery first1
    with dissolve
    mc_thought "Just what is happening here?!!???" with vpunch
    deb "Moooom you are too heavyyyy."
    sar "Hold on dear, you have to hold firm there or I will fall."
    deb "Shouldn't we use a ladder or something?"
    sar "Yes we should but we don't have one here right now, just...just a little more my little Debbie."
    sar "Also, could you please use both of your hands?"
    deb "But mooooom, That's your ass, I shouldn't be touching it."
    sar "It's ok love, you can touch it, I wont be mad at you."
    deb "The problem is not you being mad at me, that's not it at all."
    mc_thought "Omg..is she complaining about touching that ass? I volunteer!!!"
    mc_thought "What am I saying I don't even know them...."
    mc_thought "Should I make a sound or ...maybe...idk...say hello?"
    menu:
        mc "Should I say something?"
        "Say Hello":
            mc_whisper "Hello."
            mc_thought "Oh...that's a pity...I think they didnt hear me."
            mc_thought "What can I say... I tried, didnt I?"
        "Keep quiet":
            mc_thought "I think I will enjoy the show a little more."

    sar_shout "Debbie Yamanaka hold my ass with both of your hands right now!"
    deb "Ok mooooom."
    show grocery first2
    sar "Good girl, Now just a little more, I am about to finish it, hold it right there."
    mc_thought "Yes...hold it right there, with both hands that's even better."
    deb "Are you done yet?"
    sar "Just a little more, damn these old shelves"
    deb "Mom...your ass is huge and heavy too, don't you know?"
    mc_thought "I don't know if that's heavy but no doubt it is huge"
    show grocery first3
    sar "I know, just a little more, I will give you a candy after we finish here ok?"
    deb "A candy? I think I deserve two because I am holding both sides of your ass."
    sar "Ok, I will give you two candies, I am sorry dear...your first day should be better than this."
    sar "But know that I love you."
    deb "I love you too mom, and I always obey you no matter what. Its just...I don't like this situation..."
    deb "I shouldn't be touching you...especially not there and not for so long."
    mc_thought "Well if they turn around now and see me here in silence it will be awkward."
    menu: 
        mc "I better say something"
        "Hello":
            mc "Hello."
        "Good morning":
            mc "Good morning."
    deb "Oh no..."
    sar "What is that?"
    deb "I think it's a customer...I will just pretend I am not even here...."
    sar "Don't be like that.."
    show grocery first4
    sar_shout "Hello there!"
    menu:
        deb  "This isn't happening..this isn't happening this isn't happening."
        "Hello again":
            mc "Hello again."
    sar_shout "I am sorry for the scene!"
    sar_shout "I was trying to fix this shelf you see!"
    mc "Oh, I see."
    sar_shout "But it was too high for me so my kind daughter offered me a hand!"
    mc "..."
    sar_shout "Or both hands in this case, haha!"
    show grocery first5
    deb  "This isn't happening..this isn't happening this isn't happening."
    sar "Oh, it's ok Debbie, you are just helping your mom, nothing wrong with that."
    deb "Mom, could you please come down? I feel shy doing this, especially when it's just the two of us...and now that there's someone else here, it's even more uncomfortable for me."
    show grocery first6
    sar "Ok love, now, please hold my ass with all your strength so I can get down ok?"
    deb "Oh seriously I can't believe this is happening."
    sar "Just hold on with all your strength and I will get down in a second ok?"
    deb "Like this?" with vpunch
    sar "Ahhh! yeah!!"
    show grocery first7
    sar "...oh..no no no no."
    show grocery first8 with vpunch
    mc "..."
    show grocery store morning
    mc "........"
    mc "Are you ok?"
    sar "Ye ye, we are ok....are you ok love?"
    deb "I will be when you stop sitting on my..."
    sar_shout "OK WE ARE OK!"
    mc "Maybe I can come back another time if it's ok with you guys."
    sar "No need, I will be there in a second."
    mc "..."
    show debbie grocery idle
    show sarah half normal with dissolve
    sar "I am sorry about that."
    sar "Hi, my name is Sarah and this is our han....\"grocery store\", but we buy and sell a little of everything here."
    mc_thought "Man, she is even more beautiful when she is up close."
    sar "And you are?"
    mc "Oh, I am sorry, hi my name is [player.name], nice to meet you."
    show sarah half normal2
    mc_thought "She heard about me?"
    menu:
        sar "Oh, so this is the [player.name] that I heard so much about hmmm?"
        "What did you heard about me?":
            show sarah half normal3
            sar "Nothing special, just that there were a new young boy in town...that's about it."
        "Who told you about me?":
            show sarah half normal3
            sar "I...well, I don't remember."
        "How did you know about me?":
            sar "A business woman is always well informed"
    mc_thought "Why do I feel like there is more to it?"
    mc "..."
    show sarah half normal
    sar "Sorry."
    sar "Ok, the truth is I work in the field with Monica so...we like to talk."
    show monica half overall talking with dissolve:
            xpos 572 alpha 0.33 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    mc_thought "Indeed..."
    mc_thought "She is wearing clothes very similar to Monicas."
    hide monica with dissolve
    mc "Oh, now I understand."
    sar "Anyway, this is our grocery store, so... are you looking for something to buy? Maybe a bouquet of flowers to give to your loved one?" 
    mc "What?" with vpunch
    mc "No no...nothing like that"
    show sarah half normal2
    sar "It's ok, you can tell me....I wont tell Monica, it can be our little secret."
    menu:
        mc "The truth is..."
        "I don't have a girlfriend":
            sar "Oh...thats so nic....a pity...that's a pity..."
            sar "I am sure you will find one"
        "I don't have a loved one yet":
            sar "Oh...not a problem dear, you will find it soon enough."
    mc "Well, thanks"
    mc "Anyway, I started working on the fields today... and Monica told me I could come here and sell the flowers to make some money."
    show sarah half normal3
    sar "Oh so you will work on the fields with us too? I am so excited to work with you."
    mc_thought "No...I am excited to work with you"
    sar "Well, In that case you can talk with little Debbie over there."
    show sarah half hands:
        matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    sar_shout "SHE IS MY DAUGHTER!" with vpunch
    mc_thought "Wait...what?"
    show sarah half hands2
    sar_shout "SO TREAT HER WELL!" with vpunch
    mc_thought "What the hell? I can feel her intent to kill me all the way from here."
    show sarah half hands3:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    sar "for your own good."
    show sarah half normal3:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    sar "Be kind, she also is on her first day at work. I have to go now, bye."
    hide sarah with dissolve
    mc_thought "Man...she was very kind and all of sudden she went full psycho killer..."
    mc_thought "And somehow I know she is not kidding..."
    mc_thought "I better treat her daughter with respect."
    $ sarah.revealed = True
    return

label grocery_store_on_exit:
    if debbie_first == True:
        show debbie grocery idle
        mc "I came to sell the flowers, I should at least talk with the girl to see how it works."
        hide debbie
        return False
    return True

label talk_to_debbie_store:
    $ debbie.revealed = True
    scene grocery in
    if debbie_first == False:
        show debbie half grocery
        deb "Hi [player.name], how are you?"
    # teddy bear avilable dialog
    if teddy_available_first_dialog == True:
        call teddy_bear_available

    if debbie_first == True:
        $ debbie_first = False
        # show debbie half grocery
        show debbie half grocery shy
        deb "Hi...."
        menu:
            mc_thought "Is she still sad about what just happened?"
            "Are you ok?":
                mc "Hey...are you ok?"
                deb "Yeah..it's just...a shame you saw us in that situation."
            "Is everything alright?":
                mc "Hey...is everything alright?"
                deb "It is...it's just...seriously...a shameful situation you just saw."
        mc "Its alright nothing to be ashamed of, you were just helping your mom"
        menu:
            deb "Yes, I guess so..."
            "That was impressive":

                mc "Besides, that was very impressive, I mean, your Mom doesn't seem to be someone easy to lift."
            "You are a good daughter":
                mc "Besides, you conquered your fears, even though you didn't want to do it, you did it because you are a good daughter."
        show debbie half grocery5
        deb "You think soooo? Thank you, thank you a lot."
        deb "You know, it's very important to me that I be a good daughter to my mom."
        mc "Is that so?"
        show debbie half grocery6
        deb "Yes, yes it is, you see...me and my mom are not blood related. I mean you may have guessed by the color of our hair."
        mc "Yet she seems to treat you very well doesn't she?"
        show debbie half grocery7
        deb "Yes, yes she does treat me very well, she is like an angel in my life."
        mc_thought "She is talking about Sarah...her mom, the way I talk about Monica."
        show debbie half grocery2
        deb "My mom died in an accident when I was 3 years old, and she has been raising me as my mom ever since."
        show debbie half grocery7
        deb "Sarah is awesome!, but...as you saw, she can be overprotective sometimes, I think that's because she loves me."
        mc "Yes, I was scared back there for a second."
        show debbie half grocery6
        deb "But she is the best person I know, she is just the best."
        deb "Anyway...I am sorry, you must be here for business"
        mc "Yes I am indeed."
        show debbie half grocery with dissolve
        deb "So, what do you want to do?"

    call debbie_grocery_choices
    return

    label debbie_grocery_choices:
        show debbie half grocery
        menu:
            "What do you want to do?"
            "Buy and sell":
                call open_grocery_store
            "Talk":
                call talk_with_debbie_grocery
            "Do you have any teddy bears for sale?::teddybear_grocery_store":
                call do_you_have_any_teddybears
            "I want to buy a teddy bear (30 coins)::can_buy_teddy" if player.money >= 30:
                call buy_teddy_bear
            "Nothing for now, thank you":

                show debbie half grocery7
                deb "Thank you for your business."
                if prologue == True:
                    $ prologue = False
                    call time_next
                    call change_location_to("Forest Wall")
                return
        call debbie_grocery_choices
        return


label talk_with_debbie_grocery:
    show debbie half grocery
    menu:
        
        "Talk about what?"
        "About her mom":
            show debbie half grocery2
            deb "Mom?...well"
            deb "Yes, yes it is, you see...me and Sarah are not blood related. I mean you may have guessed by the color of our hair."
            show debbie half grocery2
            deb "My mom died in an accident when I was 3 years old, and Sarah has been raising me as my mom ever since."
            deb "So, she is like my mom now."
            mc "Yet she seems to treat you very well doesn't she?"
            show debbie half grocery7
            deb "Yes, yes she does treat me very well, she is like an angel in my life."
            mc_thought "She is talking about Sarah...her mom, the way I talk about Monica."
            show debbie half grocery6
            deb "Sarah is awesome!, but...as you saw, she can be overprotective sometimes, I think that's because she loves me."
            mc "Yes, I was scared back there for a second."
            show debbie half grocery5
            deb "But she is the best person I know, she is just the best."
        "Why work here?":
            mc "So...do you like working here?"
            show debbie half grocery2
            deb "No."
            mc "No?"
            show debbie half grocery5
            deb "I am sorry, let me explain, It was never my dream to work at my mom's store."
            show debbie half grocery6
            deb "But if that's what she wants me to do, I will do it with a smile."
            mc "You must really love your mom"
            show debbie half grocery7
            deb "Yes, I really do."
        "About her parents":
            show debbie half grocery2
            mc "What happened with your parents?"
            deb "I...I don't know the details, the only thing I know is that they died in an accident."
            mc "I am sorry."
            show debbie half grocery3
            deb "No need to, It was a long time ago."
        "Nothing, thanks":
            mc "..Nothing, thanks."
            return
    call talk_with_debbie_grocery
    return

label do_you_have_any_teddybears:
    $ debbie.book_phrase = "2"
    $ debbie.phase = 1

    $ teddybear_grocery_store = False
    show debbie half grocery7
    deb "Bears?"
    mc "Not real bears."
    mc "More like, you know, teddybears."
    show debbie half grocery6
    deb "Well....that is rare."
    mc "Teddy Bears are rare?"
    show debbie half grocery7
    deb "No, it's rare seeing a man looking for teddy bears."
    mc_thought "Great, so I can get Linda to tell me about the secret map."
    show debbie half grocery6
    deb "But mom says business is business."
    show debbie half grocery7
    deb "Don't worry we got teddy bears, just one second."
    show debbie looking2
    deb "It's right here."
    deb "Not here?"
    show debbie looking
    deb  "Hmm I think mom may have put them here."
    deb "Not here too?"
    menu:
        mc "..."
        "Do you want me to help looking?":
            pass
        "Are you sure you don't want me to come back later?":
            pass
    show debbie looking2
    deb "Just a second, I will find it. I am certain that I will."
    mc "Ok."
    show debbie looking3
    deb "Maybe it's here?"
    deb "Mom, where did you put it?"
    show debbie door
    deb "Just let me take a look inside, one second."
    hide debbie with dissolve


    mc "Ok."
    # sound effects
    play audio "audio/Ceramic-Break-1.ogg"
    play audio "audio/Ceramic-Break-2.ogg"
    deb "I swear...."
    play audio "audio/Ceramic-Break-1.ogg"
    play audio "audio/Ceramic-Break-2.ogg"
    # I saw it somewhere
    deb "I saw it here somewhere."
    play audio "audio/Rock-Breaking-2.ogg"
    deb "I only need to find where."
    mc "..."
    play audio "audio/Rock-Breaking-1.ogg"
    play audio "audio/Ceramic-Break-2.ogg"
    deb "Is it up there?"
    mc_thought "It seems like she is wrecking the whole place."
    show debbie half grocery7 with dissolve
    mc "So, did you find it?"
    deb "Well, it seems, oh wait, maybe there is somewhere else."
    show debbie looking4
    deb "Hmmm maybe here?"
    mc_thought "What? she is always so polite I didn't realize she had such a nice ass."
    mc_thought "I should come back here more frequently for sure."
    show debbie grocery surprised
    deb "Well, I am really sorry."
    deb "It seems like we don't have more teddy bears."
    mc "That's bad."
    deb "But I will talk to our suppliers and I will tell you as soon as they get here ok?"
    show debbie half grocery with dissolve
    mc_thought "She is so polite, Sarah raised a good girl."
    deb "Ok, I will be waiting."
    return


label open_grocery_store:
    # $ ui_show_foward_time = False
    $ ui_show_time =  False
    $ ui_show_money = False
    $ ui_show_maps = True
    $ ui_show_location = True
    $ ui_can_change_map = False
    $ ui_can_inventory = False
    call screen grocery_store_screen
    hide screen grocery_store_screen
    $ ui_can_inventory = True
    # $ ui_show_foward_time = True
    $ ui_show_time =  True
    $ ui_show_money = True
    $ ui_show_maps = True
    $ ui_show_location = True
    $ ui_can_change_map = True
    $ ui_can_inventory = True
    return

label teddy_bear_available:
    $ teddy_available_first_dialog = False
    mc "Hi debbie, Monica told me you went to the house to...."
    show debbie half grocery7
    deb "Oh yes, I went there, she said you were sleeping but she went to wake you up."
    show debbie half grocery6
    deb "But then she came back all face red and told me you got the message."
    mc_thought "So Monica was happy after that?"
    show debbie half grocery7
    deb "She looked, different. Did something happen?"
    show bedroom1 monica5:
            alpha 1.69 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.35)*BrightnessMatrix(-0.01)*HueMatrix(0.0) 
    with dissolve
    mc "If something happened?"
    hide bedroom1 with dissolve
    mc "No nothing special really."

    show debbie half grocery6
    deb "I see, maybe Im wrong then."
    deb "Anyway the teddy bears arrived, if you want one it will be 30 coins."
    return

label buy_teddy_bear:
    if player.money > 30:
        $ can_buy_teddy = False
        $ debbie.phase = 3
        $ linda.phase = 2
        $ player.money -= 30
        show debbie half grocery6
        deb "Ok [player.name]."
        show debbie half grocery7
        deb "Here it is."
        $ player_inventory.add_item(300, 1)
        "{color=#9fe58b}You got 1 TeddyBear{/color}"
        mc "Thanks Debbie, you are the best!"
        show debbie half grocery6
        deb "Another happy client he he."

label grocery_talk_about_milk:
    scene grocery in
    show sarah grocery1
    show debbie half grocery
    deb "Hi [player.name] how are you?"
    mc "Hi, Debbie, Im doing well."
    show debbie half grocery2
    deb "Glad to hear that."
    menu:
        "Do you have any milk?":
            pass
        "Can I buy some milk?":
            pass
    show debbie half grocery3
    deb "Oh...milk."
    deb "There is some time since the last time we had milk."
    mc_thought "I kind of knew it wouldn´t be that easy."
    show sarah grocery2
    mc "Why is that?"
    show debbie half grocery4
    deb "Well, we dont know."
    mc "How so?"
    deb "They just stopped delivering milk to us just like that."
    show debbie half grocery2
    hide sarah
    show sarah half normal:
            xpos 105 
    sar "Hello [player.name] I think they are facing problems at the farm."
    sar "I didnt have the oportunity to go to the farm yet."
    show sarah half normal2
    sar "But I think it would be good both for you and our business if you could go there and maybe get some information."
    mc_thought "This \"Milk quest\" is getting bigger by the second."
    mc "Ok I think I will see if I can find something."
    show sarah half normal3
    sar "Good, Debbie will show you the way."
    show debbie grocery surprised
    $ Place18.map_to_show = 1
    deb "I will what?"
    hide sarah with dissolve
    mc "she left..."
    deb "Ok I will..."
    $ debbie.phase = 5
    call change_location_to("Forest Wall")
    return
    # $ change_location_to
    
