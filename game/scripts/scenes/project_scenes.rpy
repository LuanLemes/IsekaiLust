


label input_characters_name:

    "These three girls are Monica, Ashley and Linda, (Mother and her dauthers), they will live with you during the game, but what are they to you?"
    $ monicamc = renpy.input("Monica (left one) is your (default landlady)?", length = 14, default = "landlady" )
    $ mcmon = renpy.input("And you are her? (default tenant)", length = 14, default = "tenant")

    $ ashmc = renpy.input("Ashley (Middle one) is your?", length = 14, default = "friend" )
    $ mcash = renpy.input("And you are her (default friend)", length = 14, default = "friend" )

    $ linmc = renpy.input("Linda (Right one) is your(default friend?)", length = 14, default = "friend" )
    $ mclin = renpy.input("And you are her? (default friend)", length = 14, default = "friend")

    $ monicamc = str(monicamc.lower())
    $ mcmon = str(mcmon.lower())

    $ ashmc = str(ashmc.lower())
    $ mcash = str(mcash.lower())

    $ linmc = str(linmc.lower())
    $ mclin = str(mclin.lower())

    "So Monica , is your {color=#4d0537}[monicamc]{/color} and you are her {color=#4d0537}[mcmon]{/color}."
    "Ashley is your {color=#4d0537}[ashmc]{/color} and you are her {color=#4d0537}[mcash]{/color}."
    menu:
        "And Linda is your {color=#4d0537}[linmc]{/color} and you are her {color=#4d0537}[mclin]{/color}? Is that right?"
        "Yes":
            "Alright."
            jump prologue
        "No":
            "Lets fix that then."
            jump input_characters_name
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
    mc_thought "Who am I again?"
    mc_thought "Well...the thing is...I used to live in a world pretty much like yours."
    mc_thought "I was a nerd boy in my original life, I was a small boy, my dick was small, and I didnt get any girls in my life."
    mc_thought "They always like the popular type more... So I never stood a chance."
    mc_thought "Even so one day I took corage and decided to talk with the girl I liked... and that really, really, really didnt end well."
    mc_thought "She took me to a room and told me to strip naked and I did it."
    mc_thought "When I asked if she would´t join me she said. She said she would be crazy to be with a guy like me, she even made fun and said my dick was too small."
    mc_thought "The thing is...I didnt know was, she was recording everything. The next days she blackmaild me."
    mc_thought "She made me an offer. \"You will be my dog you will obey everything I tell you to do and I will be your Queen.\" or I will show the video to everyone even your family."
    mc_thought "I accepted it and she took advantage of me, she made me carry her stuff, do her homework, she even would insult me in front of my own friends."
    mc_thought "Im not proud of it, im just telling the truth."
    mc_thought "One she left the city and I continued my lowlife, I was finaly free but...still a loser."
    mc_thought "One day I decided to buy a hentai game."
    mc_thought "This one....{b}(Cronicles of Aprhodite){/b}?....this one, this one should be good."
    mc_thought "I thought the lady of the front was hot so.....anyway."
    mc_thought "As son as I got home I went to play it."
    aph "Do you want to become the goddes Aphrodite powerfull champion, to live an awesome adventure with lots of sex and action?"

    mc_thought "And I wonder...till this day...why..why why did I click yes?"
    mc_thought "I dont know what kind of black magic was on that game."
    mc_thought "Because I ended in a world full of fantasy and magic yes."
    mc_thought "But I wasnt powerfull, I didnt become any goddes champion and sure as hell I didnt have sex till this day."
    mc_thought "After almost starving to death in a lot of ocasions, I got rescued by a lovely lady."
    mc_thought "She took care of me and ofered me a room on her house. She lives with her two daughers, and now me too."
    mc_thought "The younger one is cute and lovely, the older one...not so much."
    mc_thought "I tried many times to become a member of the guild, but they said Im not strong enough, nor I have any magic on me."
    mc_thought "So...thats it, today Is my birthday...18 years old and I didnt even care to tell anyone. I mean...there is nothing to  celebrate....Im still a total loser."
    mc "Anyway.. at least I have a home now...better go to sleep."


