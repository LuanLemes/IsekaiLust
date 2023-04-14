screen guild_gate():

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
            hovered SetVariable("focus_location", "Village")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Forest Wall")
        text "Village" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"
        if calendar.current_day_time < 2 and calendar.current_week_day != 0 and calendar.current_week_day != 6 and calendar.current_day > 0:
            imagebutton auto "overlays/makoto overlay %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("makoto_guild_gate")
    use top_screen()
    

label guild_gate:
    if makoto_first and calendar.current_day >= 1 and calendar.current_day_time <= 1:
        show makoto overlay idle
        mc_thought "So these are the guild gates." 
        mc_thought "I heard the guild was a big organization but man it's so much bigger then I imagined."

    window hide
    return

label makoto_guild_gate:
    if makoto_first == True:
        $ makoto.revealed = True
        call makoto_first
        return
    show makoto talking
    mak "So, are you ready to take the guild exam now?"
    call makoto_menu
    return

label makoto_first:
    show makoto overlay idle
    mc "Hi there, My name is [player.name] and I would like to take the guild exam."
    mc "No...not like that....Hi there, Hi I'm the great [player.name] and I would like to take the guild exam."
    mc "Too much?"
    mc "Hi there My name is [player.name] I'm from another universe. I follow aphrodite."
    show makoto talking
    mc "Hi there my...."
    mak "Hi there."
    mc_thought "Fuck!!!" with vpunch
    mak "..."
    mc "So...my name is [player.name]..."
    mak "Nice to meet you [player.name], My name is Makoto."
    mc "....Nice to meet you too...Makoto."
    mc "And I'm here to take...."
    mak "The guild exam right sir?"
    mc "Yes, wait, how do you know that?"
    show makoto talking1
    mak "Nothing, just that, everyday lots of people like you come here."
    show makoto talking2
    mak "Just to take the guild exam and try to become a guild member."
    mc "Well, if a lot of people come here, then that must mean that most of them pass the test, right?"
    show makoto talking3
    mak "In fact, usually 1 in 200 usually pass the test."
    mc "Whaaaaaaat?" with vpunch
    show makoto talking2
    mak "Hey, calm down, you can retake the test any number of times, so if you fail you can retry whenever you want sir."
    mc "Ufff, good news at least."
    hide makoto
    call makoto_menu
    return

