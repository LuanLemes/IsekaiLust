label input_characters_relations:

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    "These three girls are {color=#ff67d1}Monica{/color}, {color=#ff67d1}Ashley{/color} and {color=#ff67d1}Linda{/color}, (Mother and her daughters), they will live with you during the game, but what are they to you?"
    hide monica
    show monica:
        pos (-276, 10) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    $ monmc = renpy.input("{color=#ff67d1}Monica{/color} (left one) is your (default landlady)?", length = 17, default = "landlady" )
    $ mcmon = renpy.input("And you are her? (default tenant)", length = 17, default = "tenant")

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide ashley
    show ashley:
        xpos 16
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    
    $ ashmc = renpy.input("{color=#ff67d1}Ashley{/color} (Middle one) is your?", length = 17, default = "friend" )
    $ mcash = renpy.input("And you are her (default friend)", length = 17, default = "friend" )

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide linda
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93

    $ linmc = renpy.input("{color=#ff67d1}Linda{/color}  (Right one) is your(default friend?)", length = 17, default = "friend" )
    $ mclin = renpy.input("And you are her? (default friend)", length = 17, default = "friend")

    $ monmc = str(monmc.lower())
    $ mcmon = str(mcmon.lower())

    $ ashmc = str(ashmc.lower())
    $ mcash = str(mcash.lower())

    $ linmc = str(linmc.lower())
    $ mclin = str(mclin.lower())


    hide monica
    show monica:
        pos (-276, 10) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    "So {color=#ff67d1}Monica{/color}  is your {color=#ff67d1}[monmc]{/color} and you are her {color=#ff67d1}[mcmon]{/color}."

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide ashley
    show ashley:
        xpos 16
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    "{color=#ff67d1}Ashley{/color} is your {color=#ff67d1}[ashmc]{/color} and you are her {color=#ff67d1}[mcash]{/color}."

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide linda
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
    "And {color=#ff67d1}Linda{/color} is your {color=#ff67d1}[linmc]{/color} and you are her {color=#ff67d1}[mclin]{/color}? Is that right?"

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    menu:
        "Is that right?"
        "Yes":
            $ monica.role = monmc
            $ ashley.role = ashmc
            $ linda.role = linmc
            $ monica.role = str(str(monmc).capitalize())
            $ linda.role = str(str(linmc).capitalize())
            $ ashley.role = str(ashmc).capitalize()
            "Alright."
            menu:
                "Skip intro?"
                "Skip the intro":
                    $ aphrodite.revealed = True
                    scene black
                    jump awake_at_home
                "Don’t skip the intro":
                    pass
            jump prologue
        "No(I want to try again)":
            "Let's fix that then."
            jump input_characters_relations
    return

label start_2:
    # scene temp_bed
    call input_player_name
return

label active_quick:
    $ quick_menu = True
    return

label deactive_quick:
    $ quick_menu = False
    return