label prologue_1:
    # white_screen
    aph "[player.name]...[player.name]....Awake..."
    # aphrodite appears on the screen (giant)
    mc "What? What is it? Omg it is you you are the girl from the message on my game! I this a Dream?"
    aph "You accepted my call, and now you are my champion in this world."
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
    aph_shout "Silence!!!"
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
            aph_thought "(In the name of the great Me...what are humans doing these days?)"
        "Not at all":
            aph_thought "(Oh My... what are humans doing thinking these days?)"
    aph_shout "Im The Great Aphrodite!"
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
    aph_shout "Shut up mortal!"
    aph "And Sex and casual sex, fellatios, sexual pleasure and orgys….anal sex vaginal sex double penetration sex and......."
    aph "The Goddes creampies and pee action and cum and bukkakes and public sex and furry and….."
    "..."
    "That did go on for 20 minutes or so........"
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
        mc_thought "(oh my god)"
        aph "Yes I saw you getting hard and masturbating every day again and again and again."
        mc_thought "(what in the harry potter?!?)"
        mc "Ok I think I got it…"
        aph "I saw as you were aroused for the little things, and as you imagined fucking every cute girl in your schooll…and as you masturbated to them in secret."
        mc_thought "(I cant believe i just cant believe...)"
        mc "Ok that was suposted to be private..."
        aph "I even know about last summer on the vacation with your family when you masturbated and cum in the...."
        mc_shout "Okay I think I got it!!!"
        aph "Anyway, In opinion yes you are a great boy, and this {b}task{/b} will be both good for you and for the people of this world."
        mc_thought "(\"Task\" I knew it...I knew there was a catch)"
        menu:
            "Task?":
                mc "Task? What task?"
            "What do you mean by task?":
                mc "What do you mean by task?"
        jump task

    label task:
        aph "Of course...your task as my champion is to conquer and fuck all the girls in this world and to realease the lustfull side of the people of the planet."
        mc_shout "I knew it!"
        mc "Wait...conquer this worlds and fuck all the girls? Did I hear that right?"
        aph "Yes you did, you are to conquer this world fuck all the girls in this wolrd... no exception, friend or enemy."
        aph "They all are to be conquered and fucked. No exceptions allowed. And you are to make them more and more lustfull for you."
        mc_thought "(Well....that seems like fun, very very very fun.)"
        mc "Well...After taking a lot of thought..."
        mc "Well...I accept your terms."
        aph "As I said, You have already signed the contract."
        mc "Hey Goddes."
        aph_shout "Its \"Great Goddes Aphrodite\""
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
    mc "I mean.... Im ugly, I got a very small dick and Im not very social..."
    aph "Little [player.name], you are in the hands of the Goddess of Pleasure now."
    aph "I give you The {i} {color=#4d0537}Bless of the magic blood of the sex warlocks and my power{/i}{/color} with it."
    mc_thought "(\"Magic blood of Warlocks of sex? and her power?\")"
    aph "Also a little gift from your Goddes... {color=#4d0537}This Book.{/color}"
    menu:
        "A book?":
            mc "A Book....Really?"
        "Is that a joke?":
            mc "A Book..is That a Joke?"
    aph "No Joke Dear [player.name]. Only you can truly read this book, besides me of course."
    aph "This book has the power to know the path for everyone pleasure, use it wisely."
    mc "But thats a book!! how will I be able to..."
    aph "Relax......and sleep."
    jump awake_at_home

