screen home():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            focus_mask True
            xpos image_button_offset
            ypos image_button_offset
            hovered SetVariable("focus_location", " Enter House")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/house to living room hover.webp")
            idle ("overlays/house to living room.webp")
            action Call("change_location_to", "Living Room")

        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Village")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Forest Wall")
        text "Village" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

        #   monica and sarah talking scene at fridays
        if calendar.current_day_time == 2 and calendar.current_week_day == 5 and monica_sarah_invited == False:
            imagebutton auto "overlays/sarah monica house %s.webp":
                focus_mask True
                xpos image_button_offset
                ypos image_button_offset
                action Call("monica_sarah_talking_home")
        # lilith_outside_home_first:
        if int(debbie.phase) > 0 and flowers_monica_level > 1 and flowers_sarah_level > 1 and lilith.phase == 0 and calendar.current_day_time == 3:
            imagebutton auto "overlays/lilith home %s.webp":
                focus_mask True
                xpos image_button_offset
                ypos image_button_offset
                action Call("lilith_outside_home_first")
    use top_screen()

label home_check:
    if calendar.current_day_time == 0:
        $ can_enter = False
        $ not_enter_message = "Now its morning and you cant go home."
    elif calendar.current_day_time >= -1:
        $ can_enter = False
        $ not_enter_message = "You you cant go home now."
    return can_enter

label home:
    window hide
    return

label monica_sarah_talking_home:
    show monica_sarah home1 with dissolve
    menu:
        mc_thought "Wow, the two of them here like this."
        "Say \'Hey\'":
            pass
        "Let them chat":
            hide monica_sarah
            return
    mc "Hey."
    show monica_sarah home5
    mon "Hi [player.name]."
    sar "Oh, Hey [player.name]."
    if monica_sarah_talking_first == True:
        show monica_sarah home7 with dissolve
        sar "Now, thats something strange."
        sar "Hmmmm."
        show monica_sarah home15
        mon "Now, whats so strange?"
        sar "I knew you lived with Monica but, I kind of, forgot you lived here."
        show monica_sarah home9
        mon "Ha ha ha, oh Sarah thats so you."
        show monica_sarah home8 
        sar "Im sorry, the last two months were kind of harsh"
        mon "Yeah, It was indeed."
        show monica_sarah home5
        mon "Anyway [player.name]..."
        show monica_sarah home5
    menu:
        mon "How are you this evening?"
        "Im fine thanks.":
            show monica_sarah home11
            mon "Oh dear thats good to hear."
        "Im very good thanks.":
            show monica_sarah home11
            mon "Good thing dear."
    if flowers_sarah_level <= 1 or flowers_monica_level <= 1:
        mc_thought "I think its better to leave, girls sometimes need these moments alone."
        mc "So, I feel like Im in the middle of a \'girl thing\' here, so Im going to leave."
        mc "Good night girls."
        show monica_sarah home5
        mon "Good night [player.name]."
        sar "Good night."
        hide monica_sarah
        return
            
    sar "Anyway."
    show monica_sarah home14
    mon "..."
    mc "..."
    show monica_sarah home15
    sar "We were just talking about you."
    mc "You..."
    mc "You were?"
    show monica_sarah home16
    mon "Whaaat."
    mon "Dont say that Sarah."
    show monica_sarah home17
    sar "Oh mon mon its ok."
    mon_wisper "Sarahhh..."
    sar "What?"
    mon_wisper "..I...I didnt want him to..."
    sar "Its ok Mon."
    show monica_sarah home18
    sar "Everything will be all right."
    menu:
        mc_thought "..."
        "Leave them alone":
            mc_thought "For some reason Monica is not comfortable with this conversation."
            mc "Well girls."
            mc "I think I will let you two talk alone."
            mc "Thank you for the conversation."
            hide monica_sarah
            return
        "Invite them to go inside":
            mc "I think its starting to get darker, we better go inside."
            mc "Maybe, you should get inside?"
            mc "You know, just to be safer"
            show monica_sarah home20
            mon "Good idea [player.name]!"
            mon "We should get inside."
            mon "Im going in now."
            sar "Im going too."
            show monica_sarah home6
            mc_thought "Man, this place is too good for me."
            mc "You two can go ahead."
            $ monica_sarah_invited = True
            $ first_monica_sarah_invited = True
            mc "Im right behind you."
            hide monica_sarah
            return

            
        "What were you two talking about?":
            mc "Oh yeah? what were the two of you talking about?"
            sar "Oh we were just talking about how you have a bi..."
            show monica_sarah home20
            mon_shout "Nothing!" with vpunch
            mc "..."
            mon "Ahn, we were talking about nothing."
            mc_thought "DAMN, I really want to know..."
            mc "Ok, I think its a \'girls talk\'."
            mc "I will leave you two to it then."
            hide monica_sarah
            return
    return