label prologue:
    show sky background 
    with dissolve
    mc "Who am I again?"
    mc "Well...the thing is...I used to live in a world pretty much like yours."
    mc "I used to be a nerdy boy in my previous life, an average guy who had no luck with girls.."
    mc "I never really stood a chance because the girls always seemed to prefer the popular types."
    scene kiss bg with dissolve
    mc "Despite that, one day, I summoned up the courage and decided to buy a hentai game."
    mc "This one....{b}{color=#fc89ce}(Chronicles of Aphrodite){/color}{/b}....this one, this one should be good."
    mc "Her alluring image on the front cover immediately caught my attention, and I found her incredibly attractive."
    scene black with dissolve
    mc "Anyway, as soon as I got home, I began playing the game."
    window hide
    show aphrodite world with dissolve
    pause (1.0)
    mc "Man I like this game already, she's hot!!!"
    aph "[player.name]."
    aph "[player.name] I'm the Great Goddess Aphrodite!"
    aph "I'm in this game to make an exclusive invitation to you"
    aph "Do you want to become the Great Goddess Aphrodite's powerful champion, and embark on an amazing adventure filled with action and sex?"
    mc "Of course!!! I mean..... who would ever say no to such a question?"
    mc "And I wonder...till this day...why..why did I click yes?!!"
    scene black with dissolve
    mc "I don't know what kind of magic was in that game."
    scene tavern bg with fade
    mc "Because I ended in a world full of fantasy and magic"
    mc "But I didn't know anyone in this other world, I didn't have any help or family. I was homeless, it was really awful."
    mc "I wasn't powerful, I didn't become a powerful champion of the Goddess and I sure as hell didn't have sex till this day!"
    scene tavern bg 2 with fade
    pause (1.5)
    mc "There were times when I had to resort to eating spoiled food from others just to avoid starving to death. {color=#fc89ce} \"Please support the Patreon so that the developer doesn't end up in a similar situation.\" {/color}"
    mc "It went on like this for several months until I finally reached a breaking point.."
    scene tavern bg 3 with fade
    pause (1.0)
    mc "I realized that despite being around people every day, it was as if I didn't even exist to them."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I'm nothing in this world...nothing..."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.9)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I did my best to become a warrior, but I wasn't strong enough."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.8)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I tried many times to get into a guild but I didn't pass the test."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.7)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I even attempted to become a wizard, but my blood lacks any trace of magic."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I am even more of a loser in this world than I was on my own."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.35)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "The girls in this world don't seem to like me either."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "That's it...I give up."
    show tavern bg 3 with dissolve:
    mc "I'm going to close my eyes....and never open them again."
    scene black with Dissolve(2.0)
    mc "But then......"
    unk "Hey, are you ok?"
    mc "Of course I didn't listen....I thought it was all my imagination."
    unk "Hey!!!"
    mc "When I thought I was done for, when I thought it was my end."
    unk "Why don't you answer me?"
    mc "I felt two soft hands grabbing and shaking me."
    scene sky background
    show monica rescue
    with Dissolve (1.3)
    unk "Answer me!!!!"
    mc "Then..."
    show monica rescue 2
    with dissolve 
    unk "You are alive!!!!! "
    mc "I got rescued by a lovely lady. I got rescued by an Angel."
    mc "Oh....hi?"
    unk "Why are laying here in the sun?"
    mc_thought "(Omg she is so cute...who is she?)"
    show monica rescue
    with dissolve
    unk "Answer me please?"
    mc "She has such a good smell."
    mc "I...I had nothing left, so I just...you know...\"gave up on life\"."
    unk "What did you.."
    show monica rescue sad
    with dissolve
    unk "What did you just say?"
    mc "Hey woman, please don't cry!"
    mc "See? I'm better now, it was all just a joke, 'hahahaha' all better."
    show monica rescue embarrassed
    with dissolve
    mc "I'm even laughing! huuuu, just a joke...'haha'"
    mon "You are so funny, my name is {color=#4e25c0ff} monica{/color}."
    mc "Hi Monica, my name is [player.name]."
    mc_thought "(She is so beautiful...and she is so close. I have to be careful or I might get a boner.)"
    mon "So...do you need some help getting it up?"
    mc "What did you say?!?!??"
    show monica rescue standing with dissolve
    mon "I said..do you need some help getting up??"
    mc "Yes I need help."
    scene black with dissolve
    mc_thought "(So...monica rescued me from the streets.)"
    show house bg
    show family rescue
    with dissolve
    mc_thought "(She introduced me to her family, two daughters {color=#4e25c0ff} Ashley{/color} and {color=#4e25c0ff} Linda{/color})"
    mc_thought "(The younger one is cute and lovely, the older one...not so much.)"
    scene
    show bedroom night
    with dissolve
    mc_thought "(She even offered me a room in her house in exchange for my help with the household chores, effectively becoming my landlady.)"
    scene
    show guild gate morning
    with dissolve
    mc_thought "(I made numerous attempts to become a member of the guild, but they rejected me each time, because I wasn't strong enough nor) possessed any magical abilities.)"
    scene bedroom night with dissolve
    mc_thought "(So...that's it, today is my birthday...18 years old and I didnt even care to tell anyone. I mean...there is nothing to) celebrate....im still a total loser.)"
    scene black with dissolve
    menu:
        "Anyway.. at least I have a home now...better go to sleep."
        "sleep":
            pass
    pause 2.0
    jump prologue_1
    return


