label close_book:
    hide screen inventory
    return

    style character_screen_text:
        color "#FFFFFF"
        size 30
        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

screen book():
    default grid_y_size = 3
    modal True
    zorder 2

    frame:
        background Frame("yellow sky.webp")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1920-100
        ysize 1080-70
        background Solid("#000000a8")
    text "Book of Aphrodite" xalign 0.5 yalign 0.05 color"#ffffffff" size 80 outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

    textbutton "X":
        text_style "x_button"
        action Hide("book")
        xalign 0.97
        yalign 0.025

    grid 7 grid_y_size:
        spacing 30
        xalign 0.5
        yalign 0.5
        default offset_size = 7 * grid_y_size - len(all_girls)

        for girl in all_girls:
            # default this_image = str(girl.image_link + ".webp")
            if girl.revealed == True:
                frame:
                    background Solid("#00000000")
                    xysize(192,108)
                    imagebutton:
                        xoffset 37
                        yoffset -18
                        hover im.Scale( "sky background hover.webp" ,192,108)
                        idle im.Scale( "sky background.webp" ,192,108)
                        action [Show("character_screen", dissolve, girl.id)]
                    imagebutton :
                        focus_mask True
                        xoffset 37
                        yoffset -18
                        hover im.Scale( "character_screen/" + girl.name + ".webp" ,192,108)
                        idle im.Scale( "character_screen/" + girl.name + ".webp" ,192,108)
                        action [Show("character_screen", dissolve, girl.id), ]
                    imagebutton :
                        focus_mask True
                        xoffset 37
                        yoffset -18
                        hover im.Scale( "visible background.webp" ,192,108)
                        idle im.Scale( "transparent background.webp" ,192,108)
                        action [Show("character_screen", dissolve, girl.id), ]


            else:
                frame:
                    background Solid("#00000000")
                    xysize(192,108)                
                    imagebutton:
                        xoffset 37
                        yoffset -18
                        hover im.Scale( "sky background hover.webp" ,192,108)
                        idle im.Scale( "sky background.webp" ,192,108)
                        action [Show("character_screen", dissolve, girl.id)]
                        # focus_mask im.Scale( "sky background hover.webp" ,192,108)
                    imagebutton:
                        focus_mask True
                        xoffset 37
                        yoffset -18
                        hover im.Scale( "character_screen/" + girl.name + " hidden.webp" ,192,108)
                        idle im.Scale( "character_screen/" + girl.name + " hidden.webp" ,192,108)
                        action [Show("character_screen", dissolve, girl.id)]
                    imagebutton :
                        focus_mask True
                        xoffset 37
                        yoffset -18
                        hover im.Scale( "visible background.webp" ,192,108)
                        idle im.Scale( "transparent background.webp" ,192,108)
                        action [Show("character_screen", dissolve, girl.id), ]
        for i in range(offset_size):
            null

screen character_screen(id):

    default this_girl = ""
    default low_name_of_the_girl = ""
    for girl in all_girls:
        if girl.id == id:
            $ this_girl = girl

    if this_girl == "" and id > 0:
        $ this_girl = all_girls[0]
        $ id = this_girl.id
    if this_girl == "" and id <= 0:
        $ this_girl = all_girls[len(all_girls)-1]
        $ id = this_girl.id
    $ low_name_of_the_girl = str(this_girl.name.lower())

    modal True
    zorder 2
    frame:
        xsize 1920
        ysize 1080
        background  Frame(str("sky background.webp"), 1920, 1080)
        frame:
            xalign 0.95 yalign 0.5
            xsize 1290
            background Solid("#000000a5")
            ysize 1010
            if this_girl.revealed == True:
                text  "[this_girl.name]" xalign 0.5 yalign 0.01 size 120 style "character_screen_text" color "#FFF0F7"
                text  "{color=#D9C777}Race:{/color} [this_girl.race]" xalign 0.17 yalign 0.3 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Role:{/color} [this_girl.role]" xalign 0.17 yalign 0.4 size 45 xanchor 0.0 style "character_screen_text"
                if this_girl.book_phrase == "0":
                    text  "{color=#D9C777}Tip:{/color} No tips for now" xalign 0.17 yalign 0.5 size 45 xanchor 0.0 style "character_screen_text"
                elif this_girl.book_phrase == "1":
                    text  "{color=#D9C777}Tip:{/color} Progress story with other characters" xalign 0.17 yalign 0.5 size 45 xanchor 0.0 style "character_screen_text"
                elif this_girl.book_phrase == "2":
                    text  "{color=#D9C777}Tip:{/color} Thats all for this update" xalign 0.17 yalign 0.5 size 45 xanchor 0.0 style "character_screen_text"
                else :
                    text  "{color=#D9C777}Tip:{/color} [this_girl.book_phrase]" xalign 0.17 yalign 0.5 size 45 xanchor 0.0 style "character_screen_text"
                
                # text  "{color=#D9C777}Tip:{/color} [this_girl.book_phrase]" xalign 0.17 yalign 0.5 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Marital Status:{/color} [this_girl.marital_status]" xalign 0.17 yalign 0.6 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Relationship:{/color} [this_girl.relationship]" xalign 0.17 yalign 0.7 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Curiosity:{/color} [this_girl.curiosity]" xpos 0.17 ypos 740 size 45 xanchor 0.0 style "character_screen_text" xsize 950 
            else:
                text  "?????????" xalign 0.5 yalign 0.01 size 120 style "character_screen_text" color "#FFF0F7"
                text  "{color=#D9C777}Race:{/color} ????" xalign 0.17 yalign 0.3 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Role:{/color} ????" xalign 0.17 yalign 0.4 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Tip:{/color} ????" xalign 0.17 yalign 0.5 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Marital Status:{/color} ????" xalign 0.17 yalign 0.6 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Relationship:{/color} ????" xalign 0.17 yalign 0.7 size 45 xanchor 0.0 style "character_screen_text"
                text  "{color=#D9C777}Curiosity:{/color} ????" xalign 0.17 yalign 0.8 size 45 xanchor 0.0 style "character_screen_text" 

            textbutton ">":
                text_style "yellow_buttom_character"
                action [Hide("character_screen"), Show("character_screen", dissolve,id + 1)]
                xalign 0.97
                yalign 0.0
                text_size 70
                yoffset -28
            textbutton "<" :
                text_style "yellow_buttom_character"
                action [Hide("character_screen"), Show("character_screen", dissolve,id - 1)]
                xalign 0.92
                yalign 0.0
                text_size 70
                yoffset -28
            textbutton "X":
                text_style "yellow_buttom_character"
                action [Hide("character_screen")]
                xalign 1.0
                yalign 0.0
                yoffset -8
                text_size 45
    frame:
        xsize 1920
        ysize 1080
        if this_girl.revealed == True:
            background  Frame(str("character_screen/" + low_name_of_the_girl + ".webp"), 1920, 1080)
        else:
            background  Frame(str("character_screen/" + low_name_of_the_girl + " hidden.webp"), 1920, 1080)

        # background Solid("#000000")

init python:
    def book_refresh():
        if linda.phase == 1:
            linda.book_phrase = "2"
        return
