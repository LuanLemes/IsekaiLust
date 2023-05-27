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
    mc_thought "(It has been a month since this door broke, I better get the right tools to fix it.)"
    return

label monica_kitchen_morning:
    if monica_morning_kitchen == True:
        mc_thought "I just talked to her."
        return
    $ monica_morning_kitchen = True
    if monica.phase == 3:
        show monica half sad1
        mon "Oh, good morning [player.name]."
        mc_thought "Monica seems so sad."
        menu:
            "Is there something wrong?":
                pass
            "You look sad, are you ok?":
                pass
        show monica half sad2
        mon "No, thats not, I mean, its nothing."
        mc_thought "(Maybe it has something to do with...)"
        menu:
            mc_thought "(Not sure I should talk about this with her, but if even the book says so...)"
            "Is this something to do with your husband?":
                pass
        show monica half sad3
        mon "..."
        mc_thought "She seems even more sad now."
        mc "Im sorry I didnt mean to..."
        show monica half sad1
        mon "Its ok..."
        mon "What happened is...He was a good husbad, until one day, he left."
        mc "Im so sorry."
        show monica half sad2
        mon "Dont be, I think the worse part of it is..."
        mon "You know, he never came to talk to me, he only left a note. After years together... A note."
        mon "Telling me that he was leaving-me."
        mc_thought "So, she doesnt know about the whole map thing."
        mc_thought "I think to this point he may be dead."
        $ monica.marital_status = "Single"
        mc "Omg mon, Im very sorry."
        show monica half sad3
        mon "As I said, dont be, All I can do now is look towards the future and forget the past."
        mc "You are right mom, you are right."
        mc "I know you probably got sarah at this point but...If you ever need somebody to talk."
        mc "Just know Im aways here for you."
        show monica half talking
        mon "Oh you are so sweet, thanks."
        mon "Please, sit and have a breakfast with me and the girls."
        mc "Ok mom."
        call girls_kitchen_morning
        return
    
    show monica half talking
    mon "Oh, good morning [player.name]."


    if renpy.random.randint(1,10) > 5:
        menu: 
            mon "So, are you going to show up on the Flower Fields today?"
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
        if player_inventory.item_exists(301) != -1 and breakfast_milk_bottle == False and ashley.phase == 2:
            # bottle on ashleys mouth scene
            show breakfast currel1 with dissolve
            scene
            show breakfast currel1 
            mon "Everything ok my little star?"
            show breakfast currel2 with dissolve
            ash "..."
            mc_thought "Why do I have a bad feeling about this?"
            mon "My little ash?"
            ash "Mom the meal is beautifull....really it is."
            ash "But..."
            ash "The milk..."
            ash "Why are we not having ANY milk?!"
            show breakfast currel3 with dissolve
            ash "I want milk mom!"
            ash "And as I said, this useless boy didnt recover any milk."
            menu:
                "Oh, I didnt, DID I?":
                    pass
            show breakfast currel12
            ash "What are you saying?" with dissolve
            mc "Im saying that I got the milk right here."
            ash "You are lying."
            mc "Oh, am I?"
            menu:
                "Show the bottle of milk.":
                    pass
            show breakfast currel14
            ash_shout "Shit!"
            show breakfast currel11
            lin "Mom what did she say?"
            mon "My star!, watch your mouth..."
            show breakfast currel12
            mc "Anyway."
            mc "I remember you saying that \"If I got any milk you would let me pour it in your mouth so...\"."
            show breakfast milk12 with dissolve
            ash "Hey...what are you doing?" with vpunch
            mc "Im only fufilling our agreement Ashley, or your word doesnt have any value?"
            mon "Oh my."
            ash "..."
            ash "You are an evil one you know that?"
            ash "..."
            show breakfast milk9 with dissolve
            ash "Fine!"
            ash "Do it at once."
            mc "If you say so."
            menu:
                "Pour the milk in her mouth":
                    pass
            show breakfast milk10 with dissolve
            mc "It will be a pleasure."
            mc_thought "Here it is Ashley, a little payback for the way you treat me."
            show breakfast milk3 with dissolve
            mon "Oh my little dauther!"
            show breakfast milk4 with dissolve
            lin "Cooooooooool!!!"
            ash "*Drinking*"
            mc "Just a little more."
            show breakfast milk12
            ash_shout "STOP SPEAKING WHILE YOU DO IT!" 
            hide breakfast
            show breakfast milk4:
                    xpos -212 yzoom 1.03 zoom 1.22


            lin_shout "DO IT AGAIN!" with vpunch
            hide breakfast
            show breakfast milk12
            ash "Shut up linda!"
            lin "Mooom."
            mon "Ashley, watch your mouth."
            mc "Yes ashley more milk and less words."
            ash "What did you say?!?!..."
            mc "Lets continue."
            ash "Arent we finished already?!!?" with vpunch
            mc "What? you only drank a tiny bit."
            ash "..."
            ash "Ok, go ahead."
            show breakfast milk5
            mc "Yes, all the way into your mouth."
            mc "Veeeeery goood."
            lin "Maaaaan, This is so fun!"
            show breakfast milk12
            ash_shout "Thats enough!" with vpunch
            mc "Wait, there is still a lot of milk!"
            hide breakfast
            show breakfast milk1:
                    xpos -32 zoom 1.18 
            ash "Im out of here!"
            hide breakfast
            show breakfast milk0
            lin "Best breakfast EVER!"
            $ breakfasted = True
            $ ashley_room_locked = False
            $ ashley.phase = 3
            return


        if monica.phase == 3:
            show breakfast currel1 with dissolve
            mon "Everything ok my little star?"
            show breakfast currel2 with dissolve
            ash "..."
            mc_thought "Why do I have a bad feeling about this?"
            mon "My little ash?"
            ash "Mom the meal is beautifull....really it is."
            ash "But..."
            ash "The milk..."
            ash "Why are we not having ANY milk?!"
            show breakfast currel3 with dissolve
            ash "I want milk mom!"
            ash_shout "I want milk!" with vpunch
            show breakfast currel4
            mon "I understand dear, we all want, but the stores are all out of milk for months."
            mon "I have an idea, Maybe we could have some juice."
            show breakfast currel5
            lin "Mon....I want milk too, I like it so much."
            mon "I like it too dear but just there isnt anywhere we can get milk."
            mc_thought "Geez, whats happening here? isnt there any milk in the entire city?"
            menu:
                "Ha... whats happening really?":
                    pass
                "Mon, whats happening?":
                    pass
            show breakfast currel6
            mon "Oh sweet, you dont know do you?"
            mon "There is some months since the milk stock in the city is out."
            mc "I understand, is there something that I could do for helping?"
            show breakfast currel7
            ash_shout "Oh Yes [player.name] the \"Milk bringer\", as if a dumbass like you could do anything usefull here."
            mon "Dont be like that ash, [player.name], is your [mcash], and he is willing to help."
            show breakfast currel8
            lin "Yes sis, he found my bear and I bet that if he say so he can also find the milk."
            mc_thought "Well, this was unexpected."
            ash "He wont find anything."
            mc_thought "Maybe I could take some advantage of this situation."
            menu:
                "Wanna make a bet?":
                    show breakfast currel12
                    ash "What do you mean?"
                    mc "I mean, if I somehow manage to bring the milk back you will have to leave your door unlocked from now on."
                    ash "My door? why?"
                    mc "I dont know I just thought of something that would be important to you."
                    show breakfast currel11
                    ash "*laughs* If you mange to bring the milk better I would let you pour it in my mouth as if you were my owner."
                    ash "But we both know this is never going to happen because you are a good for nothing."
                    show breakfast currel13
                    mc "Is that so?"
                    ash "Yes it is."
                    ash "And what if you can´t manage to bring the milk back?"
                    mc "I will, so chosse whatever you want to."
                    show breakfast currel12
                    ash "If you dont manage to bring milk back you will have to clean my room every single day for an entire year."
                    mc_thought "Shit, she is so drastic."
                    ash "So [player.name] what will it be? will you accept or run?"
                    mc "I accept!"
                    show breakfast currel14
                    ash "Its a bet then."
            mc_thought "Shit...I have no idea of how to find this milk, I think the first thing I should do is.."
            mc_thought "{color=#FFAA00}To take a look at the grocery store and see if they have it.{/color}" with vpunch

            hide monica
            hide breakfast
            $ debbie.phase = 4
            $ monica.phase = 4
            $ breakfasted = True
            $ ashley.phase = 2
            return

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
    $ monica_sarah_water_first = False
    $ talked_to_girls = True
    hide monica_sarah
    return