label prologue_1:
    $ aphrodite.revealed = True
    # white_screen
    aph "[player.name]...[player.name]....Awake..."
    # aphrodite appears on the screen (giant)
    mc "What is this? Am I dreaming again?"
    show aphrodite throne hidden 0 with Dissolve (1.5)
    mc "Ok...this is a dream....but what is this big thing in my dream?"
    show aphrodite throne hidden 1 with dissolve 
    mc "Seems like a throne...with someone in it...what a crazy dream."
    unk "This is no dream [player.name]."
    show aphrodite throne hidden 2 with dissolve 
    mc "Wait...it can’t be, is that.."
    show aphrodite throne with Dissolve(1.5)
    pause 0.5
    mc "What? What's going on? Oh my god, it's you! You're the girl from the message in that game!"
    aph "This is no dream, [player.name]. You answered my call, and now you are my champion in this world."
    menu:
        mc "Whaaaaat?!?!?"
        "What do you mean by champion?":
            mc "What do you mean by champion?"
            jump champion
        "I'm not your champion!":
            mc_shout "I'm not your champion!"
            aph "Oh...Aren't you?"
            jump champion
    return

label champion:
    aph "I'm the developer...really."
    mc_shout "That's not how it works!!!"
    mc "Lady, do you know what I have been through since I got here? I almost starved to death since you sent me here."
    mc "You can't just send someone to another universe just because they clicked \"yes\" on some random message."
    aph "There was a contract, and you agreed to its terms. That's all there is to it. Now you are bound to serve me and be my champion."
    mc "That's not how it was supposed to be. You promised me an adventure where I would possess great powers, engage in action, and have lots of sex. Instead, I got nothing at all."
    mc "After nearly a year of living in this world, you suddenly appear and tell me that I am your champion?!?!"
    with vpunch
    aph_shout "Silence!!!"
    mc_thought "(What was that? An earthquake?)"
    aph "I mean, I'm sorry little one. I needed you to be the right age so I could reach you in a more direct way. Today is your birthday so now it's the right time."
    menu:
        aph "There is no way to go back now. Besides, being the champion of the {b}Goddess of Pleasure{/b} comes with great advantages."
        "I don't care who you are!":
            mc_shout "I don't care who you are!!!"
            mc "Wait...{b}Goddess of Pleasure?{/b}"
            jump goddes_of_pleasure
        "Goddess of Pleasure?":
            mc "\"{b}Goddess of Pleasure{/b}\"???"
            jump goddes_of_pleasure

    return

