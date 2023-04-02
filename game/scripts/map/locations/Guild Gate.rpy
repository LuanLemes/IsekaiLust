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
        "So this are the guild gates." 
        "I heard the guild was a big organization but man its much bigger then I imagined."

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
    mc "Hi there, My name is [player.name] and I would like to make the guild exam."
    mc "No...not like that....Hi there, Hi Im the great [player.name] and I would like to make the guild exam."
    mc "Too much?"
    mc "Hi there My name is [player.name] Im from another universe. I follow aphrodite."
    show makoto talking
    mc "Hi there My...."
    mak "Hi there."
    mc_thought "Fuck!!!" with vpunch
    mak "..."
    mc "So...My name is [player.name]..."
    mak "Nice to meet you [player.name], My name is Makoto."
    mc "....Nice to meet you too...Makoto."
    mc "And Im here to make...."
    mak "The guild exam right Sir?"
    mc "Yes, wait, how do you know that?"
    show makoto talking1
    mak "Nothing, just that, everyday lots of people like you came here."
    show makoto talking2
    mak "Just to take the guild exam and try to become a guild member."
    mc "Well, if lots of people come here means that most of them pass the test right?"
    show makoto talking3
    mak "In fact, usually 1 in 200 usually pass the test."
    mc "Whaaaaaaat?" with vpunch
    show makoto talking2
    mak "Hey, calm down, you can retake the test any number of times, so if you fail you can retry whenever you want Sir."
    mc "Ufff, good news at least."
    call makoto_menu
    return

label makoto_menu:
    menu:
        "I would like to take the exam right now.":
            $ makoto_info0 = True
            if makoto_first == True:
                $ makoto_first = False
                show makoto talking1
                mak "Good thing [player.name]. We can start your exam as soon as you pay for it."
                mc "Nice! wait...pay?"
                show makoto talking2
                mak "Yep, Oh, you dont know? There is a value to pay in order to take the test."
                mc "I see."
                mc "How much to take the test?"
                show makoto talking3
                mak "That would be {color=#FFAA00} 50 coins {/color} sir."
                mc_shout "{color=#FFAA00} 50 coins?!?!!? {/color}"
                show makoto talking2
                mak "Yes, The Guildmaster said this could be a good fount of income for the guild."
                mak "And also that also would test would also be a test of will."
                mc "I understand, It makes sense in a way."
                mc_thought "Well, at least im working at the flower fields now."
                call time_next
                call makoto_menu
            else:
                menu:
                    "Pay 50 coins (wait for the next updates)" if player.money >= 50:
                        "This will be ready on the next updates."
                        $ player.money -= 50
                        pass
                    "I dont have the money yet":
                        mak "Its alright you can came back when you get the money."
                        call makoto_menu
                    

        "How is this guild exam?::makoto_info0":
            $ makoto_info1 = True
            mc "How exacly is this exam that only one in two hundred pass?"
            show makoto talking1
            mak "Well the exam change from time to time depending on what the current guild master decides."
            show makoto talking2
            mak "But right now is basicly its a fight one on one with me."
            mc_shout "Whaaaaaaaat?"
            mc_thought "Only one in each two hundred win a fight with this girl?"
            mc_thought "I mean....She doesnt seem that tough."
            show makoto talking3
            mak "What?"
            mc "Hmmmmmmmm."
            show makoto talking1
            mak "I may not be big. But fighting its not only about strengh but about strategy, techniche and experience as well."
            mc "Only one in two hundred win in a fight one on one with you?"
            mak "In fact you dont need to win, I mean its not a fight to death or anything, there are many pass the exam."
            menu: 
                "There are many ways to pass the exam."
                "Many ways to pass the exam?":
                    pass
                "Ways?":
                    pass
            show makoto talking2
            mak "Yes, Or knokout immobilize-me are the hard ways I would say."
            mc "What is the easy way?"
            show makoto talking3
            mak "It may change from person to person but...."
            show makoto talking2
            mak "If you can make me surrender, or make me recognize your powers or even just say you passed its already ok."
            call makoto_menu
       
        "Can I use weapons?::makoto_info1":
            $ makoto_info2 = True
            mc "Can I use any weapons or is like a barefistfight?"
            show makoto talking1
            mak "You can use any means you want, like swords, arrows, shields, spear arrows."
            show makoto talking2
            mak "Even magic.... well that is a rare one nowdays."
            mc "Hmmmm."
            menu:
                "Witch weapon do you fight with?":
                    show makoto talking2
                    mak "I fight with a wooden sword."
                    mc "Wooden sword?"
                    show makoto talking3
                    mak "Yes, you see Im an apprentice swordsman."
                    mak "And my master told me not to use a real sword for this task."
                    mc "So you manage to win these matches with only an wooden sword?"
                    show makoto talking1
                    mak "Pretty much, but I train a lot you see."
                    show makoto talking2
                    mak "Also, my master told me this would be a good oportunity to train my skills."
                    mc "So Im very excited about fighting you whenever you want Sir!"
                "Witch weapon is your favorite?":
                    show makoto talking3
                    mak "My favorite weapon?"
                    mc "Yes."
                    show makoto talking2
                    mak "I like the big and long ones."
                    mc_thought "That was....."
                    mc "Big and long?"
                    show makoto talking1
                    mak "Yes, like my master´s sword"
                    show makoto talking2
                    mak "You should see, once I saw a giant fall with a single blow."
                    show makoto talking3
                    mak "My is dream to be a great warrior just like master."
            mak "You can use any weapon, the guild master instructed me to use this wooden sword."
            call makoto_menu
        "Leave ::makoto_info2":
            mc "I will came back another time, thank you."
            mak "See ya Sir!"
            hide makoto
            return
    return

label guild_gate_on_exit:
    if makoto_first == True and calendar.current_day >= 1 and calendar.current_day_time <= 1:
        show makoto overlay idle
        mc_thought "I think I should at least try to talk to the guard before I leave."
        return False
    return