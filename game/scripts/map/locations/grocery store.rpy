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
    return
label grocery_store_first:
    mc_thought "Well, I think this is the place."
    scene grocery store morning
    show grocery first1
    with dissolve
    mc_thought "Just what is happening here?!!???" with vpunch
    deb "Moooom you are too heavyyyy."
    sar "Hold don dear, you have to hold firm there or I will fall."
    deb "Shouldn´t we use a stair or something?"
    sar "Yes we should but we dont have one here right now, just...just a little more my little Debbie."
    sar "Also, could you please use both of your hands?"
    deb "But mooooom, Thats your ass, I shouldn´t be touching it."
    sar "Its ok love, you can touch it, I wont be mad at you."
    deb "The problem is not you being mad at me, thats not it at all."
    mc_thought "Omg..is she complaining to touch that ass? I volunteer!!!"
    mc_thought "What am I saying I dont even know them...."
    mc_thought "Should I make a sound or ...maybe...idk...say hello?"
    menu:
        "Should I do something?"
        "Say Hello":
            mc_whisper "Hello"
            mc_thought "Oh...thats a pitty...I think they didnt hear me."
            mc_thought "What can I say... I tried didnt I?"
        "Keep quiet":
            mc_thought "I think I will enjoy the show a little more."

    sar_shout "Debbie Yamanaka hold my ass with both of your hands right now!"
    deb "Ok mooooom."
    show grocery first2
    sar "Good girl, Now just a little more, Im about to finish it, hold it right there."
    mc_thought "Yes...hold it right there, with both hands thats even better."
    deb "Are you done yet?"
    sar "Just a little more, damn these old shelves"
    deb "Mom...your ass is huge and heavy too, dont you know it?"
    mc_thought "I dont know if thats heavy but no doubt it is huge"
    show grocery first3
    sar "I know, just a little more, I will give you a candy after we finish here ok?"
    deb "A candy? I think I deserver two because im holding both sides of your ass."
    sar "Ok, I will give you two candies, Im sorry dear...I your first day would be better than that."
    sar "But Know that I love you."
    deb "I love you too mom, and I always obey you no matter what. Its just...I dont like this situation..."
    deb "I shouldn´t be touching you...really not there and not for so long."
    mc_thought "Well if they turn around now and see me here in silence will be awkward."
    menu: 
        "I better say something"
        "Hello":
            mc "Hello."
        "Good morning":
            mc "Good morning."
    deb "Oh no..."
    sar "What is that?"
    deb "I think its a costumer...I will just pretend im not even here...."
    sar "Dont be like that.."
    show grocery first4
    sar_shout "Hello there!"
    deb  "this isnt happening..this isnt happening this isnt happening."
    menu:
        "Hello again":
            mc "Hello again."
    sar_shout "Im sorry for the scene!"
    sar_shout "I was trying to fix this shelf you see!"
    mc "Oh, I see."
    sar_shout "But it was too heigh for me so my kind daugher offered me a hand!"
    mc "..."
    sar_shout "Or both hands in this case, haha!"
    show grocery first5
    deb  "this isnt happening..this isnt happening this isnt happening."
    sar "Oh, its ok Debbie, you are just helping your mom, nothing wrong with that."
    deb "Please mom, get down, Im too shy for that if is just the two of us..and now there is someone else here."
    show grocery first6
    sar "Ok love, now, please hold my ass with all you strenght so I can get down ok?"
    deb "Oh seriously I can´t believe this is happening."
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
    sar "Ye ye, we are ok....Are you ok love?"
    deb "I will be when you stop sitting on my..."
    sar_shout "OK WE ARE OK!"
    mc "Maybe I can come back another time if its ok with you guys."
    sar "No need, I will be there in a second."
    mc "..."
    show debbie grocery idle
    show sarah half normal with dissolve
    sar "Im sorry about that."
    sar "Hi, my name is Sarah and this is our han....\"grocery store\", but we buy and sell a little of everything here."
    mc_thought "man, she is even more beautifull when she is from a near distance."
    sar "And you are?"
    mc "Oh, Im sorry, hi my name is [player.name], nice to meet you."
    show sarah half normal2
    sar "Oh, so this is the [player.name] that I head so much about hmmm?"
    mc_thought "She heard about me?"
    menu:
        "What did you heard about me?":
            show sarah half normal3
            sar "Nothing special, just that there were a new young boy in town...thats about it."
        "Who told you about me?":
            show sarah half normal3
            sar "I...well, I dont remember."
        "How did you know about me?":
            sar "A business woman is always well informed"
    mc_thought "Why do I fell there is more to it?"
    mc "..."
    show sarah half normal
    sar "Sorry."
    sar "Ok, The truth is I work in the field with monica so...we like to talk."
    show monica half overall talking with dissolve:
            xpos 572 alpha 0.33 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    mc_thought "Indeed..."
    mc_thought "She is wearing clothes very similar to monicas."
    hide monica with dissolve
    mc "Oh, now I understand."
    sar "Anyway, this is our grocery store, so... are you looking for something to buy? Maybe a bouquet of flower to give to your loved one?" 
    mc "What?" with vpunch
    mc "No no...nothing like that"
    show sarah half normal2
    sar "Its ok, you can tell me....I wont tell monica, it can be our little secret."
    mc "The truth is..."
    menu:
        "I dont have a girlfriend":
            sar "Oh...thats so nic....a pity...thats a pity..."
            sar "Im sure you will find one"
        "I dont have a loved one yet":
            sar "Oh...not a problem dear, you will find it soon enough."
    mc "Well, thanks"
    mc "Anyway, I started working on the fields today... and monica told me I could come here and sell the flowers to make some money."
    show sarah half normal3
    sar "Oh so you will work on the fields with us too? Im so excited to work with you."
    mc_thought "No...im excited to work with you"
    sar "Well, In that case you can talk with little Debbie over there."
    show sarah half hands:
        matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    sar_shout "SHE IS MY DAUTHER!" with vpunch
    mc_thought "Wait...what?"
    show sarah half hands2
    sar_shout "SO TREAT HER WELL!" with vpunch
    mc_thought "What the hell? I can fell her intent to kill me all the way from here."
    show sarah half hands3:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    sar "for your own good."
    show sarah half normal3:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    sar "Be kind, she also is on her first day at work. I have to go now, bye."
    hide sarah with dissolve
    mc_thought "Man...she was very kind and all of sudden she went full psycho killer..."
    mc_thought "And somehow I know she is not kidding..."
    mc_thought "I better treat her daugher with respect."
    $ sarah.revealed = True
    return