label goddes_of_pleasure:
    menu:
        aph "Are you saying that you never heard of the goddess of pleasure, {b}The Great Aphrodite?{/B}"
        "I’m sorry no":
            scene aphrodite throne thinking with dissolve
            aph_thought "(In the name of the great ME...what are humans doing these days?)"
        "Not at all":
            scene aphrodite throne thinking with dissolve
            aph_thought "(Oh my, what are humans thinking these days?)"
    scene
    show aphrodite throne 2
    with vpunch
    aph_shout "I'm The Great Aphrodite!"
    with vpunch
    aph_shout "The Goddess of Pleasure!"
    aph "The Goddess of Sex."
    aph "Goddess of Lust and all that there is to do with masturbation."
    aph "The Goddess of...gangbangs and threesomes."
    aph "The Goddess of foursomes and fivesomes."
    menu:
        aph "The Goddess of..."
        "Ok I get it":
            mc "Ok...I think I get it"
        "I think I understood":
            mc "...I think....I understood..."
    scene
    show aphrodite throne thinking
    with vpunch
    aph_shout "Shut up mortal!"
    aph "And hardcore sex, casual sex, fellatios, sexual pleasure, orgies….anal sex, vaginal sex double penetration sex, and......."
    aph "The Goddess does creampies, pee action, bukkake, public sex, furry and….."
    "..."
    "(That went on for 20 minutes or so........)"
    show aphrodite throne with dissolve
    menu:
        mc "Anyway..."
        "Why me?":
            mc "I understand but...why me?"
        "Wasn't there anybody else for this job?":
            mc "I see but...wasn't there anybody else for this job?"
    jump why_me

    return

    label why_me:
        aph "I can see all living creatures in all universes, and you, [player.name], are one of the most sexually charged beings I have ever come across."
        mc "Am I?"
        aph "Yes, you are. I see you watching, reading, and researching porn and hentai daily."
        mc_thought "(Oh my god.)"
        aph "Yes I saw you getting hard and masturbating every day over and over and over."
        mc_thought "(What in the Harry Potter?!?)"
        mc "Ok I think I understand…"
        show aphrodite throne 2 with dissolve
        aph "I saw how you became aroused over little things, and how you imagined fucking every cute girl in your school…and watched as you masturbated to them in secret."
        mc_thought "(I can't believe this.. this can't be possible...)"
        mc "That was supposed to be private..."
        aph "I even know about last summer on vacation with your family when you masturbated and cummed in the...."
        mc_shout "Okay I think I got it!!!"
        show aphrodite throne thinking with dissolve
        aph "Anyway, in my opinion, you are a great young man, and this {b}task{/b} will be beneficial for both you and the people of this world."
        menu:
            mc_thought "(\"(Task\" I knew it...I knew there was a catch.)"
            "Task?":
                show aphrodite throne 3 with dissolve
                mc "Task? What task?"
            "What do you mean by task?":
                show aphrodite throne 3 with dissolve
                mc "What do you mean by task?"
        jump task

    label task:
        aph "Of course...your task as my champion is to conquer and fuck all the girls in this world. You must help unleash the lustful side of this world’s inhabitants."
        mc_shout "I knew it!"
        mc "Wait...conquer this worlds and fuck all the girls? Did I hear that right?"
        aph "Yes you did, you are to conquer this world fuck all the girls in this world... no exception, friend or enemy."
        aph "They all are to be conquered and fucked with no mercy. No exceptions allowed. And you must make them more and more lustful for you"
        mc_thought "(Well...that does sounds like a lot of fun..)"
        mc "Well...After taking a lot of thought..."
        mc "I.. decided to accept your terms."
        aph "As I said, You have already signed the contract."
        mc "Hey Goddess."
        scene
        show aphrodite throne thinking
        with vpunch
        aph_shout "It's \"Great Goddess Aphrodite\""
        show aphrodite throne 4 with dissolve
        scene
        show aphrodite throne 4
        mc_thought "(Damn...she is serious about this...better address her properly...she is shaking everything here.)"
        mc "Ok... Great Goddess Aphrodite...."
        mc "Not trying to bother you but..."
        menu:
            "How the hell am I supposed to do that?!?":
                mc "How the hell am I supposed to do that?!?!?"
            "I can't do that":
                mc "I don't know how much of my life you have seen, but I'm not the kind of person who can easily fuck every girl in a world."
        jump how
        return

label how:
    mc "I mean... I'm not very attractive, and I'm not very good at socializing..."
    show aphrodite throne thinking with dissolve
    aph "Little [player.name], you are in the hands of the Goddess of Pleasure now."
    aph "I bestow upon you the {i}{color=#ff67d1}magical blood of the sex warlocks and my power{/i}{/color} so that you may fulfill your task."
    aph "Besides...you already have a big....\"talent\".. but you are not aware of that just yet."
    show aphrodite throne with dissolve
    mc_thought "(\"(Magic blood of the sex warlocks and her power?\")"
    show aphrodite throne with dissolve
    aph "And also."
    show aphrodite throne before with dissolve
    aph "A little gift..."
    show aphrodite throne during with dissolve
    aph "from your Goddess..."
    mc_thought "(Man I can feel a change in the atmosphere even from here.)"
    show aphrodite throne during 1 with dissolve
    mc_thought "(Am I seeing things?)"
    show aphrodite throne during 2 with dissolve
    mc_thought "(Such an intense energy.)"
    show aphrodite throne during 3 with dissolve
    mc_shout "Are you sure this is safe!!!!!?"
    pause 0.5
    show aphrodite throne during 4 with dissolve
    menu:
        aph "{color=#fc89ce}This Book.{/color}"
        "A book?":
            mc "A Book....Really?"
        "Is that a joke?":
            mc "A Book..is this a Joke?"
    aph "No joke Dear [player.name]. Only you can truly read this book, besides me of course."
    aph "This book holds the power to unlock the path to everyone's pleasure, use it wisely."
    mc "But that's just a book!! how will I be able to..."
    aph "Relax......and sleep now."
    scene black with dissolve
    jump awake_at_home

