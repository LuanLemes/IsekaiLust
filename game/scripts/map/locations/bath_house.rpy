screen bath_house():

    frame:
        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image)) 


        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Milk Farm")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Milk Farm")
        text "Milk Farm" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

        if calendar.current_week_day != 6 and calendar.current_week_day != 0 and calendar.current_day_time < 2 and anna_bath_house_first == True:
            imagebutton auto "overlays/anna %s.webp":
                focus_mask True
                xpos -5
                ypos -5
                action Call("anna_bath_house")

    use top_screen()

label bath_house:
    if bath_house_first == True and calendar.current_day_time < 2:
        $ bath_house_first = False
        mc_thought "A big house?"
        menu:
            "Investigate":
                pass
        scene black with dissolve
        "..."
        scene bath house morning with dissolve
        mc "I dont really know whats going what is this big house, its locked."
        mc "Maybe I could take a look at it later."
        return
    if calendar.current_day_time == 2 and girls_bathed == False:
        mc "I can hear sounds inside, maybe I should take a look."
        menu:
            "Get closer":
                call bath_girls_night
            "Nah, Im ok":
                mc "Im not in the mood of such things"
                return
        return
    return

label bath_girls_night:
    $ bath_house_scene_1 = True
    show farm 159
    mol "Ohhh I love a good bath after a hot day."
    dai "Oooh me too."
    mc_thought "Wait, is that molly and the girls?"
    mc_thought "What are they doing?"
    menu:
        "Peek inside":
            pass
        "Just leave":
            return
    show farm 170
    mc_thought "I think I go the really lucky here."
    show farm 160
    dai "So Molly, the new boy, he milked you didnt he?"
    dai "How was it?"
    show farm 162
    mol "Oh I think it was his first time doing it."
    show farm 160
    dai "His first time?"
    dai "Dont tell me that you had to teach him."
    show farm 162
    mol "No, it was not like that at all, even tho it was his first time."
    mol "How can I say...it was like he really knew where to go and when to go..."
    mol "He even surprised me once."
    show farm 160
    dai "Surprised?"
    dai "Good surprise or bad surprise?"
    show farm 162
    mol "Oh definitely good surprises."
    show farm 161
    dai "Oh Molly, Miss May is right." 
    dai "You are really the easyest one."
    sug "Oh Mom, please stop, not my boobs"
    dai "I have to clean you whole Suggar."
    dai "Dont you want to be beautifull as your mommy?"
    sug "Yeeees Moooomy."
    dai "Good girl."
    show farm 162
    mol "But, You know, I liked the way he touched me, the way he took care of me."
    mol "He was in command, but it was as he was looking for me to have a good experience also."
    mol "Not only as if Im just a cow as others did."
    mol "And the way he grabbed me, Ohhhh."
    show farm 160
    dai "Seems like you liked it."
    dai "A lot in fact."
    show farm 162
    mol "I did."
    mol "In fact at some momments seemed like he knew my breasts better than myself."    
    show farm 160
    dai "Hmmm someone that knows how to command, but also respect cows."
    dai "\"Respect.\""
    dai "I really do like that."
    dai "Maybe you will you will get to like him Anna."
    show farm 163
    ann "I really doubt it, I saw him before, once, It was the day I tried to run away."
    ann "He was trying to pork a girl in the middle of the flower field."
    ann "If he doesnt respect a fully human, how will he respect us that are so many times seen as lower lifes."
    show farm 162
    mol "Oh my did he really do that?"
    mol "Thats interesting."
    show farm 168
    ann "Im telling you I wouldn´t be saying that if I didnt saw it with my own eyes."
    ann "That boy has secrets Im telling you."
    ann "And I wont be milked by someone that doesnt respect us cows."
    ann_shout "NEVER." with vpunch
    show farm 165
    dai "Hmmmm."
    dai "I would go with caution before making an acusation."
    show farm 168
    ann "Are you calling me a liar?"
    show farm 165
    dai "Not exacly."
    dai "Im not saying you didnt saw what you saw."
    dai "Im only stating that there can be more to it."
    dai "We dont know the exact context of it."
    dai "He could be helping her and something happened."
    dai "They could be lovers having a good momment."
    dai "Could be anything and we dont know that."
    dai "Everybody have secrets, even you and me."
    dai "But As far as I know he is a boy that is now responsable for milking the cows in this farm."
    dai "And if he treats my Suggar and the rest of us well, I wont have a reson not to trust him."
    dai "Tho....I dont fell very confortable to be milked by him yet."
    show farm 163
    ann "Speak for yourself then, I dont let that human touch my boobs."
    show farm 168
    ann "NEVER!" with vpunch
    hide farm
    call time_next
    $ anna.revealed = True
    return

label anna_bath_house:
    show anna idle
    mc_thought "Another cow?"
    mc_thought "This one has a great ass."
    mc_thought "Just how many are there?"
    menu:
        mc_thought "Maybe I should call her?"
        "Call her":
            mc "Hi there."
            show anna front bath with dissolve
            ann "What do you think you are doing?"
        "Stay quiet":
            mc_thought "Better say nothing for now."
            show anna front bath with dissolve
            ann "What are you doing?"
            mc_thought "Whats with these cows and theyr panoramic vision!"
    ann "Pervert human!"
    show anna idle with dissolve
    mc "What did you just say?"
    hide anna with dissolve
    mc_thought "And I that thought nobody could be worse than ashley."
    $ anna_bath_house_first = False
    $ anna.revealed = True
    return



    

    
    
    

    




        












        



    


    
            
        

    

    

    

    


    





















    
    return