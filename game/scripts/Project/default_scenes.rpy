label input_player_name:
    $ player.name = renpy.input("What is your name?", length = 21, default = "Bill" )
    default mc = Character("[player.name]", namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"))
    default mc_shout = Character("[player.name]", what_size = 37, namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"))
    default mc_thought = Character("[player.name]", what_color = "#98969E", namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"))
    default mc_whisper = Character("[player.name]", what_size = 14, namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"))
    menu:
        mc "My name is [player.name]"
        "Confirm":
            jump input_characters_relations
        "Change name":
            jump input_player_name
        "Cheat":
            jump start_3
        "Cheat2":
            $ location = "forest wall"
            jump start_3

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

label start_3:
    call start_time_variables
    # show  screen top_screen
    call enter_map
return

label camera_reset:
    camera:
        pos ( 0, 0) yzoom 1.0 zoom 1.0 