label awake_at_home:
    $ linda.revealed = True
    show wakeup prologue with dissolve
    mc_thought "(It was just a dream...after all.)"
    lin "Hi [linmc], did you sleep well?"
    show linda prologue with dissolve
    mc "Liiiiinda, what are you doing here?"
    lin "{color=#fc89ce}Mon{/color} told me to wake you up, she said {color=#fc89ce}she needs to talk with you.{/color}"
    mc_thought "(Hmmm...maybe she has something she wants me to do for her. I should go find out what it is.)"
    lin "[player.name]?"
    mc "Sorry, I was lost in thought. Good morning, Linda."
    lin "Good morning [player.name]."
    mc "Where is Monica?"
    lin "Well, I believe she is in the kitchen."
    show linda prologue 2 with dissolve
    mc "Alright, I suppose it's time to get up."
    menu:
        lin "[player.name] are you ok?"
        "I am":
            mc "I am doing alright, thanks for asking."
            show linda prologue 3 with dissolve
            lin "No you aren't."
            mc "What do you mean?"
            lin "You didn't give me a good morning hug."
        "Why do you ask?":
            mc "I...think I am, why do you ask?"
            show linda prologue 3 with dissolve
            lin "Well...you didn't give a good morning hug to your [linmc]...that's not like you.."
    mc "What?"
    mc_thought "(Wow, she is really serious about it...)"
    show linda prologue sad with dissolve
        # she makes a face
    mc_thought "(She is even making a face now, guess she is really mad about it.)"
    jump linda_will_you_hug_me
    return


label linda_will_you_hug_me:
    menu:
        lin "So...will you hug me or not?"
        "I will hug you":
            mc "Ok, I will give you a hug."
            # she smiles
            lin "Huuuu, you are the best [mclin] there is."
            jump linda_hug
        "No I won't do that":
            mc "No I won't, you are already too grown up for this kind of stuff."
            show linda prologue sad 2 with dissolve
            lin "Why are you so mean to me? You were supposed to be my [mclin]?"
            mc "As I said you are already a grown up."
            show linda prologue sad 3 with dissolve
            scene
            show linda prologue sad 3

            lin "Gi gi gi gi gi gi gi gi gi gi gi gi gi"
            mc_thought "(Geeeez what is this? Is she crying over this? It seems like an unusual way to cry)"
            lin "Gi gi gi gi gi gi."
            menu:
                lin "Gi gi gi gi gi gi gi gi gi."
                "Alright...I will hug you so stop it already.":
                    mc_thought "(She is too cute for me to be treating her like this)"
                    mc "Alright, stop it already...I will hug you ok?"
                    # stops crying
                    show linda prologue happy with dissolve

                    lin_shout "Really?"
                    mc "Yeah... it's just a hug after all."
                    jump linda_hug
                "Stop crying!":
                    mc_thought "(Man...she just wont stop.)"
                    mc_shout "Stop crying!"
                    # she stops and look at you
                    show linda prologue angry with dissolve
                    lin "Why are you yelling at me?"
                    mc "Because you cry too loud."
                    show linda prologue leaving1
                    lin "Okay then….I-I’m going to leave....ok?"
                    mc_thought "(Man... I never really paid attention before, but when did Linda get such a beautiful ass?)"
                    show linda prologue leaving2
                    mc_thought "(Man... she is stunningly beautiful.)"
                    show linda prologue leaving3
                    mc_thought "(I even thought about stopping her, but it's just too enjoyable to watch her beautiful ass sway as she walks) away.)"
                    show linda prologue leaving4
                    mc_thought "(Well...that's it..time to make the decision.)"
                    menu:
                        "What should I do?"
                        "Stop her":
                            mc "Hey Linda."
                            show linda prologue leaving5 with dissolve
                            lin "What?"
                        # "Do nothing":
                        #     jump start_3
                    menu:
                        "Let me hug you please":
                            mc "Let me hug you please?"
                            show linda prologue happy with dissolve
                            pause 1.0
                            lin "Really [player.name] ?!!?!? best!!"
                            jump linda_hug
                        "I'm sorry for making you cry.":
                            mc "I'm sorry for making you cry."
                            lin "I see..."
                            mc "Come here and let me give you a big hug"
                            show linda prologue happy with dissolve
                            pause 1.0
                            lin_shout "Really?!?!? Oh [player.name]!!! I love you too, thank you!!"
                            jump linda_hug
    return