label grocery_store_on_exit:
    if debbie_first == True:
        mc "I came to sell the flowers, I should at least talk with the girl to see how it works"
        return False
    return True

label talk_to_debbie_store:
    $ debbie.revealed = True
    scene grocery in
    if debbie_first == False:
        show debbie half grocery
        deb "Hi [player.name], how are you?"

    if debbie_first == True:
        $ debbie_first = False
        # show debbie half grocery
        show debbie half grocery shy
        deb "Hi...."
        mc_thought "Is she still sad about what just happened?"
        menu:
            "Are you ok?":
                mc "Hey...are you ok?"
                deb "It is...its just...what a shame you see us in that situation."
            "Is everything alright?":
                mc "Hey...is everything alright?"
                deb "It is...its just...seriously...what a shamefull situation you just saw."
        mc "Its alright nothing to be ashamed of, you were just helping your mom"
        deb "yes, I guess so..."
        menu:
            "That was impressive":

                mc "Besides, that was very impressive, I mean, your Mom doesnt seem to be someone easy to lift."
            "You are a good daugher":
                mc "Besides, you conquered your fears, even you didnt want to do it, you did because you are a good daugher."
        show debbie half grocery5
        deb "You think soooo? Thank you, thank you a lot."
        deb "You know, its very important to me that I be a good daugher to my mom."
        mc "Is that so?"
        show debbie half grocery6
        deb "Yes, yes it is, you see...me and my mom are not blood related. I mean you may have guessed by the color of our hairs."
        mc "Yet she seems to treat you very well doesnt she?"
        show debbie half grocery7
        deb "Yes, yes she does treat me very well, she is like an angel in my life."
        mc_thought "She is talking about Sarah...her mom, the way I talk about Monica."
        show debbie half grocery2
        deb "My mom died in an accident when I was 3 years old, and she is raising me as my mom ever since."
        show debbie half grocery7
        deb "Sarah is awesome!, but...as you saw, she can be overprotective some times, I think thats because she loves me."
        mc "Yes, I was scared back there for a second."
        show debbie half grocery6
        deb "But she is the best person I know, she is just the best."
        deb "Anyway...Im sorry, you must be here for business"
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
            deb "Yes, yes it is, you see...me Sarah my mom are not blood related. I mean you may have guessed by the color of our hairs."
            show debbie half grocery2
            deb "My mom died in an accident when I was 3 years old, and Sarah is raising me as my mom ever since."
            deb "So, she is like my mom now."
            mc "Yet she seems to treat you very well doesnt she?"
            show debbie half grocery7
            deb "Yes, yes she does treat me very well, she is like an angel in my life."
            mc_thought "She is talking about Sarah...her mom, the way I talk about Monica."
            show debbie half grocery6
            deb "Sarah is awesome!, but...as you saw, she can be overprotective some times, I think thats because she loves me."
            mc "Yes, I was scared back there for a second."
            show debbie half grocery5
            deb "But she is the best person I know, she is just the best."
        "Why work here?":
            mc "So...do you like working here?"
            show debbie half grocery2
            deb "No."
            mc "No?"
            show debbie half grocery5
            deb "Im sorry, let me explain, It was never my dream to work on my mom´s store"
            show debbie half grocery6
            deb "But if thats what she wants me to do, I will do it with a smile."
            mc "You really must love your mom dont you?"
            show debbie half grocery7
            deb "Yes, I really do."
        "About her parents":
            show debbie half grocery2
            mc "What happened with your parents?"
            deb "I...I dont know, the details, the only thing I know is that they died in an accident."
            mc "Im sorry."
            show debbie half grocery3
            deb "No need to, It was a long time ago."
        "Nothing, thanks":
            mc "An...nothing, thanks."
            return
    call talk_with_debbie_grocery
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
