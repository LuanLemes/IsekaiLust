label input_player_name:
    $ player.name = renpy.input("What is your name?", length = 21 )
    $ p_char = Character("[player.name]", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    $ p_char_shout = Character("[player.name]", what_size = 37, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    $ p_char_thought = Character("[player.name]", what_color = "#98969E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    menu:
        p_char "My name is [player.name]"
        "Confirm":
            jump prologue
        "Change name":
            jump input_player_name


label age_check:
    "This game have NSFW contents."
    menu:
        "Are you +18 years old?"
        "Yes":
            jump start_2
        "No":
            "Maybe in a few more years then"
            jump finish_game


label finish_game:
    return


label start_2:
    # scene temp_bed
    call input_player_name
return



label start_3:
    call start_time_variables
    show screen top_screen
    call enter_map
return


label active_quick:
    $ quick_menu = True
    return


label deactive_quick:
    $ quick_menu = False
    return


label prologue:
    # white_screen
    aphrodite "[player.name]...[player.name]....Awake..."
    # aphrodite appears on the screen (giant)
    p_char "What? What is it? Omg it is you you are the girl from the message on my game!"
    aphrodite "You accepted my call, and now you are my champion in this world."
    p_char "Whaaaaat?!?!?"
    menu:
        "What do you mean by champion?":
            p_char "What do you mean by champion?"
            jump champion
        "Im not your champion!":
            p_char_shout "Im not your champion!"
            aphrodite "Oh...Arent you?"
            jump champion
    return

label champion:
    aphrodite "You clicked yes on the message didnt you?"
    p_char_shout "Thats not how it works!!!"
    p_char "You cant just send someone to another universe just because they clicked \"yes\" on some random message."
    aphrodite "There was a contract and you agreed to it, thats is all. Now  you are my serve and my champion."
    # p_char "(Came to think of it, it makes sense....I mean because damn she is beautifull)"
    aphrodite "There is no way to go back, besides, there are very good advantages in being the {b}Goddes of pleasure{/b} champion."
    menu:
        "I dont care who you are!":
            p_char_shout "I dont care who you are!!!"
            p_char "Wait...{b}Goddes of Pleasure?{/b}"
            jump goddes_of_pleasure
        "Goddes of Pleasure?":
            p_char "\"{b}Goddes of Pleasure{/b}\"???"
            jump goddes_of_pleasure

    return

label goddes_of_pleasure:
    aphrodite "Are you saying that you never heard of the goddess of pleasure, {b}The Great Aphrodite?{/B}"
    menu:
        "Im sorry no":
            aphrodite_thought "(In the name of the great Me...what are humans doing these days?)"
        "Not at all":
            aphrodite_thought "(Oh My... what are humans doing thinking these days?)"
    aphrodite_shout "Im The Great Aphrodite!"
    aphrodite_shout "the Goddes of pleasure!"
    aphrodite "the Goddes of sex."
    aphrodite "Goddes of  and all that there is to do with masturbation."
    aphrodite "The Goddes of...gangbangs and threesomes"
    aphrodite "The Goddes of foursomes and fivesomes"
    aphrodite "The Goddes of..."
    menu:
        "Ok I get it":
            p_char "Ok...I think I get it"
        "I think I understood":
            p_char "...I Think....I understood..."
    aphrodite "Shut up mortal!"
    aphrodite "And Sex and casual sex, fellatios, sexual pleasure and orgys….anal sex vaginal sex double penetration sex and......."
    aphrodite "The Goddes creampies and pee action and cum and bukkakes and public sex and fury and….."
    "..."
    "That did go on for 20 minutes or so........"
    menu:
        "Why me?":
            p_char "I Understand but...why me?"
        "Wasnt there anybody else for this job?":
            p_char "I See but...wasnt there anybody else for this job?"
    jump why_me

    return

    label why_me:
        aphrodite "Well, I can see all living creatures in all universes, and you [player.name] between the most sexual  beings in all universe."
        p_char "Am I?"
        aphrodite "Yes you are, I see you watching reading and researching porns and hentais everyday."
        p_char_thought "(oh my god)"
        aphrodite "Yes I saw you getting hard and masturbating every day again and again and again."
        p_char_thought "(what in the harry potter?!?)"
        p_char "Ok I think I got it…"
        aphrodite "I saw as you were aroused for the little things, and as you imagined fucking every cute girl in your schooll…and as you masturbated to them in secret."
        p_char_thought "(I cant believe i just cant believe...)"
        p_char "Ok that was suposted to be private..."
        aphrodite "I even know about last summer on the vocation with your family when you masturbated and cum in the...."
        p_char_shout "OOkay I think I got it!!!"
        aphrodite "Anyway, In opinion yes you are a great boy, and this {b}task{/b} will be both good for you and for the people of this world."
        p_char_thought "(\"Task\" I knew it...I knew there was a catch)"
        menu:
            "Task?":
                p_char "Task? What task?"
            "What do you mean by task?":
                p_char "What do you mean by task?"
        jump task

    label task:
        aphrodite "Of Course...your task as my champion is to fuck all the girls in this world and to realease the lustfull side of the people of the planet"
        p_char_shout "I knew it!"
        p_char "Wait...fuck all the girls? Did I hear that right?"
        aphrodite "Yes you did, you are to fuck all the girls in this wolrd... no exception, friend or enemy, strange or even your own family."
        aphrodite "They all are to be fucked. No exceptions allowed. And you are to make them more and more lustfull for you."
        p_char_thought "(Well....that seems like fun, very very very fun.)"
        p_char "Well...After taking a lot of thought..."
        p_char "Well...I accept your terms."
        aphrodite "As I said, You have already signed the contract."
        p_char "Hey Goddes."
        aphrodite_shout "Its \"Great Goddes Aphrodite\""
        p_char "Ok... Great Goddes Aphrodite...."
        p_char "Not Willing to borther you but..."
        menu:
            "How the hell am i supposed to do that?!?":
                p_char "How the hell am I supposed to do that?!?!?"
            "I can´t do that":
                p_char "I dont know how much of my life you saw but...Im not the kind of person that can fuck every girl in a world."
        jump how
        return

label how:
    p_char "I mean.... Im ugly, I got a very small dick and Im not very social..."
    aphrodite "Little [player.name], you are in the hands of the Goddess of Pleasure now."
    aphrodite "I give you The {i} Bless of the magic blood of the sex warlocks and my power in it{/i}."
    p_char_thought "(\"Magic blood of Warlocks of sex? and her power?\")"
    aphrodite "Also a little gift from your Goddes... This Book."
    menu:
        "A book?":
            p_char "A Book....Really?"
        "Is that a joke?":
            p_char "A Book..is That a Joke?"
    aphrodite "No Joke Dear [player.name]. Only you can truly read this book, besides me of course."
    aphrodite "This book has the power to know the path for everyone pleasure, use it wisely."
    p_char "But thats a book!! how will I be able to..."
    aphrodite "Relax......and sleep."
    jump awake_at_home

label awake_at_home:
    p_char "It was just a dream...after all"
    linda "Hi step bro, did you sleep well?"
    p_char "Liiiiinda what are you doing here?!?!?"
    p_char_thought "(Wait...How do I know her name is Linda? This is just so strange.....Im Not from this world and I know her name, I even have memoirs with her.)"
    p_char_thought "(I Remember I was adopted, the people, the names and everything, thats awesome.)"
    p_char_thought "(Well...I guess thats all part of Aprhodite´s power.)"
    linda "Step Bro?"
    p_char "Good morning Linda..."
    p_char_thought "(Seems like I also know theyr language and culture as well.)"
    linda "Good morning step bro."
    p_char "Where is Step Mom?"
    p_char_thought "(Wait...Step Mom? At Least I think remember having one, man thats so strange.)"
    linda "Well, she is in the Kitchen I think."
    p_char "Ok, Well guess its time to wake up."
    linda "Step Bro are you Ok?"
    p_char_thought "(Oh no, she is looking at me weird, am I acting so different? I have to be \"myself\" or she will suspect.)"
    menu:
        "I am":
            p_char "I am very ok thanks for asking."
            linda "No you arent."
            p_char "What do you mean?"
            linda "You didnt say \"I love you\". "
        "Why do you ask?":
            p_char "I...think I am, why do you ask?"
            linda "Well...you havent told you love your little step sister...thats not like you.."
    p_char "What?"
    p_char_thought "Wow, she is really serious about it..."
        # she makes a face
    p_char_thought "She is even making a face now, guess she is really mad about it."
    jump linda_do_you_love_me
    return


label linda_do_you_love_me:
    linda "So...will you say you love me or not?"
    menu:
        "I love you":
            p_char "I love you."
            # she smiles
            linda "I love you too big bro."
            jump linda_hug
        "No I wont say that":
            p_char "No I wont, you are already too grown up for this kind of stuff."
            linda "Why are you mean to me step bro?"
            p_char "As I Said you are already a Grown up."
            linda "Gi gi gi gi gi gi gi gi gi gi gi gi gi"
            p_char_Thought "(Geeeez what is this? is she crying? what a strange way to cry)"
            menu:
                "Ok...I love you so stop it already.":
                    p_char_thought "(ok, she is too cute for me to treat her this way)"
                    p_char "Ok ok, stop it already...I love you ok?"
                    # stops crying
                    linda "Really?"
                    p_char "Yeah... now go"
                "Stop Crying!":
                    p_char_thought "(Man...she just wont stop)"
                    p_char_shout "Stop Crying!"
                    # she stops and look at you
                    linda "Why are you yelling at me?"
                    p_char "Because you cry too loud"
                    linda "Okay...Im....Im gonna leave....ok?"
                    # she leaves slowsly
                    p_char_thought "(She is so cute, she is like a cute pet, I cant leave her like that)"
                    p_char "Hey little sister"
                    # she looks at you
                    linda "what?"
                    menu:
                        "I love you little sister.":
                            p_char "I love you."
                            linda "Really big bro?!!?!? I love you too! you are the best!!"
                        "Im sorry for making you cry.":
                            p_char "Im sorry for make you cry."
                            linda "I see..."
                            p_char "And I really love you"
                            linda_shout "Really?!?!? Oh big bro!!! I love you tooo thank you!!"
                            # she leaves
    return

label linda_hug:
    # she hugs you
    p_char_thought "(Wow she has a pretty amazing body for a little sister. Maybe I should...)"
    menu:
        "Stop hugging":
            p_char "Okay, thats enough hugging."
        "Enjoy the hug a little more":
            p_char_thought "Yes, I think I will enjoy this \"hug\" a little more..."
            jump linda_enjoy_the_hug
    return

label linda_enjoy_the_hug:
    p_char_thought "(Yes....like that...Thats an interesting view, Im loving it.)"
    menu:
        "Enjoy a little more":
            jump linda_enjoy_the_hug_2
        "Stop the Hug":
            jump linda_stop_hugging
    return

# randomize phrases latter
label linda_enjoy_the_hug_2:
    linda "Big bro?"
    p_char "What?"
    linda "Isnt this hug taking a little too long?"
    menu:
        "I love hugging you":
            p_char "The thing is that I like huging my little step sister."
            linda "Is that so? In that case...go on hug me all you like."
        "You are right.":
            p_char "You are right little Linda."
            jump linda_stop_hugging
        "Stop Hugging":
            p_char_thought "(Okay)"
            jump linda_stop_hugging

# randomize phrases latter
label linda_stop_hugging:
    p_char_thought "(Man that was one good way to start a day.)"
    linda "Its ok if you want to hug me more big bro...I understand."
    jump start_3
    return