label awake_at_home:
    mc "It was just a dream...after all."
    lin "Hi [linmc], did you sleep well?"
    mc "Liiiiinda what are you doing here?!?!?"
    lin "{color=#4d0537}Mom{/color} told me to wake you up, she said {color=#4d0537}she needs to talk with you.{/color}"
    lin "[player.name]?"
    mc "Good morning Linda..."
    lin "Good morning [mclin]."
    mc "Where is monica?"
    lin "Well, she is in the Kitchen I think."
    mc "Ok, Well guess its time to wake up."
    lin "Step Bro are you Ok?"
    menu:
        "I am":
            mc "I am very ok, thanks for asking."
            lin "No you arent."
            mc "What do you mean?"
            lin "You didnt say \"I love you\". "
        "Why do you ask?":
            mc "I...think I am, why do you ask?"
            lin "Well...you havent told you love your little step sister...thats not like you.."
    mc "What?"
    mc_thought "Wow, she is really serious about it..."
        # she makes a face
    mc_thought "She is even making a face now, guess she is really mad about it."
    jump linda_do_you_love_me
    return


label linda_do_you_love_me:
    lin "So...will you say you love me or not?"
    menu:
        "I love you":
            mc "I love you."
            # she smiles
            lin "I love you too big bro."
            jump linda_hug
        "No I wont say that":
            mc "No I wont, you are already too grown up for this kind of stuff."
            lin "Why are you mean to me step bro?"
            mc "As I Said you are already a Grown up."
            lin "Gi gi gi gi gi gi gi gi gi gi gi gi gi"
            mc_Thought "(Geeeez what is this? is she crying? what a strange way to cry)"
            menu:
                "Ok...I love you so stop it already.":
                    mc_thought "(ok, she is too cute for me to treat her this way)"
                    mc "Ok ok, stop it already...I love you ok?"
                    # stops crying
                    lin "Really?"
                    mc "Yeah... now go"
                "Stop Crying!":
                    mc_thought "(Man...she just wont stop)"
                    mc_shout "Stop Crying!"
                    # she stops and look at you
                    lin "Why are you yelling at me?"
                    mc "Because you cry too loud"
                    lin "Okay...Im....Im gonna leave....ok?"
                    # she leaves slowsly
                    mc_thought "(She is so cute, she is like a cute pet, I cant leave her like that)"
                    mc "Hey little sister"
                    # she looks at you
                    lin "what?"
                    menu:
                        "I love you little sister.":
                            mc "I love you."
                            lin "Really big bro?!!?!? I love you too! you are the best!!"
                        "Im sorry for making you cry.":
                            mc "Im sorry for make you cry."
                            lin "I see..."
                            mc "And I really love you"
                            linda_shout "Really?!?!? Oh big bro!!! I love you tooo thank you!!"
                            # she leaves
    return

label linda_hug:
    # she hugs you
    mc_thought "(Wow she has a pretty amazing body for a little sister. Maybe I should...)"
    menu:
        "Stop hugging":
            mc "Okay, thats enough hugging."
            jump linda_stop_hugging
        "Enjoy the hug a little more":
            mc_thought "Yes, I think I will enjoy this \"hug\" a little more..."
            jump linda_enjoy_the_hug
    return

label linda_enjoy_the_hug:
    mc_thought "(Yes....like that...Thats an interesting view, Im loving it.)"
    menu:
        "Enjoy a little more":
            jump linda_enjoy_the_hug_2
        "Stop the Hug":
            jump linda_stop_hugging
    return

# randomize phrases latter
label linda_enjoy_the_hug_2:
    lin "Big bro?"
    mc "What?"
    lin "Isnt this hug taking a little too long?"
    menu:
        "I love hugging you":
            mc "The thing is that I like huging my little step sister."
            lin "Is that so? In that case...go on hug me all you like."
        "You are right.":
            mc "You are right little Linda."
            jump linda_stop_hugging
        "Stop Hugging":
            mc_thought "(Okay)"
            jump linda_stop_hugging

# randomize phrases latter
label linda_stop_hugging:
    mc_thought "(Man that was one good way to start a day.)"

    # lin "Its ok if you want to hug me more big bro...I understand."
    jump start_3
    return

