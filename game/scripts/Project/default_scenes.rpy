label input_player_name:
    $ player.name = renpy.input("What is your name?", length = 21, default = "Bill" )
    define mc = Character("[player.name]", namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"), what_outlines=[ (2, "#202121") ], what_color = "#f1f0f3", image = "mc")
    define mc_shout = Character("[player.name]", what_size = 37, namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"), what_outlines=[ (2, "#202121") ], what_color = "#f1f0f3", image = "mc")
    define mc_thought = Character("[player.name] Thought", what_color = "#f1f0f3", namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"), what_outlines=[ (2, "#202121") ],  image = "mc")
    define mc_whisper = Character("[player.name]", what_size = 14, namebox_background=AlphaMask(Solid("#35406d"), "gui/namebox.png"), what_outlines=[ (2, "#202121") ], what_color = "#f1f0f3" , image = "mc") 
    menu:
        mc "My name is [player.name]"
        "Confirm":
            jump input_characters_relations
        "Change name":
            jump input_player_name
        # "Cheat:: ":
        #     jump start_3
        # "Cheat2":
        #     $ location = "forest wall"
        #     jump start_3

label age_check:
    scene black with Dissolve(0.5)
    centered "All the characters in this story are 18+"
    centered "This game contains content of adult nature and is not suited for audiences  below the age of 18. If you are easily offended or are under the age of 18, close the game now."
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
        pos (0.0, 0.0) yzoom 1.0 xzoom 1.0 zoom 1.0
    return
    
label sleep_from_where:
    $ sleep_when_enter = True
    $ dont_show_map_image = True
    call change_location_to("Bedroom")
    scene black with dissolve
    return