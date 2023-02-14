label close_store:
    # hide screen grocery_store
    # jump reload_location
    return

screen grocery_store_screen():
    default placeholder = ""
    default player_item_match = ""
    default quantity_placeholder = 0
    default id_placeholder = 0
    default ygrid = 0
    default items_to_show = []
    # modal False
    # add background Solid("0000")
    frame:
        xpadding 50
        background Solid("#FAFFFBA3")
        xsize 1270
        ysize 50
        xalign 1.0
        yalign 0
        textbutton "X":
            text_style "x_button"
            action Call("close_store")
            xalign 1.04
            yalign 0.0
            yoffset -24
        grid 6 1:
            yalign 0.5
            spacing 63
            text"Quantity" style "title_text"
            text"Rarity" style "title_text"
            text"Name" style "title_text"
            text"Buy" style "title_text"
            text"Sell" style "title_text"
            text"Sell 10" style "title_text"
    frame:
        xpadding 50
        background Solid("#0D0D0DA0")
        xsize 1270
        ysize 1080
        xalign 1.0
        ypos 50
        vbox:
            $items_to_show.clear()
            for item in all_items:
                if item.type != "Potion" and item.is_active == True:
                    $ items_to_show.append(item)
                    $ ygrid = len(items_to_show)
            grid 6 ygrid:
                xspacing 5
                yspacing 3
                default list_of_store_items = []
                for item in items_to_show:
                    if item.type == "Potion":
                        pass
                    $ placeholder = player_inventory.item_exists(item.id)
                    $ player_item_match = placeholder
                    if placeholder == -1:
                        text "0" style "show_text"
                    else:
                        $ placeholder = player_inventory.items[placeholder].quantity
                        text "[placeholder]" style "show_text"

                    $ placeholder = str(rarity_list[item.rarity]).capitalize()
                    text "[placeholder]" style "show_text"

                    $ placeholder = item.name
                    text "[placeholder]" style "show_text"

                    if player.money >= item.buy_price:
                        $ placeholder = item.buy_price
                        textbutton "Buy [placeholder]$":
                            text_style "mytextbutton"
                            action  [Function(player.remove_money, item.buy_price), Function (player_inventory.add_item, item.id, 1)]
                    else:
                        $ placeholder = item.buy_price
                        text "Buy [placeholder]$" style "can_not"

                    $ placeholder = player_inventory.item_exists(item.id)
                    if placeholder != -1:
                        $ placeholder = player_inventory.items[placeholder].quantity

                    if placeholder > 0:
                        $ placeholder = item.sell_price
                        textbutton "Sell [placeholder]$":
                            text_style "mytextbutton"
                            # action  Call("speak_now", item.id)
                            action  [Function(player.add_money, item.sell_price), Function (player_inventory.remove_item, item.id, 1)]
                    else:
                        $ placeholder = item.sell_price
                        text "Sell [placeholder]$" style "can_not"


                    $ placeholder = player_inventory.item_exists(item.id)
                    if placeholder != -1:
                        $ placeholder = player_inventory.items[placeholder].quantity
                    if placeholder > 10:
                        textbutton "Sell 10":
                            text_style "mytextbutton"
                            action  [Function(player.add_money, item.sell_price * 10), Function (player_inventory.remove_item, item.id, 10)]

                    else:
                        text "Sell 10" style "can_not"


    frame:
        xpadding 50
        background Solid("#FAFFFBA3")
        xsize 1270
        ysize 50
        xalign 1.0
        ypos 1030

        hbox:
            xalign 0.5
            yalign 0.5
            text"Coins: " style "money"
            text"[player.money]" style "money"
