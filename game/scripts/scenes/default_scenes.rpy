label input_player_name:
    $ player.name = renpy.input("What is your name?", length = 21 )
    $ p_char = Character("[player.name]", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    $ p_char_shout = Character("[player.name]", what_size = 37, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    $ p_char_thought = Character("[player.name]", what_color = "#98969E", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    menu:
        p_char "My name is [player.name]"
        "Confirm":
            call prologue
        "Change name":
            call input_player_name


label age_check:
    "This game have NSFW contents"
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
    aphrodite "[player.name]...[player.name]....Awake"
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
        p_char "Ok I think I got it…"
        aphrodite "I saw as you were aroused for the little things, and as you imagined fucking every cute girl in your schooll…and as you masturbated to them in secret."
        p_char "Ok I think thats enough..."
        aphrodite "I even know about last summer on the vocation with your family when you masturbated and cum in the...."
        p_char_shout "OOkay I think I got it!!!"
        aphrodite "Anyway, In opinion yes you are a great boy, and this {b}task{/b} will be both good for you and for the people of this world."
        p_char_thought "(I knew it...I knew there was a catch)"
        menu:
            "task?":
                p_char "Task? What task?"
            "What do you mean by task?":
                p_char "What do you mean by task?"
        jump task

    label task:
        aphrodite "Of Course...your task as my champion if to fuck all the girls in this world and to realease the lustfull side of the people of the planet"
        p_char_shout "I knew it!"
        p_char "Wait...fuck all the girls? Did I hear that right?"
        aphrodite "Yes you did, you are to fuck all the girls in this wolrd... no exception, friend or enemy, strange or even your own family."
        aphrodite "They all are to be fucked. No exceptions allowed. And you are to make them more and more lustfull for you."
        p_char_thought "(Well....that seems like fun, very very very fun.)"
        p_char "Well...I accept your terms"
        aphrodite "As I said, You have already signed the contract."
        p_char "Hey Goddes"
        aphrodite_shout "Great Goddes Aphrodite"
        p_char "Ok... Great Goddes Aphrodite...."
        P_char"Not Willing to borther you but..."
        menu
            "how the hell am i supposed to do that?!?":
                p_char "how the hell am I supposed to do that?!?!?"
            "I can´t do that":
                p_char "I dont know how much of my life you saw but...Im not the kind of person that can fuck every girl in a world"
        jump how
        return

label how:
    p_char "I mean.... Im ugly, I got a very small dick and Im not very social..."
    aphrodite "Little [player.name], you are in the hands of the goddess of pleasure now."
    aphrodite "I give you The {i} Bless of the blood of the sex warlocks and my power in it{/i}."
    aphrodite "Also a little gift from your Goddes... This Book."
    menu:
        "A book?":
        p_char "A Book....Really?"
        "Is that a joke?"
        p_char "A Book..is That a Joke?"
    aphrodite "No Joke Dear [player.name]. Only you can truly read this book, besides me of course."
    aphrodite "This book has the power to know the path for everyone pleasure, use it wisely."
    p_char "But thats a book!! how will I be able to..."
    aphrodite "Relax......and sleep"
