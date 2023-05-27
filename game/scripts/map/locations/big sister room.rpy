screen ashley_room():

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
    use top_screen()
    
label ashley_room:
    if ashley.phase < 10 and calendar.current_day_time != 1:
        show ashley room2
        ash "What the fuck are you thinking?"
        ash "My room is unlocked but that doesnt mean you are welcome here."
        mc "But I thought."
        ash "GET OUT!" with vpunch
        mc_thought "Damn, I have to pick a time where she is not in her room."
        mc_thought "{color=#FFAA00}Probably at noon{/color} when monica is at the flower field and ashley is usually out."
        call change_location_to("Hallway")
        return
    if ashley.phase <10 and calendar.current_day_time == 1 and monica.phase == 4:
        call investigate_map_at_ashley_room
        return
    return
    

label ashley_room_on_enter:
    if ashley_room_locked == True:
        $phrase = renpy.random.choice(["(The door is locked...)", "(why does she always leave the door locked?)"])
        mc_thought "[phrase]"
        return False
    return

label investigate_map_at_ashley_room:
    show ashley room3 with dissolve
    mc "Good, she is not here, now I can finally look for the map!"
    show ashley room4
    mc "Nothing here seems like a map to the witch." with dissolve
    mc "I have to look somewhere else."
    show ashley room6
    mc "Maybe one of those photos?" with dissolve
    mc "Didnt knew ashley liked to photograph."
    mc "No....doesnt seem like that either"
    show ashley room5
    mc "Maybe inside one of these books?"
    mc "Hmmmm..."
    scene black with Dissolve(1.0)
    mc "I will look inside every single one of them."
    show ashley room5 with dissolve
    mc "NOTHING!!!!?"
    mc "Damn...Im starting to think its not here..."
    mc "Just where is this then?"
    show ashley room3
    mc "Maybe its like...."
    mc "I dont really know."
    show ashley room7
    mc "Hm....is it ok to leave your panties on your bed like this?."
    mc "Now that Im thinking about it..."
    mc "Ashley isnt home, Monica isnt home either."
    show ashley room8
    mc "They are so cute even ashley being a living hell."
    mc "Maybe I could..."
    mc "you know.."
    mc "Just a little bit?"
    show ashley room11
    mc "Yes...I was needing something like that."
    mc "Nothing personal or anything..."
    mc "Just to get rid of this stress of course."
    mc "Oh I love this feeling."
    mc_thought "Wait..the house is empty, why am I hearing steps?"
    mon "Ashley are you th..."
    show ashley room14
    mon "OMG WHAT ARE YOU DOING?!?!!?" with vpunch
    mc "What?? Monica? but I thought you were at the flower field!"
    mc "Its...its nothing I was just..I was only...I was..."
    show ashley room17
    mc "Wait Monica dont get any closer"
    mon "...."
    show ashley room18
    mon "..."
    mon "I see it now..."
    show ashley room19
    mon "You were...."
    mon "You were masturbating because you saw ashley´s panties werent you?"
    mc "No....I ...I was only...I was.."
    mon "[player.name]...."
    mon "Look at you..."
    show ashley room21
    mon "Look at your....."
    mc "Ok..I was."
    mon "Just..."
    show ashley room19
    mon "Its ok..."
    mc "It is?"
    mon "I understand."
    mon "You are a man."
    show ashley room21
    mon "Man need to do ....han..these kind of things."
    mc "Then...can I continue?"
    mon "No you can´t."
    mon "This is a disrespect with ashley because she doesnt even know about it."
    mc "Ok Im sorry, I know, I will st..."
    show ashley room22
    mon "Do it looking at me instead."
    mc "What?!?"
    mon "Err....I said."
    mon "You can do it looking at me instead."
    mc_thought "Man...the way she is looking at my cock only makes it grow even bigger."
    mc "Monica, you doesnt seem to be very....you know, sure about it."
    mon "No, its ok, I can take it."
    mon "You can do it and I will watch as you do it."
    mc "Monica...are you sure?"
    mon "*swallow*...I am."
    mc_thought "In fact...thats not bad...is like a dream coming true."
    mc "Ok then."
    menu:
        "Masturbate to her":
            pass
    show ashley room28 with dissolve
    mon "..."
    mc "..."
    mon "Whats the problem?"
    mc "Thats nothing, there is no problem."
    mon "..."
    show ashley room29 with dissolve
    mc "Is just that..."
    mon "Am I not cute?"
    mc "Thats not it...Its just that...if you could.."
    mon "\"Could...?\""
    mc "Maybe...show me...something...more?"
    mon "You mean..."
    mon "Like that?"
    show ashley room35 with dissolve
    mc_shout "Holy shit!!"
    mon "What?"
    show ashley room36 with dissolve
    mc_shout "They are beautiful!!!" with vpunch
    mc "Yes, yes like that!"
    mon "He he, thanks [player.name]."
    mon "Now get to it then."
    menu:
        "Masturbate to her boobs.":
            pass
    show ashleyr handjob3 with dissolve
    mc "*moaning*"
    menu:
        "You are so beautiful.":
            mon "Thanks [player.name], I try to take care of myself."
        "Your boobs are so beautifull":
            mon "Thanks [player.name], Im glad you like them"
        "You are so cute":
            mon "Thanks [player.name], I try to take care of myself."
    mc_thought "This is crazy, Im masturbating in front of Monica."
    mc_thought "THE Monica."
    mc_thought "And she knows it."
    mc_thought "Also, the way she is looking at me, makes me excited."
    show ashleyr handjob4 with dissolve
    mc "Please keep looking at me while I do it."
    mon "Like that?"
    mc "Yes, Like that."
    mon "Got it."
    mc "*moaning*"
    mc_thought "I never imagined I would, do this in front of her."
    mc_thought "Like...never."
    mc_thought "Man...such beautifull boobs."
    mc "*moaning*"
    mon "Its ok, you can moan, I dont mind."
    mc "*moaning*"
    mc "Thanks."
    hide ashleyr
    show ashley room39 with dissolve
    mon "Wait, is that?...."
    mon "Cum?"
    show ashley room40 with dissolve
    mc "Yes."
    mc "Just a bit thought."
    mon "*heavily breathing*"
    mon "I understand."
    mon "I can fell the smell all the way here."
    mc "Can you?"
    mon "Yes.. At least I think I can."
    menu:
        "Get closer to her.":
            pass
    show ashley room48 with dissolve
    mon "What?"
    show ashley room43 with dissolve
    mc "I got closer so you can be sure about the smell"
    mon "I see."
    mc_thought "Man...its like she somehow is hipnotized by my dick."
    mon "Yes, I can definetily smell the cum from here."
    mon "Its so strong."
    show ashleyr handjob5 with dissolve
    mc "Look at me."
    mon "Looking."
    mc "Ah...*moaning* this feels so good."
    mon "Does it?"
    mc "Yes it does, you boobs are just the best."
    mon "Oh, you are so kind."
    show ashleyr handjob6 with dissolve
    mc "Ah..."
    mon "What dear what is it?"
    mc "I think Im....*moaning*"
    mon "What?"
    mc "I think im about to cum."
    mc "Can I cum on your boobs?"
    mon "What? my boobs?"
    mc "Yes!"
    mc "On your boobs, can I?"
    mon "Well..."
    mc "*moaning*"
    mon "Well I think..."
    mc "There is no time to think!"
    hide ashleyr
    show ashley room51 with dissolve
    mc_shout "Ahhh!!!!"
    mon_shout "OH MY!"
    show ashley room56
    mc "Sorry mon, I...I could´t hold myself."
    mon "Oh, how did you came so much?!?"
    mc "Im sorry thats your boobs."
    show ashley room58
    mon "My boobs?"
    mon "What do you mean?"
    show ashley room59
    mc "I dont know that just..."
    show ashley room60
    mc "They are too beautifull."
    show ashley room58
    mon "Thanks, I guess."
    mc "Oh, this was just too good!"
    show ashley room61
    lin "Heeeeyyyyy, someone in there?!?!?"
    lin "Mom is that you???"
    mon "Oh no thats linda!"
    show ashley room62
    mon "My boobs are full of cum"
    mc "What are we going to do?"
    mc "She can´t see you like that!"
    mon "I dont know."
    show ashley room63
    lin "Mooooom? Is it mom or Ashley?"
    lin "Can I come inside?"
    show ashley room64
    mon "This is bad."
    mc "..."
    mon "Very bad."
    show ashley room65
    mon "There is no way she can come in and see us like that."
    mon "I have to...get up."
    mc "But how are you going to celan yourself?"
    mon "I wont, I have to go."
    mc "Hey wait dont just get up like th..."
    show ashley room68
    mon "I have to."
    mon "Omg Im such a mess."
    mc "Yes you are full of cum."
    show ashley room69
    mon "I..."
    lin "Ok im going in."
    mon "I...I have to go like this"
    show ashley room70
    mon "Hey dear dont come in, Im going outside!"
    mc_thought "And she is going to meet Linda with her body covered in cum."
    show ashley room9
    mon "Hello my little star."
    lin "Hey mom."
    mon "What?"
    lin_shout "BEAR HUG!"
    mon "No dear no!"
    lin "Moooom you are all sticky? eeeeeew!"
    lin "What is this?"
    mon "Im sorry dear. I had a little glue accident just a while ago."
    lin "Hmmmm this glue smells goooooood!"
    mon "No dear dont do it!"
    lin "It tastes good too!"
    mon "Oh Dear."
    mc_thought "Oh Dear Indeed."
    $ monica.phase = 5
    return
    

    






    
    
    
    
    



    return