label ashley_prologue:
    # scene
    mc "Good Ashley."
    ash "Dont try that with me brat."
    mc "What do you mean?"
    ash "I mean that I dont want people to think that Im related to a loser like you."
    mc "Jeez...why this now? whats the problem?"
    ash "The problem is that I have to look at your ugly face everyday, dont you have anywhere else so go?"
    mc "Monica let me stay here, so I have as much right to live here as you."
    ash "*Sigh* Yeah, whatever..."
    ash "Couldnt she at least pick a popular boy or someone that could turn into an adventurer?"
    mc "I can still try"
    ash "Yeah... And fail as you always do"
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
    ash "She is downstaris preparing you breakfast. Why? why she even bothers doing this kind of stuff to a loser like you?"
    mc "Maybe because she likes me."
    ash "Pff, get real, I think she fells sorry for you."
    mc "What do you mean?"
    ash "I mean isn´t that obvious? Dad is always traveling, She is a mom with two daughers."
    ash "She probably adopted a boy so you could be strong, he could be the man and help the house. While dad is traveling"
    ash "But Here you are, small and weak, such a disappointment."
    menu:
        "I could turn into a powerfull mage":
            mc "Maybe someday I can turn into a powerfull mage you know."
            ash "A Loser like you? dont make me laugh, you probably don´t have any magical blood on you."
        "I could turn into a powerfull warrior":
            mc "Maybe someday I can turn out to be really strong you know."
            ash "A loser like you? dont make me laugh, with your body you can´t even beat me in a fight."
    ash "with your age all warrior were strong and all wizards heirs had theyr powers awakened and you have none, so stop dreaming about it."
    mc "I will grow up and be awesome, wait and see."
    ash_shout "Hahahaha, you are so funny."
    mc "..."
    ash "Wait that wasn´t a joke?...oh you are more dumb than I thought, do whatever you want."
    mc_thought "(Man, she is sush a drag...doesn´t she know she is talking to aphrodite chosen one?)"
    #  she leaves
    return

    label monica_prologue:
        mon "Oh, good morning sweet, how was your night?"
        mc "Good morning Monica, it was good thank you."
        mon "I made you breakfast."
        mc "Thank you Monica, but Im really not that hungry right now."
        mon "Are you sure? I made your favorite 3 eggs and bacon and warm milk, not too hot, not too cold, just warm, the way you like it."
        # ashley enters and sees you two
        mc "Monica You didnt need to, but you are simply the best, Thanks!"
        mon "Oh you dont need to thank me sweetie, And please dont call me Monica, you call me \"Mon\" if you want to."
        mc "Thanks \"Mon\"."
        mon "Oh you are so sweet."
        mon "So, today is the big day isn´t it?"
        menu:
            "Big day?":
                mc "Big day?"
                mon "Yes the big day."
            "Oh...yes...the big day....":
                mon "Oh sweet, dont tell me you forgot about today?"
        mc "..."
        mon "Yes, you told me that you would help me in the {color=#4d0537}flower fields{/color} while you dont find a work."
        mc_thought "(Wait, flower fields, dont I have a world to conquer? Nah she is so sweet I can´t say no to her.)"
        mc "I see, so today is my first day helping on the flower fields. I will be glad to help."
        # ashley makes a angry face
        return

    label flower_camp_first:
        # monica appears
        mon "Oh so here you came after all"
        lin "[mclin] you are here!!!"
        mc "Yes I did, so, can I help you with something?"
        mon "Yes you can, I thought since you didnt became an adventure yet you could help us on the field so you could get some money."
        mc "I see, Im ready to help you!!!"
        mon "Oh you are so sweet."
        mon "Right, so what you need to do is to collect flowers and herbs, afterwards {color=#4d0537}On fridays you can sell them to the magister.{/color}"
        $ flowers_cap_first = False
        jump flower_camp
        return