label makoto_menu:
    show makoto talking2
    menu:
        "I would like to take the exam right now.":
            $ makoto_info0 = True
            if makoto_first == True:
                $ makoto_first = False
                show makoto talking1
                mak "Sure thing [player.name]. We can start your exam as soon as you pay for it."
                mc "Nice! wait...pay?"
                show makoto talking2
                mak "Yes, that's right. Oh, you didn't know? There is a fee to take the test."
                mc "I see."
                mc "How much do you need to pay in order to take the test?"
                show makoto talking3
                mak "That would be {color=#FFAA00} 50 coins {/color} sir."
                mc_shout "{color=#FFAA00} 50 coins?!?!!? {/color}"
                show makoto talking2
                mak "That's correct. The Guildmaster said that this would be a good source of income for the guild."
                mak "The Guildmaster also mentioned that the test would be a test of one's willpower."
                mc "I understand, It makes sense in a way."
                mc_thought "Well, at least I'm working at the flower fields now."
                call time_next
                call makoto_menu
            else:
                menu:
                    "Pay 50 coins" if player.money >= 50:
                        if makoto_info2 == False:
                            mak "I see you are very rich indeed, but Please listen to the rest of informations about the test before taking it."
                            call makoto_menu
                        if witch_talk_first == False:
                            $ player.money -= 50
                            mak "And are you going to fight without using any weapons?"
                            mc "I did some karate training when I was younger, so I think I will be ok."
                            mc_thought "I mean that's just a girl and a piece of wood after all."
                            show makoto before fight
                            mak "Well then."
                            mak "Since you are so \'prepared\'."
                            mak "Lets see what you are capable of!"
                            jump makoto_test
                            return
                        if witch_talk_first == True:
                            mc "I should get stronger before taking the test again."
                        call makoto_menu
                    "I dont have the money yet":
                        call makoto_menu
                    

        "How difficult is this guild exam?::makoto_info0":
            $ makoto_info1 = True
            mc "How difficult is this exam that only one in two hundred pass?"
            show makoto talking1
            mak "Well the exam changes from time to time depending on what the current guild master decides."
            show makoto talking2
            mak "But right now it’s basically a one on one fight against me."
            mc_shout "Whaaaaaaaat?"
            mc_thought "Wait, did she just say that only one out of every two hundred people can win a fight against her"
            mc_thought "I mean....she doesn't seem that tough."
            show makoto talking3
            mak "What?"
            mc "Hmmmmmmmm."
            show makoto talking1
            mak "I may not be big, but fighting isn't just about strength. It's also about strategy, technique, and experience."
            mc "Only one in two hundred win in a fight one on one with you?"
            mak "In fact you don't need to win, I mean it's not a fight to death or anything, there are many ways to pass the exam."
            menu: 
                mak "There are many ways to pass the exam."
                "Many ways to pass the exam?":
                    pass
                "Ways?":
                    pass
            show makoto talking2
            mak "Yes, I would say that knocking me out or immobilizing me would be the hard way.."
            mc "What is the easy way?"
            show makoto talking3
            mak "It may change from person to person but...."
            show makoto talking2
            mak "Well, if you can make me surrender, or make me acknowledge your powers, then that's good enough for me."
            call makoto_menu
       
        "Can I use weapons?::makoto_info1":
            $ makoto_info2 = True
            mc "Can I use any weapons or is it like a barefistfight?"
            show makoto talking1
            mak "You can use any means you want, like swords, arrows, shields, spear arrows."
            show makoto talking2
            mak "Even magic.... well that is a rare one nowadays."
            menu:
                mc "Hmmmm."
                "Which weapon do you fight with?":
                    show makoto talking2
                    mak "I fight with a wooden sword."
                    mc "Wooden sword?"
                    show makoto talking3
                    mak "Yes, you see I'm an apprentice swordsman."
                    mak "And my master told me not to use a real sword for this task."
                    mc "So you manage to win these matches with only a wooden sword?"
                    show makoto talking1
                    mak "Pretty much, but I train a lot you see."
                    show makoto talking2
                    mak "Also, my master told me this would be a good opportunity to train my skills."
                    mc "So I'm very excited about fighting you whenever you want sir!"
                "Which weapon is your favorite?":
                    show makoto talking3
                    mak "My favorite weapon?"
                    mc "Yes."
                    show makoto talking2
                    mak "I like the big and long ones."
                    mc_thought "That was....."
                    mc "Big and long?"
                    show makoto talking1
                    mak "Yes, like my master's sword"
                    show makoto talking2
                    mak "You should see, once I saw a giant fall with a single blow."
                    show makoto talking3
                    mak "My dream is to be a great warrior just like my master."
            mak "You can use any weapon, the guild master instructed me to use this wooden sword."
            call makoto_menu
        "About the witch::witch_talk_first":
            call makoto_witch_talk
            call makoto_menu
        "Leave ::makoto_info2":
            mc "I will come back another time, thank you."
            mak "See ya sir!"
            hide makoto
            return
    return

label guild_gate_on_exit:
    if makoto_first == True and calendar.current_day >= 1 and calendar.current_day_time <= 1:
        show makoto overlay idle
        mc_thought "I think I should at least try to talk to the guard before I leave."
        return False
    return

