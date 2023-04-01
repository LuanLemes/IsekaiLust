


label input_characters_relations:
    scene black

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    "These three girls are {color=#9b006c}Monica{/color}, {color=#9b006c}Ashley{/color} and {color=#9b006c}Linda{/color}, (Mother and her dauthers), they will live with you during the game, but what are they to you?"
    hide monica
    show monica:
        pos (-276, 10) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    $ monicamc = renpy.input("{color=#9b006c}Monica{/color} (left one) is your (default landlady)?", length = 14, default = "landlady" )
    $ mcmon = renpy.input("And you are her? (default tenant)", length = 14, default = "tenant")

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide ashley
    show ashley:
        xpos 16
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    
    $ ashmc = renpy.input("{color=#9b006c}Ashley{/color} (Middle one) is your?", length = 14, default = "friend" )
    $ mcash = renpy.input("And you are her (default friend)", length = 14, default = "friend" )

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide linda
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93

    $ linmc = renpy.input("{color=#9b006c}Linda{/color}  (Right one) is your(default friend?)", length = 14, default = "friend" )
    $ mclin = renpy.input("And you are her? (default friend)", length = 14, default = "friend")

    $ monicamc = str(monicamc.lower())
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
    "So {color=#9b006c}Monica{/color}  is your {color=#9b006c}[monicamc]{/color} and you are her {color=#9b006c}[mcmon]{/color}."

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide ashley
    show ashley:
        xpos 16
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    "{color=#9b006c}Ashley{/color} is your {color=#9b006c}[ashmc]{/color} and you are her {color=#9b006c}[mcash]{/color}."

    show monica:
        pos (-276, 10) 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show ashley:
        xpos 16
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    hide linda
    show linda:
        pos (383, 75) zpos 0.0 xzoom 0.93 yzoom 0.93
    "And {color=#9b006c}Linda{/color} is your {color=#9b006c}[linmc]{/color} and you are her {color=#9b006c}[mclin]{/color}? Is that right?"

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
            "Alright."
            jump prologue
        "No(I want to try again)":
            "Lets fix that then."
            jump input_characters_relations
    $ monica.role = monmc
    $ ahsley.role = ashmc
    $ linda.role = linmc
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
    mc "I was a nerd boy in my original life, I was a normal boy, and I didnt get any girls in my life."
    mc "They always like the popular type more... So I never stood a chance."
    scene kiss bg with dissolve
    mc "Even so one day I took corage and decided to buy a hentai game."
    mc "This one....{b}{color=#9b006c}(Cronicles of Aprhodite){/color}{/b}....this one, this one should be good."
    mc "I thought the lady of the front was hot so.....anyway."
    scene black with dissolve
    mc "As soon as I got home I went to play it."
    window hide
    show aphrodite world with dissolve
    pause (1.0)
    mc "Man I like this game already, she hot!!!"
    aph "[player.name]."
    aph "[player.name] Im the Great Goddes Aphrodite!"
    aph "Im in this game to make an invitation to you and only you."
    aph "Do you want to become the goddes Aphrodite powerfull champion, to live an awesome adventure with lots of sex and action?"
    mc "Of course!!! I mean..... would I ever say no to such a question?"
    mc "And I wonder...till this day...why..why why!? did I click yes?!!"
    scene black with dissolve
    mc "I dont know what kind of magic was on that game."
    scene tavern bg with fade
    mc "Because I ended in a world full of fantasy and magic yes."
    mc "But I didnt know any one on this other world, I didnt have any help or family. I was homeless, it was really awfull."
    mc "I wasnt powerfull, I didnt become any goddes champion and sure as hell I didnt have sex till this day!"
    scene tavern bg 2 with fade
    pause (1.5)
    mc "And many times I ate spoiled food from other people so I wouldnt starve to death. {color=#c02566ff} \"Please help the patreon so the developer dont end up that way.\" {/color}"
    mc "It was like this during some months...it was then...when I decided...."
    scene tavern bg 3 with fade
    pause (1.0)
    mc "Thats it....everybody sees me everyday and its as if Im not even there."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "Im nothing in this world...nothing..."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.9)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I Tried my best to see if I could become warrior and Im took weak."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.8)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I tried many times to get in a guild but I didnt pass the test."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.7)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I even tried to become a wizard but my blood has no magic in it."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "I even more of a loser in this world than I am was in my."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.35)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "And the girls here dont like me either."
    show tavern bg 3 with dissolve:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    mc "Thats it...I give up."
    show tavern bg 3 with dissolve:
    mc "Im going to close my eyes....and never open then again."
    scene black with Dissolve(2.0)
    mc "But then......"
    unk "Hey, are you ok?"
    mc "Of course I didnt listen....I thought it was all my imagination."
    unk "Hey!!!"
    mc "When I thought I was done for, when I thought it was my end."
    unk "Why dont you answer me?"
    mc "I felt two soft hands grabing me and shaking me."
    scene sky background
    show monica rescue
    with Dissolve (1.3)
    unk "Anwer me!!!!"
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
    mc "I....I...got nothing and then I just...you know..\"gave up living\"."
    unk "What did you?"
    show monica rescue sad
    with dissolve
    unk "What did you just say?"
    mc "Hey woman, please dont cry!"
    mc "See? Im better now, it was all just a joke, 'hahahaha' all better."
    show monica rescue embarassed
    with dissolve
    mc "Im even laughing! huuuu, just a joke...'haha'"
    mon "You are so funny, my name is {color=#4e25c0ff} monica{/color}."
    mc "Hi Monica, my name is [player.name]."
    mc_thought "(she is so beautifull...and she is so close. I have to be carefull or I might get a boner.)"
    mon "So...do you need some help to getting it up?"
    mc "What did you say?!?!??"
    show monica rescue standing with dissolve
    mon "I said..do you need some help getting up??"
    mc "Yes I need help."
    scene black with dissolve
    mc_thought "(So...monica rescued me from the streets.)"
    show house bg
    show faimly rescue
    with dissolve
    mc_thought "(she introduced me to her family, Two dauthers {color=#4e25c0ff} Ashley{/color} and {color=#4e25c0ff} Linda{/color})."
    mc_thought "(The younger one is cute and lovely, the older one...not so much.)"
    scene
    show bedroom night
    with dissolve
    mc_thought "(She also gave me a room in her house in exchange for me helping her with her with the house chores. She became my landlady)"
    scene
    show guild gate morning
    with dissolve
    mc_thought "(I tried many times to become a member of the guild, but they said Im not strong enough, nor I have any magic on me.)"
    scene bedroom night with dissolve
    mc_thought "(So...thats it, today Is my birthday...18 years old and I didnt even care to tell anyone. I mean...there is nothing to  celebrate....Im still a total loser.)"
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
    mc "Wait...it can´t be, is that?"
    show aphrodite throne with Dissolve(1.5)
    pause 0.5
    mc "What? What is it? Omg it is you you are the girl from the message on that game!"
    aph "This is no dream [player.name] You accepted my call, and now you are my champion in this world."
    mc "Whaaaaat?!?!?"
    menu:
        "What do you mean by champion?":
            mc "What do you mean by champion?"
            jump champion
        "Im not your champion!":
            mc_shout "Im not your champion!"
            aph "Oh...Arent you?"
            jump champion
    return