label linda_hug:
    show linda prologue hug1 with dissolve
    # she hugs you
    lin "I really love your hugs, your hugs are just the best."
    mc_thought "(Come to think of it...maybe this 'hug' thing...isn't so bad after all...)"
    menu:
        mc_thought "(Maybe I should...)"
        "Enjoy the hug a little more":
            mc_thought "(Yes, I think I will enjoy this \"hug\" a little more…)"
            mc "I know right? I also love hugging you Linda."
            jump linda_enjoy_the_hug
        "Stop hugging":
            mc "Okay, that's enough hugging."
            jump linda_stop_hugging_prologue
    return

label linda_enjoy_the_hug:
    lin "You are just the best."
    show linda prologue hug2 with dissolve
    mc_thought "(Yes, just like that... It's such a nice view. I'm absolutely loving it... and that ass of hers is just the best I've ever) seen)"
    menu:
        mc_thought "(Maybe I should....)"
        "Try to (move your hand a little lower)":
            mc "..."
            show linda prologue hug3 with dissolve
            jump linda_enjoy_the_hug_2
        "Stop the hug":
            mc "Okay, that's enough hugging."
            jump linda_stop_hugging_prologue
    return

# randomize phrases latter
label linda_enjoy_the_hug_2:
    lin "[player.name]?"
    mc "What?"
    menu:
        lin "Isn't this hug taking a little too long?"
        "I love hugging you" :
            mc "The thing is that I like hugging my [linmc] like that."
            lin "Is that so? In that case...go on hugging me as much as you want."
            jump linda_enjoy_the_hug3
        "You are right.":
            mc "You are right, I'm sorry Linda, my mistake."
            lin "No, that's not what I meant!"
            lin "You can keep hugging me all you want."
            menu:
                "Nah, let's just stop.":
                    mc "No, let's just stop, it was a really long hug."
                    jump linda_stop_hugging_prologue
                "Continue hugging":
                    mc "I see, do you want to stop then?"
                    lin "No, I want to continue."
                    mc_thought "(Just as I thought.)"
                    jump linda_enjoy_the_hug3

label linda_enjoy_the_hug3:
    mc_thought "(Ok then...for the next step I think I will...)"
    mon_shout "Lindaaaa what's taking you so long?"
    menu:
        lin "That's Monica calling...sorry [player.name], I have to go now."
        "Tell her to stay (requires courage > 3)" if courage > 3:
            "The course with courage"
        "Let her go":
            mc_thought "(Oh man...now?)"
            mc "Yes, I think you should go..."
            jump linda_stop_hugging_prologue
    $ Linda.revealed = True

# randomize phrases latter
label linda_stop_hugging_prologue:
    show linda prologue leaving5 with dissolve
    mc_thought "(Yep that was one good way to start a day.)"
    lin "Good morning [player.name]."
    mc "Good morning lin.....!!!"
    show book shining with dissolve
    mc_shout "THE BOOK?!?!?!??"
    lin "What? what book?"
    mc_thought "(She can’t see it??)"
    
    show aphrodite throne during 4: 
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.12)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with dissolve
    aph_thought "\"Only you can truly read this.\""
    mc_thought "(Oh, I remember now...so only I can see it.)"
    hide aphrodite with dissolve
    lin "[player.name], What book??" 
    mc "Sorry, I just remembered I have to return a book in the library today."
    lin "Anyway, leaviiiing."
    hide book
    show book shining:
            ypos -96 
    with dissolve
    mc_thought "(She left.)"
    mc_thought "(So it wasn't a dream after all.)"
    mc_thought "(This also explains a lot of my unusual behavior with hugs this morning, I never looked at Linda this way, Its like im someone) else.)"
    mc_thought "(I think I will like this Aphrodite champion thing. Anyway, let's open this book.)"
    show screen book
    show bedroom morning
    mc "It seems like this book will only show me the girls I've met after getting it. So no one I met before will appear. Interesting."
    # lin "It's ok if you want to hug me more big bro...I understand."
    jump start_3
    return