label makoto_test:
    scene black with dissolve
    mc_thought "Time to enter the guild."
    menu:
        mak "Prepare yourself!"
        "I'm born ready.":
            pass
        "Okay!":
            pass
    scene makoto test2 with dissolve
    mc_thought "Well, I wasn't expecting that."
    mc_thought "When she picked that sword, she really changed."
    show makoto test3
    mc_thought "That's clearly not the same cute makoto."
    mc_thought "That was talking to me moments ago."
    show makoto test2
    mc_thought "I mean..."
    camera:
            pos (4, -355) zoom 1.76 
    mc_thought "Look at her expression."
    mc_thought "It’s like she is ready to kill me at any moment."
    mc_thought "I mean.. we haven't even started yet but..."
    call camera_reset
    show makoto test6
    $ side_image_activated = False
    mak "Are you afraid [player.name]?"
    mc "What?"
    menu:
        mak "I said. \'Are you afraid?\'"
        "Of course not":
            mc "Of course not, I think I can do this with one hand behind my back."
            mak "Oh so you are THAT confident then?"
            mak "Good I like it, I wish you the best of luck."
        "I don't think I am":
            mc "No, I don't think I am."
            mak "Really?"
            mc "Really."
        "Ok, maybe a little.":
            mc "I am a little. But I'm going to win this fight even so."
            mak "That is good, master always said you have to face your fears."
    $ side_image_activated = True
    mak "Anyway, it's about time we start."
    show makoto test2
    mc "I agree."
    mc_thought "No I don't."
    mc_thought "Ok, she is just a girl with a piece of wood right?"
    mc_thought "I must remember my karate classes."
    show makoto test4
    mc_thought "Damn!"
    mc_thought "I feel like if I go anywhere near her she will take me down for sure."
    window hide
    scene
    show makoto test1
    mc_thought "This stance of hers."
    mc_thought "It's like she is ready for anything."
    mc_thought "Even more important than that."    
    mc_thought "EVEN MORE IMPORTANT THAN THAT!"
    scene
    show makoto test1:
        subpixel True 
        pos (0, 0) zoom 1.0 
        linear 0.03 pos (-1500, -1332) zoom 3.81 
    with Pause(0.3)
    show makoto test1:
        pos (-1500, -1332) zoom 3.81 
    mc_thought "DAMN I WISH I COULD SMACK THAT ASS!!!" with vpunch
    mc_thought "I WANT IT SO BADLY!!" with vpunch
    mak "So are we going to fight or?"
    hide makoto
    show makoto test7
    mc_thought "This is not time for that..."
    mc_thought "Focus, focus I have to focus."
    mc_thought "If I don't make the first move then she will."
    mc_thought "I have to make the first move!!!"
    show makoto test8
    menu:
        mc "I HAVE TO MAKE THE FIRST MOVE!!!."
        "!MEGA PUNCH!":
            pass
    show makoto test9
    mc_shout "OKAY THEN!!"
    show makoto test10
    mc_shout "PREPARE YOURSELF!"
    show makoto test13
    mak_shout "Yes sir!" with vpunch
    show makoto test11
    mc_thought "This is my!!!"
    show makoto test14
    mc_shout "THIS IS MY SPECIAL MOVE!"
    camera:
            xpos -915 zoom 2.19 
    mc_thought "Lady Aphrodite, lend me your powers!"
    call camera_reset
    show makoto test12
    mc_shout "Here!!"
    show makoto test15
    mc_shout "I...."
    show makoto test16
    mc_shout "GO!" with vpunch
    mak "..."
    mc_thought "I think I..."
    show makoto test17
    mc_thought "I think got too excited.."
    show makoto test19
    mc_thought "Way too excited..."
    mc_thought "Oh man."
    show makoto test18
    mc_thought "I'm going to die."
    mc_thought "I need to think of something fast."
    show makoto test22
    mak "My turn SIR!"
    mc_thought "Already?"
    mak "Blue Lotus Style!"
    show makoto_slash with vpunch
    mak_shout "PURGATORY SHIKAKU!" with vpunch
    scene makoto test29
    mc_thought "What happened?"
    mc_thought "Did she hit me?"
    mak "I told you it's about technique and strategy."
    mc "Ah.... the pain is so..."
    show makoto test30 with dissolve
    mc "I think I will....."
    mak "[player.name]?"
    mc "I think I will....."
    mak "[player.name]."
    show makoto test31 with dissolve
    mak_shout "[player.name]!!!"
    scene black with Dissolve(2.0)
    scene makoto test33 with Dissolve(2.0)
    mak "Oh [player.name] thank heavens you are alive!"
    menu:
        mak "..."
        "What?":
            pass
        "How?":
            pass
        "When?":
            pass
        "Why?":
            pass
    mak "Calm down."
    mak "We were fighting and you passed out."
    mc "I passed out?"
    mak "Yes you did."
    mc "I see that...but..."
    show makoto test34
    mc "Why are you on top of me?" with vpunch
    show makoto test35
    mak "Well I...I.."
    mak "I got worried and..."
    mak "So I..."
    mak "So I..... you see."
    scene black
    show makoto test41
    mc_thought "Since Aphrodite gave me that book this kind of situation is happening time and time again."
    mc_thought "Also since she gave me that book I can't stop thinking about girls."
    mak "....because you see my sword can't cut but she can..."
    show makoto test36
    mc_thought "I don't even want to know what her explanation is..."
    mc_thought "She is sitting on me and..."
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        linear 0.25 pos (-727, -1173) zoom 2.18 
    with Pause(0.26)
    camera:
        pos (-727, -1173) zoom 2.18 
    mc_thought "Damn her ass is so beautiful!." with vpunch
    call camera_reset
    show makoto test39
    mak "...and then I thought, Is he dead? So I ran to see if......"
    camera:
            pos (-991, -958) zoom 2.26 
    mc_thought "She is still talking. She is so close."
    mc_thought "My dick is going hard and I can’t stop it, even if I want to."
    call camera_reset
    show makoto test36
    mc_thought "The pain is so strong it\'s making me dizzy."
    mc_thought  "She should’ve known that would happen if she sat on top of a man like that."
    mc_thought "She almost cut through me with that wooden sword."
    mc_thought "And right now all I want to do is go through her with my dick."
    mc_thought "Since I can't do that yet, here is the second best thing."
    mc_thought "This is the payback Miss Makoto."
    show makoto test40 with vpunch
    mc_thought  "Enjoy the show."
    mak "Wait what is this?"
    mc_thought "Now she feels it, my dick is touching her pussy, such a nice feeling."
    mc_thought "The best part of it is that it is \'totally by accident\'."
    show makoto test37
    mak "[player.name] what is this?"
    mc_thought "The feeling of my dick touching her is just so good!"
    mak "[player.name]..."
    mc_thought "She will get up any moment now."
    menu:
        mc_thought "Do I even have to say something?"
        "Say nothing":
            mc "..."
        "Say something":
            mc "Makoto I.."
    mak "..."
    mc_thought "She didn't say a thing..."
    mc_thought "And she didn't get up either."
    show makoto test38
    mc_thought "Wait...is she..looking at me?"
    mc_thought "She is looking at me!"
    mc_thought "She is looking at me while feeling my dick between her legs!!"
    mc_thought "This is just too perfect."
    mc_thought "Wait."
    show makoto test40
    mc_thought "Maybe, maybe it's a signal..."
    mc_thought "Maybe it's time for me to take action."
    menu:
        mc_thought "She gave me all the signs!"
        "Smack her ass!":
            pass
        "Slap her ass!":
            pass
    mc_thought "I will go for it."
    show makoto test44
    mc_thought "It's now or never!" with vpunch
    mak "Wait [player.name]."
    show makoto test45 with dissolve
    mak "Not now, not yet."
    mc "What? why?"
    show  makoto test46 with dissolve
    mc_thought "Ohhh maaaaan she got up."
    mc_thought "Why did she get up in a moment like this?"
    mc "Makoto why did you get up?"
    mak "I...."

    mak "I........"
    mak "[player.name] you...are..."
    mak "[player.name] You need to get {color=#eca2a2ff}{b}stronger!{/b}{/color}." 
    mak "You need to win this fight!"
    mc_thought "She is not making any sense!"
    mak "Get up..."


    mc "Why?"
    mak "Get up and talk with me."
    mc "..."
    show  makoto test47 
    mak_shout "Just do it ok?!"  with vpunch
    mc "Gezz no need to scream ok?"
    mak "..."
    scene guild gate morning
    show makoto looking dick
    menu:
        "Im up":
            mc "I'm u...."
        "Ok what is it?":
            mc "Ok wha...."
        "What do you want?":
            mc "What d...."
    mak "You didn't pass the test."
    mc "I know."

    show makoto looking dick2
    mak "But you have a very b...."
    mc_thought "Is she...staring at my dick?"
    mak "Could you please....put that thing away?"
    show makoto looking dick3
    mc "Sorry makoto, it has a mind of its own."
    mak "Can you at least...cover it with your hands?"
    menu:
        mak "Can you at least...cover it with your hands?"
        "Ok, I’m sorry (Cover it)":
            mc "I'm sorry, I will at least cover it."
            show makoto looking dick5
            mak "Thank you."

        "But you want to look at it (Don't cover it)":
            mc "Why would I hide if you like to look at it so badly?"
            show makoto looking dick4
            mak "I don't."
            mc "..."
            show makoto looking dick5
            mak "I don't!"
    mak "Anyway... as I was saying."
    show makoto looking dick4
    mak "But you have a very {color=f7cfcfff}{b}BIG!{/color}{/b}"
    mak "Talent."
    show makoto looking dick5
    mc "I see."
    mc "I thought I could but, it seems I can’t be an adventurer after all."
    mc "Look, Makoto, you were only doing your job, no hard feelings ok?"
    mc "I'm going to go back to the flower fields then."
    show makoto looking dick4
    mak "Wait."
    mc "What is it?"
    show makoto looking dick3
    mak "Just, give me a second to clear my mind ok?"
    mc "Ok."
    # show makoto talking
    scene black with dissolve
    "Some minutes later."
    scene guild gate morning
    show makoto talking with dissolve
    mak "Ok now as I was saying."

    mak "There is a legend about a witch."
    call makoto_witch_talk
    return
    