label champion:
    aph "You clicked yes on the message didnt you?"
    mc_shout "Thats not how it works!!!"
    mc "Lady, do you know what I have been through since I got here? I almost starved to death since you sended me here on this planet."
    mc "You cant just send someone to another universe just because they clicked \"yes\" on some random message."
    aph "There was a contract and you agreed to it, thats is all. Now  you are my serve and my champion."
    mc "Thats not how it works, you promissed me an adventure where I would have a great power, action, and lots of sex and I got nothing."
    mc "And now, almost one year after I get on this world you appear telling me that I am your champion??!?!"
    with vpunch
    aph_shout "Silence!!!"
    mc_thought "What was that? An earthquake?"
    aph "I mean, Im sorry little one. I needed you to be the right age so I could reach you in a more direct way. today is your birthday so now its the right time."
    aph "There is no way to go back, besides, there are very good advantages in being the {b}Goddes of pleasure{/b} champion."
    menu:
        "I dont care who you are!":
            mc_shout "I dont care who you are!!!"
            mc "Wait...{b}Goddes of Pleasure?{/b}"
            jump goddes_of_pleasure
        "Goddes of Pleasure?":
            mc "\"{b}Goddes of Pleasure{/b}\"???"
            jump goddes_of_pleasure

    return

label goddes_of_pleasure:
    aph "Are you saying that you never heard of the goddess of pleasure, {b}The Great Aphrodite?{/B}"
    menu:
        "Im sorry no":
            scene aphrodite throne thinking with dissolve
            aph_thought "(In the name of the great Me...what are humans doing these days?)"
        "Not at all":
            scene aphrodite throne thinking with dissolve
            aph_thought "(Oh My... what are humans doing thinking these days?)"
    scene
    show aphrodite throne 2
    with vpunch
    aph_shout "Im The Great Aphrodite!"
    with vpunch
    aph_shout "the Goddes of pleasure!"
    aph "the Goddes of sex."
    aph "Goddes of  and all that there is to do with masturbation."
    aph "The Goddes of...gangbangs and threesomes."
    aph "The Goddes of foursomes and fivesomes."
    aph "The Goddes of..."
    menu:
        "Ok I get it":
            mc "Ok...I think I get it"
        "I think I understood":
            mc "...I Think....I understood..."
    scene
    show aphrodite throne thinking
    with vpunch
    aph_shout "Shut up mortal!"
    aph "And Sex and casual sex, fellatios, sexual pleasure and orgys….anal sex vaginal sex double penetration sex and......."
    aph "The Goddes creampies and pee action and cum and bukkakes and public sex and furry and….."
    "..."
    "(That did go on for 20 minutes or so........)"
    show aphrodite throne with dissolve
    mc "Anyway..."
    menu:
        "Why me?":
            mc "I Understand but...why me?"
        "Wasnt there anybody else for this job?":
            mc "I See but...wasnt there anybody else for this job?"
    jump why_me

    return

    label why_me:
        aph "Well, I can see all living creatures in all universes, and you [player.name] between the most sexual  beings in all universe."
        mc "Am I?"
        aph "Yes you are, I see you watching reading and researching porns and hentais everyday."
        mc_thought "(Oh my god)"
        aph "Yes I saw you getting hard and masturbating every day again and again and again."
        mc_thought "(what in the harry p#tter?!?)"
        mc "Ok I think I got it…"
        show aphrodite throne 2 with dissolve
        aph "I saw as you were aroused for the little things, and as you imagined fucking every cute girl in your schooll…and as you masturbated to them in secret."
        mc_thought "(I cant believe I just cant believe...)"
        mc "Ok that was suposted to be private..."
        aph "I even know about last summer on the vacation with your family when you masturbated and cum in the...."
        mc_shout "Okay I think I got it!!!"
        show aphrodite throne thinking with dissolve
        aph "Anyway, In opinion yes you are a great boy, and this {b}task{/b} will be both good for you and for the people of this world."
        mc_thought "(\"Task\" I knew it...I knew there was a catch)"
        menu:
            "Task?":
                show aphrodite throne 3 with dissolve
                mc "Task? What task?"
            "What do you mean by task?":
                show aphrodite throne 3 with dissolve
                mc "What do you mean by task?"
        jump task

    label task:
        aph "Of course...your task as my champion is to conquer and fuck all the girls in this world and to realease the lustfull side of the people of the planet."
        mc_shout "I knew it!"
        mc "Wait...conquer this worlds and fuck all the girls? Did I hear that right?"
        aph "Yes you did, you are to conquer this world fuck all the girls in this wolrd... no exception, friend or enemy."
        aph "They all are to be conquered and fucked with no mercy. No exceptions allowed. And you are to make them more and more lustfull for you."
        mc_thought "(Well....that seems like fun, very very very fun.)"
        mc "Well...After taking a lot of thought..."
        mc "Well...I accept your terms."
        aph "As I said, You have already signed the contract."
        mc "Hey Goddes."
        scene
        show aphrodite throne thinking
        with vpunch
        aph_shout "Its \"Great Goddes Aphrodite\""
        show aphrodite throne 4 with dissolve
        scene
        show aphrodite throne 4
        mc_thought "(Damn...she is serious about this...better say her way...she is shaking everything here.)"
        mc "Ok... Great Goddes Aphrodite...."
        mc "Not Willing to borther you but..."
        menu:
            "How the hell am i supposed to do that?!?":
                mc "How the hell am I supposed to do that?!?!?"
            "I can´t do that":
                mc "I dont know how much of my life you saw but...Im not the kind of person that can fuck every girl in a world."
        jump how
        return