label lilith_outside_home_first:
    $ lilith.phase = 1
    $ lilith.revealed = True
    show lilith home idle
    mc_thought "What? its not a cat?"
    mc_thought "Its....A GIRL?"
    mc_thought "A very cute girl in fact."
    mc_thought "However she is on my rofftop and she is very loud."
    mc_thought "I need to teach this girl a lesson."
    menu:
        mc_thought "A girl?"
        "Scream something":
            mc_shout "HEEEEEEY! You on the rooftop!!!"
            mc_thought "I think she can´t hear me from up there."
        "Go towards the girl":
            pass
    mc_thought "Im going over there."
    scene
    show house_roff_dawn
    show lilith roff1
    mc_thought "Wow, she is so pretty."
    mc_thought "Like she is like she is an angel or something."
    mc_thought "I think she went up there to look at the moon from a better place."
    mc_thought "Well, between looking at her and looking at the moon."
    mc_thought "I think I chosse look at her."
    mc_shout "Heeeeey, could you please get down?"
    mc_thought "Man, not a reaction? Is she ignoring me?"
    menu:
        "Scream again":
            mc_shout "HEEEEEEEEEEY!!!!"
    mc "Ok...just keep ignoring me."
    mc "I will stay here and look carefully at each part of your body."
    show lilith roff4
    mc_thought "Wait, did she hear that?"
    show lilith roff3
    mc_thought "She is looking."
    mc_thought "Not only hot but also cute!" with vpunch
    mc_thought "She is just too pretty!"
    mc_thought "Im not sure, but I think this is love at first sight."
    mc_thought "Man, this is so crazy, she just looked at me and my heart is already pounding like my life is in danger."
    mc_thought "It is love at first sight!"
    lunk "Hi."
    mc_thought "Even her voice is beutiful!!!"
    mc_thought "Come on [player.name] be good behave, the first impression is what matters."
    menu:
        mc_thought "I need to make a first good impression!"
        "Hi":
            mc "h.. h..m.. h.."
            mc "Me.."
        "Lovely night isnt it?":
            mc " The ah gr lovely it isnt night?"
        "Beautifull moon isnt it?":
            mc "I ... I moon big moon big moon..."
        "Life unfurls as a vibrant tapestry isn't that true?":
            mc "lif...fur han big it try isnt?..."
    lunk "?"
    mc_thought "And there it goes my first impression."
    menu:
        mc_thought "I need her to come down here."
        "Please come down":
            mc "Listen lady could you please get down here?"
            lunk "Okay."
            call lilith_teleport_animation
        "What are you doing up there?":
            lunk "I was..."
            call lilith_teleport_animation
            lunk "Watching the moon."
            mc "What are you doing up there?"
    mc_shout "Whaaaaaaat!?!?!?!??" with vpunch
    lunk "What?"
    mc "You you you.."
    mc "You just teleported!" with vpunch
    lunk "No I didnt."
    mc "Yes you did."
    lunk "Oh, that was no teleport, it was only a little speed."
    mc "That didn´t seem like a little."
    lunk "Oh, the thing is, I can be very fast sometimes."
    menu: 
        mc_thought "Man...I understand I should be thinking about other things in this situation but..."
        "Look at her boobs":
            window hide
            camera:
                subpixel True 
                pos (0, 0) zoom 1.0 
                linear 0.11 pos (-2400, -510) zoom 2.26 
            with Pause(0.11)
            camera:
                pos (-2400, -510) zoom 2.26 
            window show
            mc_thought "(Those booobs!!!!)"  with vpunch
        "Look at her body":
            window hide
            camera:
                subpixel True 
                pos (0, 0) zoom 1.0 
                linear 0.15 pos (-1900, -1063) zoom 2.02 
            with Pause(0.25)
            camera:
                pos (-1900, -1063) zoom 2.02 
            window show
            mc_thought "(She is hot!)" with vpunch
    lunk "...are you..."
    call camera_reset
    scene
    show llilith roff6
    lunk "Having fun there?"
    mc "Im sorry."
    lunk "..."
    show llilith roff7
    mc "Im sorry!" with vpunch
    lunk "Its ok.. you ca look if you want."
    mc "Really?"
    menu:
        "Look.":
            pass
    show llilith roff8
    mc "Thanks mam."
    menu:
        lunk "What do you like more?"
        "Your boobs":
            mc "Your boobs they are so beautiful!"
            lunk "Thanks, Im very proud of them."
        "Your body":
            mc "Your body is just awesome!"
            lunk "Oh thanks, its all natural you know."
        "Your face":
            mc "You face is so cute."
            lunk "Oh you are so pure"
            mc "Hehe."
        "Everything!":
            mc "I like everything im seeing."
            lunk "Oh you are just being polite."
            mc "Im not, you body is just too hot."
    mc "You really really are very beutiful."
    lunk "Is that why you are so happy down there?"
    show llilith roff9
    mc_thought "Down there?"
    mc_thought "hmmmm."
    mc "What do you mean?"
    show llilith roff10
    mc "Ohhh, Im sorry!!!"
    mc "I didnt realize I was..."
    lunk "Its ok [player.name]."
    mc "[player.name]? How do you know my?"
    lunk "You didnt get it yet? Im a succubus."
    mc_thought "She is a succubus?!?"
    show llilith roff11
    mc_thought "Succubus steal human vital energy through sex."
    mc_thought "This bad, If she start having sex with me im going to die."
    menu: 
        mc_thought "I need to get out of here!"
        "Run inside!":
            mc_thought "Thats it, im out of here."
            mc "Im out of here!"
    scene door dawn
    mc_thought "Almost there."
    
    window hide
    show lilith roff5:
        subpixel True 
        xpos 207 alpha 0.0 additive 3.21 blur 7.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.82)*SaturationMatrix(1.07)*BrightnessMatrix(0.08)*HueMatrix(0.0) 
        linear 0.30 xpos -7 alpha 2.42 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(0.40)
    show lilith roff5:
        xpos -7 alpha 2.42 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    window show

    show lilith roff5
    lunk "Hey."
    mc "Wait how?"
    lunk "Did you forget succubus are magical creatures?"
    lunk "Besides, you saw how fast I am."
    lunk "Now, Lean on the wall and let me do the rest."
    menu:
        mc_thought "Does she think Im going to obey her?"
        "Tell her you wont":
            mc "You are very wrong if you think I will obey you."
        "Kick her and get inside":
            mc "Lets see how fast you are when I do this!!!...."
    show lilith roff7 with dissolve
    lunk "Good boy."
    mc "What?"
    mc "How?"
    mc_thought "Its like my body moved on its own."
    lunk "You have your little tricks, I have mine."
    mc "No, please no! I dont wanna die!"
    lunk "Relax, most of man go with a smile on theyr faces."
    mc "Isn´t there a way for we to do this and me staying alive?"
    lunk "Im sorry [player.name], there is not."
    show lilith roff6 with dissolve
    lunk "Besides, Your body is very much begging for me right now."
    mc "No it isnt."
    lunk "Well, lets see if this is true or not."
    show lilith roff8 with dissolve
    lil_shout "OH MY!!!!!!!!!" with vpunch
    show lilith roff9 with dissolve
    lil_shout "This cock!!!"
    lil_shout "Is so beautiful!!!"
    lil_shout "I never imagined you would be hiding such a colossal thing like this."
    lil_shout "In a thousand years I never seen such a huge and beautifull cock like this."
    lil_shout "[player.name], your are truuully special."
    scene black
    show lilith roff10 with fade
    lunk "Anyway, lets start."
    mc "Ahh!"
    mc_thought "She is just so beautifull, and her hands are so warm."
    lunk "Such a big and young cock."
    mc_thought "Maybe if I try not to cum."
    mc_thought "I can resist her and get out of this alive."
    show lilith roff11 with dissolve
    lunk "I know what you are thinking bill."
    mc "..."
    lunk "You are thinking \"That if you try to resist you can get out of this alive\" right?"
    mc "How did you?"
    lunk "Im sorry, but there is no way out of this."
    lunk "The best thing you can do now its enjoy the momment."
    lunk "you know most man live theyr entire life without having the experience of be with a woman like me."
    lunk "So let your cock enjoy the best of it."
    lunk "Besides, even if you want you wont be able to resist anyway."
    menu:
        lunk "Besides, even if you want you wont be able to resist anyway."
        "I will resist":
            lunk "Oh, is that so?"
        "You are wrong":
            lunk "Oh am I?"
    show lilith roff10 with dissolve
    lunk "lets see what you dick has to say about that."
    mc_thought "Her hands are so smooth."
    mc_thought "And the way she looks at my cock also fells so good."
    lunk "Are you sure you will try resist Me?!"
    menu: 
        "Resist!":
            pass
        "Resist!":
            pass
        "Resist!":
            pass
    mc "I can admit it fells good, but I have a lot of self control."
    mc "And with my life on the line, Im telling you!"
    mc_shout "I wont cum!"
    lunk "Is that so?"
    show lilith cock cum1
    lunk "Then what is that on the tip of your cock?"
    mc_thought "Shit!" with vpunch
    show lilith cock cum2
    lunk "Hum?"
    mc "..."
    lunk "You know what it is dont you?"
    mc "I can still resist!"
    mc_thought "I can´t die here. I need to resist!"
    mc "This doesnt mean anything!"
    lunk "You really think you are special dont you?"
    lunk "Well time will tell."
    lunk "And we have a lot of time."
    show lilith roff12 with dissolve
    lunk "And a lot of space too."
    mc "Ahhh!"
    lunk "Confess [player.name]."
    mc_thought "Aw maaan, this girl is...a whole other level!"
    lunk "You like it, dont you?"
    lunk "You couldn´t stop me even if you wanted to."
    lunk "I can see in your eyes, you looking at me as if you wanted to eat me."
    mc "Thats not true!"
    show lilith roff13 with dissolve
    lunk "Your cock says otherwise doesnt it?"
    lunk "Look, how it is now, Its dripping cum."
    lunk "Im only using my right hand here."
    show lilith roff14 with dissolve
    lunk "And still... its very very good, dont you agree?"
    mc "Ahh, It....it isnt!"
    mc_thought "I must keep resisting her! I must get out of this alive!"
    lunk "Listen [player.name]."
    lunk "You can say it all you want."
    show lilith roff15 with dissolve
    lunk "But how can you not find this beautifull?"
    lunk "I mean, come on, this is a true work of art."
    lunk "This huge cock of yours."
    lunk "Plus the way your cum is going out of it."
    lunk "I can fell your cum smell from here, is so good."
    lunk "It looks so yuumi."
    show lilith cock cum3 with dissolve
    lunk "I wonder how it tastes."
    mc "What are you doing?"
    lunk "Well, isnt that obvious?"
    lunk "Your Im going to check if the taste of your cum is as good as it looks."
    show lilith cock cum5 with dissolve
    lunk "Look at that, so beautiful."
    mc "Are you really going to..."
    show lilith cock cum6 with dissolve
    lunk "Prove it?"
    lunk "Yes I am."
    lunk "I know you want me to."
    show lilith cock cum7 with dissolve
    lunk "Hmmmmm."
    mc_thought "I know this succubus will drain all my life force to death."
    mc_thought "But look at her putting my cum in her mouth its very rewarding."
    mc_thought "She swallowed it all."
    show lilith cock cum8 with dissolve
    mc_thought "She is just perfect!"
    lunk "Hmmmmm."
    mc_thought "I think Im starting to like her."
    show lilith cock cum9 with dissolve
    lunk "Delicious!"
    $ lil.name = "Lilith"
    lil "My name is Lilith by the way."
    mc_thought "Ah! she is getting to me, I know it."
    mc "..."
    mc "Hi Lilith..."
    mc_thought "Wait, I can´t be friends with her, I need to be though here."
    show lilith cock cum10 with dissolve
    lil "Dont look at me like that."
    lil "I know you liked it."
    lil "But..."
    mc "But?"
    show lilith cock cum11 with dissolve
    lil "I want more!"
    menu: 
        "Maybe we could stop (live)":
            mc "Listen lilith we could stop it by now"
            mc "You had your share of cum, and I could keep on living."
            lil "Im sorry, thats not how a succubus do things."
            lil "We absorb life though sex and cum, and we wont stop until there is nothing left."
        "I want more too (give up living for pleasure)":
            mc "I want more too."
            mc_thought "What am I saying?"
            lil "I see, so you finally admit that you are liking it ."
            mc "A little, yes."
    show lilith roff12 with dissolve
    mc_thought "She is starting again!"
    lil "Yes, lets do this again until your I drain every drop of cum left in you!"
    mc_thought "This feeling is even better than before."
    show lilith roff10 with dissolve
    mc_thought "I usually dont fell that much pleasure."
    mc_thought "How is this possible? it is just different with her."
    menu:
        "How can you be so good at this?":
            lil "Thats just the way I am."
        "Ah, you are good at this!":
            lil "Thanks [player.name], your cock is very unique too."
    show lilith roff15 with dissolve
    lil "Wow, that again?"
    mc "Im sorry, your hand just fell too good."
    lil "Dont worry, I like it that way."
    lil "I mean...I find cum is facinating."
    show lilith roff13 with dissolve
    lil "By your breathing I would say you are about to cum right?."
    mc_thought "I dont want to cum, I dont want to die!"
    mc_thought "But at the same time I want to cum!!!"
    lil "Its ok you can cum on my face."
    menu:
        mc_thought "I need to resist!, I need to live!"
        "Resist!":
            pass
    show lilith roff14 with dissolve
    lil "Oh [player.name] thats very cute of you."
    lil "But you wont be able to hold up much longer."
    lil "Trust me I know what Im saying."
    lil "My handjob is very slow."
    lil "But your cock is feeling so good right now."
    lil "Little by little the momment where you cum is coming."
    mc_thought "I hate to say that."
    mc_thought "I dont think I can hold up´any longer."
    lil "Aint I right?"
    menu:
        mc_thought "Thats it, this is the end."
        "Im going to cum!!!":
            mc "Ahhhhh Im cumming!" with vpunch
        "Yes you are right!":
            mc "Yes you are right!"
            mc "Im cumming!!!" with vpunch
    show lilith roff16 with dissolve
    mc "Ahhhh!" with vpunch
    lil "Good boy, good boy."
    lil "Yes, thats it."
    lil "Let it all out!"
    lil "What a powerful cum, so much energy."
    mc_thought "Thats it, I die here."
    mc_thought "Good bye Monica, Linda, Ashley, Sarah, Debbie, Makoto, It was good to know you all."
    scene black with Dissolve (1.5)
    mc_thought "Good bye."
    lil "Its all over my face."
    show lilith cock cum13 with dissolve
    mc_thought "What?"
    mc "Am I still alive?"
    lil "Of course you are."
    mc "But I thought."
    lil "[player.name] you are going to die, but not after only one time."
    lil "The night its only begining."
    show lilith cock cum14 with dissolve
    lil "Ohhh Noooo!"
    lil "Thats not fair!"
    show lilith cock cum15 with dissolve
    lil "Damn your dick is beautifull even when its not hard."
    lil "You really have a huge dick [player.name]."
    lil "I think girls have a hard time with you." 
    lil "Such a colossal member."
    show lilith cock cum16 with dissolve

    mc "Soh, Hey Lilith."
    mc "We can see here that I cant do anything so..."
    mc "Maybe we should try it another day or..."
    
    show lilith cock cum17 with dissolve
    lil "Such a pity you have to die..."
    lil "I think, I love your cock."
    mc "Thats exacly my point! maybe I dont!"
    show lilith cock cum16 with dissolve
    lil "..."
    lil "[player.name]."
    show lilith cock cum18 with dissolve
    mc "What?"
    lil "I like you."
    mc_thought "Maybe I can get rid of this!"
    mc "I like you too!"
    lil "But mark my words..."
    show lilith cock cum19 with dissolve
    lil "I will drain your balls up!"
    mc "What is this?!"
    lil "A little succubus magic I learned a little magic with time."
    lil "Now watch this!"
    show lilith cock cum20 with dissolve
    mc "Whaaat?"
    lil "I think you are all better now."
    lil "Also.."
    show lilith cock cum21 with dissolve
    lil "I think I will take these off too."
    mc "You can take your clothes off with magic?"
    show lilith cock cum22 with dissolve
    lil "Oh [player.name]"
    lil "There are so many things a succubus can do."
    lil "Things you have no idea."
    show lilith cock cum23 with dissolve
    lil "Anyway, I think you are ready for more."
    mc "Just how powerfull are you?"
    lil "Powerfull enough."
    mc "Im starting to think you are not just any succubus."
    show lilith roff17 with dissolve
    lil "Enough talk and more action."
    lil "This time, I want you to look at my boobs while we do it."
    mc "Really?"
    lil "Yes, thats the part of my body that I like the most."
    lil "I fell happy when people look at them."
    lil "Also, I´d like you to cum on my boobs before you..."
    mc "...."
    lil "Well, do it as much as you can."
    show lilith roff18 with dissolve
    mc_thought "She really has beuatifull boobs."
    lil "Yes, Thats how I like it."
    lil "You are starting to learn."
    lil "Such a good boy."
    lil "Tell me [player.name]."
    mc "What?"
    lil "Do you want me to stop?"
    menu:
        lil "Do you want me to stop?"
        "No":
            lil "Such a good boy."
            lil "Seems Like I will have to reward you."
        "Yes":
            lil "Such a bad boy."
            lil "Seems Like I will have to punish you."
    show lilith cock cum27
    lil "I find so beautifull this cum dripping from the tip."
    mc_thought "How can someone be so pretty and so mean?"
    show lilith cock cum28
    lil "Oh."
    lil "It felt on my boob!"
    lil "Haha."
    show lilith roff19 with dissolve
    mc_thought "All I want is to take her and fuck her very rough style right now!"
    mc_thought "But her dam magic wont let me move so..."
    mc "Well, If I can´t win this, I might as well enjoy it."
    lil "Thats what im talking about!"
    lil "Will you be a good boy and cum a lot for me?"
    mc "Yes I will."
    lil "Very good!"
    mc "Lilith."
    lil "What is it [player.name]"
    mc "If I survived this, I would get my revenge on you."
    lil "Its ok, no one ever survives."
    mc_thought "Her body is too hot!"
    mc "I want to cover your in cum!"
    show lilith cock cum29 with dissolve
    lil "Go ahead."
    lil "On my boobs!"
    show lilith cock cum30 with dissolve
    lil "Cum on my boobs please."
    mc "Are you sure?"
    lil "Yes."
    mc "Im abou to cum!!"
    lil "Do it do it on my boobs!"
    show lilith roff20 with dissolve
    mc "Haa!"
    lil "Yes!!!"
    lil "Do it the cover me in your cum!"
    lil "Do it with that huge dick of yours."
    show lilith cock cum32 with dissolve
    lil "My boobs!"
    mc "They are...Ah..I can´t....talk. right now."
    lil "My boobs look beautifull covered in your cum."
    lil "Look at this!"
    menu:
        "They really look better this way.":
            pass
        "They really are beautifull":
            pass
    lil "Thanks [player.name]."
    show lilith cock cum33 with dissolve
    mc "(heavily breathing)"
    mc "Ah...Im too tired."
    mc "I dont think I can..."
    mc "(heavily breathing)"
    mc "I dont think I can take another one."
    lil_shout "UP!"
    show lilith cock cum35 with dissolve
    mc "Whaaaaat?"
    lil "Good boy!"
    lil "Weeew even your dick is full of cum now."
    mc "No Lilith, I dont think I can (heavily breathing)"
    show lilith roff21 with dissolve
    lil "Just watch while I play with your cock then."
    lil "We are still going to do that many many before you go dry."
    scene black with Dissolve(2.0)
    lil "A lot! of times."
    scene black
    call wake_naked_1
    return

label lilith_teleport_animation:
    scene house_roff_dawn
    show house_roff_dawn
    window hide
    show lilith roff3:
        subpixel True 
        parallel:
            pos (0, 0) 
            linear 0.19 pos (18, 8) 
        parallel:
            alpha 1.0 
            linear 0.19 alpha 0.35 
            linear 0.06 alpha 0.0 
        parallel:
            additive 0.0 blur 0.0 
            linear 0.31 additive 2.73 blur 6.2 

    window hide
    show llilith roff5:
        subpixel True 
        xpos 50 alpha 0.0 additive 4.29 blur 7.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.39)*HueMatrix(0.0) 
        linear 0.31 xpos 0 alpha 1.04 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(0.41)
    show llilith roff5:
        xpos 0 alpha 1.04 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    window show
    return

    window show
    show llilith roff5

return
    