label makoto_witch_talk:
    scene guild gate morning
    show makoto talking 
    menu:
        "Witch?":
            show makoto talking1
            $ witch_talk = True
            mak "Since I was a little girl people have told the legend of a big witch that lived here in this city long ago."
            mak "As far as I know she was a good person and one the most powerful members of the guild."
            show makoto talking2
            mak "If not the most powerful member in the guild."
            show makoto talking3
            mak "People say she even had her own statue."
        "Why are you telling me about her?::witch_talk":
            $ why_tell_witch = True
            show makoto talking3
            mak "She was famous for helping weak people to get stronger."
            mc_thought "She just called me weak, it's true but it hurts."
            show makoto talking2
            mc "I see, do you think maybe she could help me to get stronger and then enter the guild?"
            mak "That's exactly what I was thinking."
            show makoto talking1
            mak "Then you could enter the guild!"
        "Is this witch in the guild now?::why_tell_witch":
            $ is_witch_in_guild = True
            show makoto talking1
            mak "No it is said that one day she decided to leave the path of fame."
            show makoto talking2
            mak "So she destroyed her own statue and all the records about her."
            show makoto talking3
            mak "People say she went to live somewhere {color=#fc89ce} in the forest {/color} but no one knows where."
            mc "Somewhere in the forest!?"
            mc "As far as I know this forest is giant and very dangerous even for some adventurers."
            show makoto talking1
            mak "I know but don't you want to become an adventurer?"
            mc "Yes I do."
        "Where is she?::is_witch_in_guild":
            $ is_she_in_the_guild_now = True
            $ where_witch = True
            show makoto talking2
            mak "No one knows for sure, since it has been at least 50 years since she left the city."
            mc "50 years?!?! As far as I know she might be dead by now."
            show makoto talking1
            mc "And I'm not sure that an old hag would be a good mentor."
            mak "I know, but here is the thing."
            # conditional
            if witch_talk_first == False:
                show makoto talking3
                mak "I mean.."
                menu:
                    mak "Can you keep a secret?"
                    "Yes":
                        pass
                    "Of course":
                        pass
            show makoto talking2
            mak "I have a friend that works in the guild library sir."
            show makoto talking1
            mak "She once told me that recently two of the guild researchers said they could make a map to her location."
            mc "So, there is a map?!?"
            show makoto talking3
            mak "Well, there should be..."
            mc "\"there should be?\" What do you mean by \"There should be?\""
            show makoto talking1
            mak "Well, you see, the two adventurers that started to draw the map were told by one of the high rank members of the guild that..."
            mc "That?"
            show makoto talking2
            mak "If the witch is alive her privacy should be respected. therefore no map should be drawn."
            show makoto talking3
            menu:
                mak "And they had to hand over all their research to the guild."
                "So there is no hope after all.":
                    show makoto talking1
                    mak "Maybe yes maybe not."
                    pass
                "Shit! why did they do that?":
                    show makoto talking1
                    mak "I don't know. Maybe they are respecting the witch privacy?"
                    pass
            mc "..."
            show makoto talking2
            mak "Anyway. Not everybody knows but, the researchers continued to draw the map secretly."
            show makoto talking3
            mak "The guild discovered and was able to arrest one of them."
            mc "And the other?"
            show makoto talking1
            mak "The other one was able to run away."
            mc "Did he have the map?"
            show makoto talking2
            mak "No one knows. guild members searched his house but found nothing."
            mc "Still dont get why you are telling me this stuff."
            show makoto talking3
            mak "Well, the researcher that was able to run away was..."
            mc "Was?"
            show makoto talking1
            mak "Monica´s Husband."
            mc_shout "MONICA´S HUSBAND?!?!" with vpunch
            show makoto scared1
            mak "Please don't scream, not many people know about this sir."
            mc "Sorry about that."
            mc "She knows about that?"
            show makoto scared2
            mak "I dont think she does, Most of people inside the guild dont know about it."
            mc_thought "So monica doesn´t know a thing?"
            mak "So, my theory is that till this day the map may be in the same house you are living in right now."
            mc "I see..."
            mc "Well, I think I will take a look in the house and see if I find such a map."
            if witch_talk_first == False:
                $ witch_talk_first = True
                show book shining with dissolve:
                        xpos -345 
                boo "Go to Lindas bedroom and ask her about the map."
                mc_shout "It speaks!?!?!!??" with vpunch
                $ linda.book_phrase = "Ask about the map (bedroom Night)."
                $ makoto.book_phrase = "0"
                show makoto scared1
                mak "What? what speaks?"
                mc "Just curious if the map speaks about the path to the witch. that's it."
                mak "I see...well, yes it is a map after all."

        "Leave::is_she_in_the_guild_now":
            mc "I understand, thank you for the information."
            hide makoto
            return  
    call makoto_witch_talk



image makoto_slash:
    animation
    "guild/makoto test22.webp" with vpunch
    pause 0.07
    "guild/makoto test22.webp"
    pause 0.07
    "guild/makoto test23.webp"
    pause 0.07
    "guild/makoto test24.webp"
    pause 0.07
    "guild/makoto test25.webp"
    pause 0.07
    "guild/makoto test26.webp"
    pause 0.07
    "guild/makoto test27.webp"
    pause 0.07
    "guild/makoto test28.webp"
    pause 0.1
return