label how:
    mc "I mean.... Im ugly, and Im not very social..."
    show aphrodite throne thinking with dissolve
    aph "Little [player.name], you are in the hands of the Goddess of Pleasure now."
    aph "I give you The {i} {color=#ff67d1}Bless of the magic blood of the sex warlocks and my power{/i}{/color} with it."
    aph "besides...you alraedy have a big....\"Talent\".. but you are not aware of that just yet."
    show aphrodite throne with dissolve
    mc_thought "(\"Magic blood of Warlocks of sex? and her power?\")"
    show aphrodite throne bbehind with dissolve
    aph "And also."
    show aphrodite throne before with dissolve
    aph "A little gift..."
    show aphrodite throne during with dissolve
    aph "from your Goddes..."
    mc_thought "(man I can fell a change in the atmosphere even from here)"
    show aphrodite throne during 1 with dissolve
    mc_thought "(Am I seeing things?)"
    show aphrodite throne during 2 with dissolve
    mc_thought "(Such an intense energy)"
    show aphrodite throne during 3 with dissolve
    mc_shout "Are you sure this is safe!!!!!?"
    pause 0.5
    show aphrodite throne during 4 with dissolve
    aph "{color=#4d0537}This Book.{/color}"
    menu:
        "A book?":
            mc "A Book....Really?"
        "Is that a joke?":
            mc "A Book..is That a Joke?"
    aph "No Joke Dear [player.name]. Only you can truly read this book, besides me of course."
    aph "This book has the power to know the path for everyone pleasure, use it wisely."
    mc "But thats a book!! how will I be able to..."
    aph "Relax......and sleep now."
    scene black with dissolve
    jump awake_at_home