label ashley_prologue:
    $ ui_show_top_screen = False
    # scene
    scene hallway morning
    show ashley half sleepover angry2
    with dissolve
    mc "Good morning Ashley."
    show ashley half sleepover angry
    with dissolve
    ash "Don't try that with me brat."
    mc "What do you mean?"
    ash "I mean that I don't want people to think that I'm related to a loser like you."
    mc "Jeez, why is this happening now? What's the problem?"
    ash "The problem is that I have to look at your ugly face everyday, don't you have anywhere else so go?"
    mc "Monica let me stay here, so I have as much right to live here as you."
    ash "*Sigh* Yeah, whatever..."
    ash "Couldn't she at least pick a popular boy or someone that could actually be an adventurer?"
    mc "I can still try."
    ash "Yeah... and fail as you always do."
    mc_thought "(Man she is such a drag... but she is kind of cute though.)"
    menu:
        ash "You don't even have a job."
        "Not your business":
            mc "That's none of your business."
        "Do YOU?":
            mc "Hmmm, do YOU have a job?"
    ash_shout "What did you just say??!?"
    mc "Nothing..."
    mc_thought "(Better not to pick a fight with her just yet.)"
    ash "That's what I thought."
    mc "Do you know where Monica is?"
    ash "And why should I tell you?"
    mc_thought "(Geez, she won’t give me a break.)"
    mc "Please?"
    ash "She's downstairs making your breakfast. But why? Why does she even bother doing things like this for a loser like you?"
    mc "Maybe because she likes me?"
    ash "Pff, get real, I think she only let you in because it's convenient."
    mc "What do you mean?"
    ash "I mean isn't that obvious? Dad is always traveling, She is a mom with two daughters."
    ash "She probably adopted a boy so that he could help out around the house and be the man of the house while Dad is away on business trips."
    menu:
        ash "But here you are, small and weak, such a disappointment."
        "I could become a powerful mage":
            mc "Maybe someday I will become a powerful mage."
            ash "A loser like you? don't make me laugh, you probably don't have any magical blood in you."
        "I could become a powerful warrior":
            mc "Maybe someday I will become a really strong warrior."
            ash "A loser like you? don't make me laugh, with your body you can't even beat ME in a fight."
    ash "At your age all warriors were strong and all wizard heirs had their powers awakened and you have none, so stop dreaming about it."
    mc "I will grow up and be awesome, wait and see."
    hide ashley
    show ashley half sleepover happy
    with dissolve
    ash_shout "Hahahaha, you are so funny."
    mc "..."
    ash "..."
    scene hallway morning
    show ashley half sleepover angry2
    with dissolve
    ash "Wait that wasn't a joke?...oh you are more dumb than I thought, do whatever you want."
    mc_thought "(Man, she is such a drag...doesn't she know she is talking to Aphrodites chosen one?)"
    mc_thought "(She left...)"
    $ ashley.revealed = True
    hide ashley with dissolve
    #  she leaves
    $ ui_show_top_screen = True
    return

    label monica_prologue:
        $ ui_show_top_screen = False
        scene kitchen bg1 
        show monica half turned
        with dissolve
        mc_thought "(Oh, there she is...)"
        mc "Monica?"
        show monica half talking
        with dissolve
        mon "Oh, good morning sweetie, how was your night?"
        mc "Good morning Monica, it was good thank you."
        mon "I made you breakfast."
        mc "Thank you Monica, but I'm really not that hungry right now."
        show monica half talking2
        with dissolve
        mon "Are you sure? I made your favorite 3 eggs, bacon and warm milk, not too hot, not too cold, just warm, the way you like it."
        # ashley enters and sees you two
        mc "Monica, you didn't have to do this, but you're simply the best. Thank you so much, I'm going to enjoy this breakfast!"
        show monica half happy
        with dissolve
        mon "Oh you don't need to thank me sweetie, and please don't call me Monica, call me \"Mon\" there's no need to be so formal."
        show monica half talking3
        with dissolve
        menu:
            mon "So, today is the big day isn't it?"
            "Big day?":
                show monica half talking2
                with dissolve
                mc "Big day?"
                mon "Yes the big day."
            "Oh...yes...the big day....":
                show monica half talking
                with dissolve
                mon "Oh sweetie, don't tell me you forgot about today?"
        mc "..."
        show monica half talking
        mon "Yes, you told me that you would help me in the {color=#fc89ce}flower fields{/color} while you look for a job."
        mc_thought "(Wait, flower fields, don't I have a world to conquer? Nah she is so sweet I can't say no to her.)"
        mc "I see, so today is my first day helping on the flower fields. I’ll do my best."
        $ ui_show_top_screen = True
        $ monica.revealed = True
        $ monica.book_phrase = "Go help her in the flower camp."
        $ monica_prologue = False
        $ ui_can_change_map = True
        return



