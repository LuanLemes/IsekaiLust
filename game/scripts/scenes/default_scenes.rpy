label input_player_name:
    $ player.name = renpy.input("What is your name?", length = 21 )
    $ p_char = Character("[player.name]", namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
    $ p_char_shout = Character("[player.name]", what_size = 43, namebox_background=AlphaMask(Solid("#FF7F7F"), "gui/namebox.png"))
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
            jump champion
        "Im not your champion!":
            Aphrodite "Oh...Arent you?"
            jump champion
    return

label champion:
    aphrodite "Yes, you clicked yes on the message didnt you?"
    p_char_shout "Thats not how it works!!!"
    p_char "you cant just send someone to another universe just because they clicked \"yes\" on some random message."
    aphrodite "There was a contract and you agreed to it, thats is all. Now  you are my serve and my champion."
    # p_char "(Came to think of it, it makes sense....I mean because damn she is beautifull)"
    aphrodite "There is no way to go back, besides, there are very good advantages in being the {b}Goddes of pleasure{/b} champion."
    return