label awake_at_home:
    $ linda.revealed = True
    show wakeup prologue with dissolve
    mc_thought "(It was just a dream...after all.)"
    lin "Hi [linmc], did you sleep well?"
    show linda prologue with dissolve
    mc "Liiiiinda what are you doing here?"
    lin "{color=#4d0537}Mom{/color} told me to wake you up, she said {color=#4d0537}she needs to talk with you.{/color}"
    mc_thought "(hmm..maybe she wants me to do something for her...well I better go see what it is)"
    lin "[player.name]?"
    mc "Sorry, I was thinking, Good morning Linda..."
    lin "Good morning [player.name]."
    mc "Where is Monica?"
    lin "Well, she is in the Kitchen I think."
    show linda prologue 2 with dissolve
    mc "Ok, Well guess its time to get up up."
    lin "[player.name] are you Ok?"
    menu:
        "I am":
            mc "I am very ok, thanks for asking."
            show linda prologue 3 with dissolve
            lin "No you arent."
            mc "What do you mean?"
            lin "You didnt gave me a good morning hug."
        "Why do you ask?":
            mc "I...think I am, why do you ask?"
            show linda prologue 3 with dissolve
            lin "Well...you give a good morning hug to your [linmc]...thats not like you.."
    mc "What?"
    mc_thought "(Wow, she is really serious about it...)"
    show linda prologue sad with dissolve
        # she makes a face
    mc_thought "She is even making a face now, guess she is really mad about it."
    jump linda_will_you_hug_me
    return


label linda_will_you_hug_me:
    lin "So...will hug me or not?"
    menu:
        "I will hug you":
            mc "Ok, I will give you a hug."
            # she smiles
            lin "Huuuu, you are the best [mclin] there is."
            jump linda_hug
        "No I wont do that":
            mc "No I wont, you are already too grown up for this kind of stuff."
            show linda prologue sad 2 with dissolve
            lin "Why are you mean to me? You were supposed to be my [mclin]?"
            mc "As I Said you are already a Grown up."
            show linda prologue sad 3 with dissolve
            scene
            show linda prologue sad 3

            lin "Gi gi gi gi gi gi gi gi gi gi gi gi gi"
            mc_thought "(Geeeez what is this? is she crying over this?also what a strange way to cry)"
            lin "Gi gi gi gi gi gi."
            menu:
                "Ok...I Will hug you so stop it already.":
                    mc_thought "(ok, she is too cute for me to treat her this way)"
                    mc "Ok ok, stop it already...I will hug you ok?"
                    # stops crying
                    show linda prologue happy with dissolve
                    pause 1.0

                    lin_shout "Really?"
                    mc "Yeah... its just a hug after all."
                    jump linda_hug
                "Stop Crying!":
                    mc_thought "(Man...she just wont stop)"
                    mc_shout "Stop Crying!"
                    # she stops and look at you
                    show linda prologue angry with dissolve
                    lin "Why are you yelling at me?"
                    mc "Because you cry too loud."
                    show linda prologue leaving1
                    lin "Okay then.....Im....Im gonna leave....ok?"
                    mc_thought "(Man...I never payed atention to this but....since when linda had such a beautifull ass?)"
                    show linda prologue leaving2
                    mc_thought "(Man...she is as beautifull as she goes.)"
                    show linda prologue leaving3
                    mc_thought "(It even crossed my mind to stop her....but is really fun to watch that beautifull ass ofher leaving like this.)"
                    show linda prologue leaving4
                    mc_thought "(Well...thats it..time to take the decision.)"
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
                        "Im sorry for making you cry.":
                            mc "Im sorry for make you cry."
                            lin "I see..."
                            mc "Came here and let me give you a big hug"
                            show linda prologue happy with dissolve
                            pause 1.0
                            lin_shout "Really?!?!? Oh [player.name]!!! I love you tooo thank you!!"
                            jump linda_hug
    return

