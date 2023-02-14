label close_inventory:
    hide screen inventory
    return

screen inventory():
    modal True
    default screen_item = {
    'Selected' : ''
    }
    default item_name = ""
    default item_quantity = ""
    default item_description = ""
    default item_type = ""

    default placeholder = ""
    default placeholder2 = ""
    default placeholder3 = ""
    default placeholder4 = ""
    zorder 2
    frame:
        xpadding 25
        ypadding 30
        xalign 1.0
        yalign 0.0
        xsize 1340
        ysize 1080
        background Solid("#6B89DB")

        if item_name != "":
            text "[item_name]" style "show_text" xalign 0.5 yalign 0.1 size 77 color "#000000"
            text "Quanatity: [item_quantity]" style "show_text" xalign 0.05 ypos 300 color "#242424" size 37 xanchor 0.0
            text "Type: [item_type]" style "show_text" xalign 0.05 ypos 370 color "#242424" size 37 xanchor 0.0
            text "[item_description]" style  "show_text" xalign 0.05 xanchor 0.0 yalign 0.45 color "#242424" size 37 xsize 900 yanchor 0.0


    frame:
        default var = -1
        xalign 0.0

        xsize 580
        ysize 1080
        add Solid("#D45359FF")
        viewport:
            vbox:
                for item in player_inventory.items:
                    $ placeholder = item.quantity
                    $ placeholder2 = item.get_item().name
                    $ placeholder3 = item.get_item().description
                    $ placeholder4 = item.get_item().type
                    textbutton "[item.quantity]     [placeholder2]":
                        text_style "inventory_button"
                        action [SetScreenVariable("var", item.id), SelectedIf(var == item.id), SetScreenVariable("item_name", placeholder2), SetScreenVariable("item_description", placeholder3), SetScreenVariable("item_quantity", placeholder), SetScreenVariable("item_type", placeholder4)]
            xfill True
            yoffset 80
            xpos 350
            xalign 0.5
            yalign 0.5
            mousewheel True
            draggable True
            arrowkeys True
            $ placeholder = len(player_inventory.items)



    frame:
        xpadding 0
        ypadding 0
        xalign 0.3
        yalign 0.0
        xsize 43
        ysize 1080
        add Solid("#E6E6E6")
    frame:
        xpadding 0
        ypadding 0
        xalign 1.0
        yalign 0.0
        xsize 43
        ysize 1080
        add Solid("#E6E6E6")
    frame:
        xpadding 0
        ypadding 0
        xalign 0.0
        yalign 0.0
        xsize 43
        ysize 1080
        add Solid("#E6E6E6")
    frame:
        xpadding 0
        ypadding 0
        xalign 0.0
        yalign 1.0
        xsize 1920
        ysize 34
        add Solid("#E6E6E6")
    frame:
        xpadding 0
        ypadding 0
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 70
        add Solid("#E6E6E6")
        # textbutton "X":
        #     text_style "x_button"
        #     action Call("close_inventory")
        #     xalign 1.0
        #     yalign 0.5


        text "Items" xalign 0.12 yalign 0.5 size 43 color "#000000"
        text "Description" xalign 0.65 yalign 0.5 size 43 color "#000000"
    frame:
        xpadding 0
        ypadding 0
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 70
        add Solid("#E6E6E6")
        textbutton "X":
            text_style "x_button"
            action Call("close_inventory")
            xalign 1.0
            yalign 0.5
        textbutton "X":
            text_style "x_button"
            action Call("close_inventory")
            xalign 0.005
            yalign 0.5
        text "Items" xalign 0.12 yalign 0.5 size 43 color "#000000"
        text "Description" xalign 0.65 yalign 0.5 size 43 color "#000000"