label linda_hug:
    show linda prologue hug1 with dissolve
    # she hugs you
    lin "I really love your hugs, your hugs are just the best."
    mc_thought "(Cm to think of it...maybe this 'hug' thing...isnt bad at all...)"
    mc_thought "(Maybe I should...)"
    menu:
        "Enjoy the hug a little more":
            mc_thought "Yes, I think I will enjoy this \"hug\" a little more..."
            mc "I know right? I also love hugging you Linda."
            jump linda_enjoy_the_hug
        "Stop hugging":
            mc "Okay, thats enough hugging."
            jump linda_stop_hugging_prologue
    return

label linda_enjoy_the_hug:
    lin "You are just the best."
    show linda prologue hug2 with dissolve
    mc_thought "(Yes....like that...Thats an interesting view, Im loving it.....and that ass is just the best there is)"
    mc_thought "(Maybe I should....)"
    menu:
        "Try to (move your hand a little lower)":
            mc "..."
            show linda prologue hug3 with dissolve
            jump linda_enjoy_the_hug_2
        "Stop the Hug":
            mc "Okay, thats enough hugging."
            jump linda_stop_hugging_prologue
    return

# randomize phrases latter
label linda_enjoy_the_hug_2:
    lin "[player.name]?"
    mc "What?"
    lin "Isnt this hug taking a little too long?"
    menu:
        "I love hugging you" :
            mc "The thing is that I like huging my [linmc] like that."
            lin "Is that so? In that case...go on hug me all you like."
            jump linda_enjoy_the_hug3
        "You are right.":
            mc "You are right, im sorry linda, my mistake."
            lin "No, thats not what I meant!"
            lin "You can keep hugging me all you want."
            menu:
                "Nah, lets just stop.":
                    mc "no, lets just stop, it was a really long hug."
                    jump linda_stop_hugging_prologue
                "Continue hugging":
                    mc "I see, do you want to stop then?"
                    lin "No, I want to continue."
                    mc_thought "(Just as I thought.)"
                    jump linda_enjoy_the_hug3

label linda_enjoy_the_hug3:
    mc_thought "(Ok then...for the next step I think I will...)"
    mon_shout "Lindaaaa whats taking you so long?"
    lin "Thats mon calling...Sorry [player.name], I have to go now."
    menu:
        "Tell her to stay (requires courage > 3)" if courage > 3:
            "the course with courage"
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
    mc_shout "The Book?!?!?!??"
    lin "What? what book?"
    mc_thought "She can´t, She cant it??"
    
    show aphrodite throne during 4: 
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.12)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with dissolve
    aph_thought "\"Only you can truly read this.\""
    mc_thought "(Oh, I remember it now...So only I can see it.)"
    hide aphrodite with dissolve
    lin "[player.name], What book??" 
    mc "Sorry, I just remembered I have to return a book in the library today."
    lin "Anyway, leaviiiing."
    hide book
    show book shining:
            ypos -96 
    with dissolve
    mc_thought "(She left.)"
    mc_thought "(So it wasnt a dream after all.)"
    mc_thought "(This also explain a lot of my unusual behaviour with hugs this morning, I never looked at Linda this way, Its like im someone else.)"
    mc_thought "(I think I will like this Aphrodite champ thing. Anyway, lets open this book.)"
    show screen book
    show bedroom morning
    mc "It seems like this book will only show me girls I met after I got it. So no one I met before will appear. Interesting."
    # lin "Its ok if you want to hug me more big bro...I understand."
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
    ash "Dont try that with me brat."
    mc "What do you mean?"
    ash "I mean that I dont want people to think that Im related to a loser like you."
    mc "Jeez...why this now? whats the problem?"
    ash "The problem is that I have to look at your ugly face everyday, dont you have anywhere else so go?"
    mc "Monica let me stay here, so I have as much right to live here as you."
    ash "*Sigh* Yeah, whatever..."
    ash "Couldnt she at least pick a popular boy or someone that could actually an adventurer?"
    mc "I can still try."
    ash "Yeah... And fail as you always do."
    mc_thought "(Man she is such a drag... but she is kind of cute tho.)"
    ash "You dont even have a job."
    menu:
        "Not your business":
            mc "Thats none of your business."
        "Do YOU?":
            mc "Hmmm, do YOU have a job?"
    ash_shout "What did you just say??!?"
    mc "Nothing..."
    mc_thought "(Better not to pick a fight with her just yet.)"
    ash "Thats what I thought."
    mc "Do you know where Monica is?"
    ash "And why should I tell you?"
    mc_thought "(Geez, she wont let me be)"
    mc "Please?"
    ash "She is downstaris preparing your breakfast. Why? why she even bothers doing this kind of stuff to a loser like you?"
    mc "Maybe because she likes me?"
    ash "Pff, get real, I think she only let you in because its convenient."
    mc "What do you mean?"
    ash "I mean isn´t that obvious? Dad is always traveling, She is a mom with two daughers."
    ash "She probably adopted a boy so you could be strong, he could be the man and help the house. While dad is traveling."
    ash "But Here you are, small and weak, such a disappointment."
    menu:
        "I could become a powerfull mage":
            mc "Maybe someday I can become a powerfull mage you know."
            ash "A Loser like you? dont make me laugh, you probably don´t have any magical blood on you."
        "I could become a powerfull warrior":
            mc "Maybe someday I can become a really strong warrior you know."
            ash "A loser like you? dont make me laugh, with your body you can´t even beat ME in a fight."
    ash "With your age all warrior were strong and all wizards heirs had theyr powers awakened and you have none, so stop dreaming about it."
    mc "I will grow up and be awesome, wait and see."
    hide ashley
    show ahsley half sleepover happy
    with dissolve
    ash_shout "Hahahaha, you are so funny."
    mc "..."
    ash "..."
    scene hallway morning
    show ashley half sleepover angry2
    with dissolve
    ash "Wait that wasn´t a joke?...oh you are more dumb than I thought, do whatever you want."
    mc_thought "(Man, she is sush a drag...doesn´t she know she is talking to aphrodite chosen one?)"
    mc_thought "She left..."
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
        mon "Oh, good morning sweet, how was your night?"
        mc "Good morning Monica, it was good thank you."
        mon "I made you breakfast."
        mc "Thank you Monica, but Im really not that hungry right now."
        show monica half talking2
        with dissolve
        mon "Are you sure? I made your favorite 3 eggs and bacon and warm milk, not too hot, not too cold, just warm, the way you like it."
        # ashley enters and sees you two
        mc "Monica You didnt need to, but you are simply the best, Thanks, Im going to eat it!"
        show monica half happy
        with dissolve
        mon "Oh you dont need to thank me sweetie, And please dont call me Monica, you call me \"Mon\" if you want to."
        show monica half talking3
        with dissolve
        mon "So, today is the big day isn´t it?"
        menu:
            "Big day?":
                show monica half talking2
                with dissolve
                mc "Big day?"
                mon "Yes the big day."
            "Oh...yes...the big day....":
                show monica half talking
                with dissolve
                mon "Oh sweet, dont tell me you forgot about today?"
        mc "..."
        show monica half talking
        mon "Yes, you told me that you would help me in the {color=#4d0537}flower fields{/color} while you dont find a work."
        mc_thought "(Wait, flower fields, dont I have a world to conquer? Nah she is so sweet I can´t say no to her.)"
        mc "I see, so today is my first day helping on the flower fields. I will be glad to help."
        $ ui_show_top_screen = True
        $ monica.revealed = True
        $ monica.book_phrase = "Go help her in the flower camp."
        $ monica_prologue = False
        $ ui_can_change_map = True
        return


