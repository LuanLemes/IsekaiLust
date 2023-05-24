screen milk_farm():

    frame:
        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image)) 
    if calendar.current_week_day != 6 and calendar.current_week_day != 0 and calendar.current_day_time < 2:
        imagebutton auto "overlays/ayummi farm %s.webp":
            focus_mask True
            xpos -5
            ypos -5
            action Call("mayummi_front_farm")
# molly first
    if calendar.current_week_day != 6 and calendar.current_week_day != 0 and calendar.current_day_time < 2 and cow_milked == False:
        imagebutton auto "overlays/molly overlay %s.webp":
            focus_mask True
            xpos -5
            ypos -5
            action Call("molly_farm_well")
# molly standard
    if molly_first == False:
        imagebutton auto "overlays/farm arrow green %s.webp":
            focus_mask True
            xpos -5
            ypos -5
            action Call("change_location_to", "Bath House")
    if Place18.can_map == True:
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

    use top_screen()

label milk_farm_on_enter:
    if milk_farm_first == True:
        $ milk_farm_first = False
        call milk_farm_first
        return
    return

label milk_farm:
    pass
    return

label mayummi_front_farm:
    if molly_first == True:
        show farm 3
        may "Have you found molly yet?"
        mc "No I didnt."
        hide farm 3
        return
    call mayumi_menu
    hide farm
    return
label mayumi_menu:
    show farm 3
    menu:
        may "What is it kid?"
        "Why people drink milk from cowgirls and not from cows?":
            may "For fuck sake."
            mc_thought "I think in this world this is a dumb question."
            may "When a baby is born do you feed him with cow food?"
            mc "No."
            may "Then why the hell would you feed someone with cow milk?"
            mc "That...kind of makes sense."
            may "Cow milk is not made for humans."
            may "The full human mons only produce milk for so long."
            may "But the cows produce milk theyr entire life."
            mc "So all cow girls in the world work as milk girls?"
            may "Do all man work as sperm donors?"
            mc "Ok I see you got a point."
            may "They are the same as you and me, only they produce milk, they can be whatever they want to be ok?"
            may "But become milk girls are the easy way for most of them."
            may "Most of them have an easygoing personality as a cow or whatever."
            may "The fact is, a cowgirl usually like to be milked."
        "So...was the milk man before me?":
            may "hufff..."
            may "The milk man before you was my brother."
            may "He couldnt do a good job like you but...he was all we had."
            mc "Is that so? why did he leave?"
            may "He didn´t leave."
            mc "So why isnt he milking the cows anymore?"
            may "Shut up and listen ok?"
            mc_thought "Seriously how can the cow girls like her?"
            may "He didnt leave, he died."
            mc "He died!?!??"
            may "I dont know if you have heard of it but there is a powerfull succubus around."
            mc "Oh I hav..."
            may "Besides a fake suicide note, we believe he died having relations with her."
            may "He was all drained out, there was no life on him anymore."
            mc "I see, Im sorry for asking."
            may "Dont be, what happened, happened."
        "About you...":
            may "About me what?"
            mc "What do you do in the farm?"
            may "Pretty much everything besides milking the girls."
            mc "Well, that was a thing back there, you told me you couldn´t milk the girls."
            may "Yes I did."
            mc "Why couldn´t you?"
            mc "I mean, it seems like you know pretty much everything here."
            may "*Takes a deep breath*"
            mc "..."
            may "Milk cow girls, isnt something a woman can do..."
            mc "Why?"
            may "It seems they \'react\' better when a man is doing the work."
            mc "Hmmm."
            may "You probably get what Im saying when you milk them for some time."
        "The other cows..":
            may "Every cow has its own personality." 
            may "I recomended you start with Molly because she is the easy one."
            may "But you will have to find your way with each other girl."
            mc "Find my way?"
            may "Yes, they are human after all not only animals that you order around."
            mc "But Molly told me when I milk them Im in comand."
            may "Thats true."
            mc "Since Im in command can´t I like, just order them around like animals?"
            may "I just said you can´t do that."
            may "When you dance with a girl you are in command."
            may "But before that you have to convince them to dance with you."
            mc "Oh that was very good, I think I understand now."
            may "Oh you do now dont you?"
        "Leave":
            mc "Well, I think thats about it, thank you for the talk."
            may "Anytime kid."
            return
    call mayumi_menu
    return

label milk_farm_first:
    show farm 9
    mc_thought "This should be the girl that is reponsable for the farm."
    mc_thought "But the way she dresses, damn!" with vpunch
    may "Who are you? what are you doing here?."    
    menu:
        "Hello, my name is [player.name], Im here to talk about the milk.":
            pass
        "Im called [player.name], Im here because Sarah told me about the milk problem.":
            pass
    may "Oh, so you are the milk boy?"
    mc "Ah, yes...I ...think I am?"
    show farm 10
    may "I see..."
    may "No bad..."
    may "Not bad at all..."
    show farm 9
    may "I think you will..."
    may "Do very well indeed."
    mc "Im sorry, are we in the same page here?"
    mc "Im not sure if expressed myself right but what Im aiming here is to solve the milk problem."
    show farm 10
    may "Yes, thats exacly what we are needing right now."
    may "Or...what I am needing right now."
    mc "..."
    may "Anyay, have you ever proved our milk?"
    mc "No I dont think I have."
    mc_thought "In fact I think I didnt have any milk since I got in this world."
    may "In that case."
    show farm 4
    may "Let me show you something."
    mc "Oh, so there is still milk?"
    may "Shut up."
    mc "Okay."
    mc_thought "Bitch what did you just say?"
    show farm 2
    may "I will fetch it some milk."
    mc_thought "Oh, her panties are so beautifull from behind."
    may "Just a little more and..."
    show farm 5
    may "Here, have drink it up."
    mc "the milk?"
    may "No, the saliva from my mouth big head."
    mc "What did you just..."
    show farm 6
    may_shout "DRINK!" with vpunch
    mc_thought "Ok, since you asked nicely."
    mc "Okay then..."
    menu:
        "Drink":
            pass
    show farm 9
    mc "Omg!"
    may "I know right?"
    mc_shout "This is the BEST milk I ever had in my entire life!"
    mc_thought "For real, this is just too good."
    may "Thanks, everybody says that but its always good to hear that again."
    mc "It was the best drink of my life."
    may "I heard the first time."
    show farm 10
    mc "I also know exacly what I would like to drink right now."
    mc "Milk?"
    may "Hmmm Yeah but....not the same milk as you have."
    may "Besides that was the last cow milk we had anyway."
    mc_shout "THAT WAS THE LAST MILK?"
    may "Relax big boy, relax and follow-me."
    show farm 11
    may "There they are, the right one is Daisy and the left one is...what was her name again?"
    may "Honey? no....wasnt that...sweetener?...Not that too.."
    may "Whatever...we she doesnt give milk anyway."
    may_shout "Daisy!!!"
    show farm 16
    dai "Ohhhh Hiiii Mayumi you are so beautifull today."
    dai "How are you doing?"
    show farm 13
    may "Im fine, and you?"
    show farm 16
    dai "Im fine tooooo."
    show farm 13
    may "What are you doing?"
    show farm 16
    dai "I was talking with Sugar, You know...so she could understand how life works."
    show farm 17
    mc_thought "Oh, so her name is Sugar, she is kind of cute."
    mc_thought "No...she is just too cute, Ohhh I want to hug her."
    show farm 18
    mc_thought "Shit, I think she saw me looking at her."
    mc_thought "So cute and so shy."
    show farm 13
    may "Im fine, Listen do you know where molly is?"
    dai "Molly? No I dont think so."
    show farm 14
    may "Great..."
    may "Dont tell me she left too."
    dai "What, Molly? You know she love this farm and everyone in here, she would never leave."
    show farm 16
    dai "Wait, I think I saw her...."
    show farm 14
    may "Where?"
    show farm 16
    dai "I think she is She is near the well."
    show farm 14
    may "Great, Thanks Daisy"
    show farm 16
    dai "Not for this."
    show farm 3
    may "Kid, go look for molly she is {color=#FFAA00}near the well,{/color} or at least, she should be."
    mc "Ok then."
    mc_thought "She is so bossy, but also she is so hot."
    $ sugar.revealed = True
    $ daisy.revealed = True
    $ mayumi.revealed = True
    return

label molly_farm_well:
    if molly.revealed == True:
        call molly_farm_well_daily
        return
    $ molly.revealed = True
    show farm 22
    mc_thought "That must be molly."
    mol "Wooooow thats so deep, I cant even see the bottom of it."
    mc_thought "She has a beautifull voice"
    mc_thought "Why are all the girls dressed with so few clothes? not that im complaining."
    mc_thought "Also this cow theme between all of them is also strange."
    mc_thought "I think it must be something like a farm uniform."
    show farm 23
    mc_thought "I think I should try to understand the reason of everything."
    mc_thought "And maybe enjoy the beautifull ass that is in front of me."
    show farm 24
    mol "Hello!"
    mc_thought "What the fuck? all of sudden? Im sure I was on her blind spot!"
    mol "..."
    mc "Hello!"
    mol "Han, im sorry, who are you?"
    mc "You scared me for a momment."
    mol "Im sorry, cows have a bit of a panoramic vision."
    mc "Oh, I see."
    mc_thought "How is this relevant?"
    mc "Anyway..."
    mc "My name is [player.name] and Mayumi asked me to call you."
    mol "Oh May May is calling me?"
    mc "I dont understand how someone as strict as she is can be called by such a cute nickname."
    mc "But if your name is Molly, yes, thats the one she asked me to call."
    show farm 31
    mol "Dont be like that, she is a lovely person, she is a good farmgirl."
    mol "You only need to know her better thats all."
    mol "So where is she?"
    mc "She is in front of the house in front of the farm."
    mol "So she is on her house? Lets go then."
    show farm 34
    mol "Hey May May [player.name] told me you were calling me."
    may "Yes I was."
    mol "So, how may I help you?"
    show farm 35
    may "So, As you know Im taking care of the farm now."
    show farm 34
    mol "Yes, and we are very thankfull for that."
    may "As you also know we have been looking for someone to milk the cows."
    mol "Oh yes, that there is quite some time since and all the cows are so full of milk"
    show farm 36
    may "Well, since I can not do this myself"
    show farm 38
    may "He is going to take care of milking all the cows."
    mc "What?"
    show farm 42
    mol "Oh my He? Thats such good news"
    mc_thought "Ok This milk quest is going out of bounds here. Maybe I should just agreed to clean ashley´s bedroom."
    may "And since all the cows have different personalities I think he may start with you that is probably the easyest one."
    mc_thought "Ok, its ok, all for getting to the map on ashleys room. No problem I can do this."
    mol "I think he is will be a ver...."
    may "Just go take the bucket for him already."
    mol "Yes mam."
    show farm 46
    mol "Here mr [player.name]."
    menu:
        "Alright":
            mol "Allright lets go"
        "Isnt that bucket too big?":
            may "Thats the standard size, now go you two."
            mol "Yes mam."
    mol "Im ready mr [player.name]."
    show farm 59
    mc_shout "WHAT?!" with vpunch
    may "Well, you are here to milk the cows arent you?"
    mc "So, they are not only dressed like cows?"
    mc_shout "They are the cows?"
    may "Not shit sherlock, everybody knows that since they are kids."
    may "I mean, why would someone prove milks from pure cows? cows produce milk for cows."
    may "Cowgirls produce milk for humans."
    mc "So the milk I tasted earlier were?"
    may "The last drop of our girls milk yes."
    mc_thought "This is kind of crazy."
    may "Anyway, Im going to leave you two alone."
    show farm 61
    mc "Wait!"
    may "Fill that bucket, good luck [player.name]."
    show farm 60
    mc  "I..."
    mc_thought "Seriously how did I get here again?"
    show farm 48
    mol "Im ready whenever you are [player.name]."
    mc_thought "Bad news is...I have no idea about how to procced here."
    mc_thought "Good new is...she is hot."
    menu:
        "Stare at her":
            mol "You can get near if you want, I dont bite."
        "knell at her side":
            pass
    mc "Ok then..."
    show farm 64
    mc "Han...Hello."
    mol "You get more cute the near you get."
    menu:
        "I was going to say the same.":
            mol "Ow stop, I will get all red."
        "And you hotter.":
            mol "Oooown, dont be like that."
    mc "So...I have to milk you right?"
    mol "Yes, but you can do it in your own way. I wont judge you."
    show farm 67
    mc_thought "Man, her body is just so beautiful from this distance."
    mc "I can even fell her smell from here."
    show farm 73
    mc_thought "Man, I like this view."
    mc_thought "Thinking about it this situation is not bad at all."
    mol "You are doing very well."
    mc "Its so clear im that nervous?"
    mol "Kind of, but you are really going well, just be yourself."
    show farm 76
    mc "So....Can I....like..."
    mc "Touch you?"
    mol "Yes silly, thats how it works."
    mc "Ok then...Then I think I wil..."
    menu:
        "Touch her breast.":
            pass
    show farm 77
    mol "See? nothing bad happened..."
    mol "You are doing very well."
    mc "Its so big."
    mol "Yes, Im a cow, most cows have big boobs."
    mc_thought "Man that feels so good."
    mc "I think I will need to use the other hand too."
    show farm 78
    mol "Its ok, You are on command here."
    mc "Im on command?"
    mol "Yes, thats how it works."
    mc "Interesting."
    mc_thought "Im starting to like this whole Idea of milking a cowgirl."
    mc "Than can I do the way I want?"
    mol "Yes, you are creating your procedure here."
    mc "Than If I want to like...."
    menu:
        mc_thought "I think she will leave as soon as I do this but...I have to try."
        "Lif her bra":
            pass
    show farm 80
    mc "Lift you bra...its ok?"
    mc_thought "This is where she gets out very mad and leaves."
    mol "Yes it is."
    mc_thought "This can´t be true, am I in heaven?"
    mc_thought "I can...touch her at will here..."
    mc_thought "I mean, Im just milking her."
    mc "I understand"
    menu:
        "Toutch her breast":
            pass
    show farm 79
    mc "I wont lie, your breast feels good."
    mol "Thanks [player.name]. I really like them too."
    mc "So Big."
    mc "And so cute."
    mol "Oh you are so kind."
    mc "Now, whats the next step?"
    menu:
        mc "Maybe I should like.."
        "Grab her breast":
            pass
    show farm 83
    mc "In this position I can fell your breast differently."
    mc "This feels good."
    mol "You are getting to know each other hun?"
    mc "Yes we are."
    mc "But the thing is, its so nice to fell them."
    mol "Heheheh, You are so funny, I think I like you [player.name]."
    mc "It goes for both of us."
    mol "*laughs*"
    mc_thought "Man this is just too good."
    mc "I want to really fell them."
    menu:
        mc "Like this."
        "grab her boob a little harder":
            pass
    show farm 85
    mol "Huh."
    mc_thought "Her reaction..."
    menu:
        "Are you ok?":
            pass
        "Everything alright?":
            pass
    mol "Ah..Yes yes it is, thats only..."
    mol "I felt you changing the pace thats all."
    mc "Hmm."
    mc_thought "Its so nice to fell like...her small reactions to what I do."
    mc_thought "I really fell in control of everything here."
    mol "But Im ok."
    mc "Are you really?"
    mol "Yes I am."
    menu:
        mc "In this case its time to..."
        "Grab the tip":
            pass
    show farm 86
    mol "*breath changing*"
    mc_thought "She is turning red..."
    mc_thought "Its like even she is so confident, My actions are getting to her."
    mc_thought "This is really fun."
    menu:
        "Its it ok to hold the tip like this?":
            pass
    mol "Yeees..."
    mol "*breathing*"
    mc_thought "The way she is looking at my hand its so awesome."
    menu:
        "I think I need to feel it a little more...":
            pass
    show farm 88    
    mc_thought "Man...her nipples are bigger right now, I think she likes it."
    mc "Like this..."
    mc "Thats a nice feeling."
    mol "Is it?"
    mc "Yes it is."
    menu:
        "Do you like when I hold the tip of your nipples like this?":
            pass
    show farm 89
    mol "Yes I dooo."
    mc "Good to know"
    mc_thought "This is just too much fun."
    mc_thought "I wonder how the other cowsgirls will be like."
    mc_thought "I can fell her breast will be like."
    menu:
        "But right now I want to get a better fell of this one.":
            pass
    show farm 90
    mol "Ahh."
    mc "Oh I can fell them way better like this."
    mol "Yes, so good."
    mc "It is indeed, But I cant forget Im milking you here."
    mol "Thats true mr [player.name]."
    mc "How do I do this exacly?"
    mol "..."
    mc "I think I should grab your entire boob, feels like the right way to do."
    mol "*breathing*"
    mc_thought "She stopped talking a little, what is she thinking?"
    menu:
        "Grab her boob a little stronger than before.":
            pass
    show farm 95
    mc_thought "Oh, I see a little drop right there."
    mol "Yeah? Thats good to hear. *heavily breathing*"
    mc "You seem to be a little tired."
    mol "Im ok, Im ok, its just there´s been quite some time since the last time."
    mol "And also, its my first time with you."
    mc "You are so cute."
    mc "Your face is red."
    mol "Oh, is it?"
    mc "Yes it is."
    mol "I can´t imagine why."
    mc "Well, if I see milk thats because its working right?"
    mol "Right!"
    mc "I think I need to grab them harder"
    mol_shout "Harder?!"
    menu:
        mc "Yes"
        "Grab her boobs harder(Milk!)":
            pass
    mc "Harder like this!"
    show farm 96
    mol_shout "Haaaaaaaa!!!!!"
    mc "Its working Molly!"
    mc "Its working!"
    mol "Ahhhhhhhh!"
    show farm 97
    mol "Ahhh, is it going to the bucket?"
    mc "Yes."
    mc "The bucket is filling up."
    mc_thought "She seems so tired."
    mc_thought "Well, I cant stop now."
    menu:
        mc_thought "I have to go on until the bucket is full."
        "Press her boobs harder and caress her back.":
            pass
    show farm 98
    mol "Ah *heavily breathing*"
    mc_thought "She isnt even reacting anymore."
    mc_thought "She is just, letting me do whatever I want"
    mc_thought "She isnt making eye contact anymore too."
    mc_thought "I need to support her."
    menu:
        "You are doing very well!":
            pass
        "You are doing great!":
            pass
        "Your breasts are awesome!":
            pass
    mol_shout "Tha-.....Thanks!"
    mc_thought "Well, since she seems to let me do whatever I want..."
    mc_thought "Im going to make a test just in case."    
    mc_thought "Slowly move my hand toward her ass.."
    mc_thought "If she reacts in a bad way I will stop."
    menu:
        "Move your left hand towards her ass":
            pass
    show farm 100
    mc_thought "I think she realized it."
    mc_thought "I need her to keep focused on her breast."
    menu: 
        "grab her boob again and again (harder)":
            pass
    show farm 101
    mc_thought "Now she seems relaxed."
    mc_thought "Even her eyes seems to be lost in some way."
    mc "You are doing great."
    mol "Haaaaa."
    mol "Than *breath* ks."
    mc_thought "I think thats the right momment to make my move."
    menu:
        "Fell her ass with your left hand.":
            pass
    show farm 103
    mc "This is just too good."
    mc_thought "Shit, I talked it out loud."
    mol "I agree. *breath*"
    mc_thought "I dont know about what she agreed, but she agreed."
    show farm 106
    mc "Now Moly lets focus on filling this bucket up ok?"
    mol "Ok Mr [player.name] Haaaaaaa."
    mc "At this rate we will end up taking a whole lot of time."
    mol "Y--yes."
    mc "Lets do it in a more intense way ok?"
    mol "Ahhhk."
    menu: 
        "Use both hands to take the milk out.":
            pass
    show farm 108
    mol_shout "Haaaaaaaaa!!!!!!!!!" with vpunch
    mol_shout "So stroooong!" with vpunch
    mc "Im sorry but its just necessary."
    mc "Mayumi told me to fill this buket and that what we are going to do!"
    mol_shout "You are so ...ah."
    show farm 110
    mc_thought "I think the bucket is full, also...she doesnt seem to have any milk left in her."
    mc "We did it Molly, we did it."
    mc "Molly?"
    mol ".........."
    mc "Molly?"
    mol "...."
    mc "Wait..."
    show farm 113
    mc "She slept?"
    mc "So getting milked drains her out."
    mc "Its understandable."
    show farm 114
    mc "Man..such a beautifull view."
    mc "I would love to fuck her right now but Mayumi can get here at any momment."
    mc "I will tell Mayimi about the milk I managed to get."
    show farm 3 with dissolve
    may "So you did it hun?"
    may "I knew you had it in you."
    may "Good job kid."
    may "Here, you can get some milk for yourself."
    may "You can sell it, or whatever you want to do with it."
    mc "Seriously? Thanks"
    may "Yes, you deserved it."
    may "Just be sure to come every once in a while so we wont run out of milk."
    mc "Ok I certainly will."
    $ molly_first = False
    $ cow_milked = True
    $ player_inventory.add_item(301, 2)
    $ Place18.can_map = True
    "{color=#FFAA00}You got 2 bottles of milk.{/color}"
    hide farm
    return

label molly_farm_well_daily:
    show farm 31
    mol "Oh, so its you again [player.name]."
    call molly_farm_menu
    hide farm
    return

label molly_farm_menu:
    show farm 31
    menu:
        mc "So..."
        "Pick the bucket, Im going to milk you.":
            call molly_milk_daily
            return
        "I forgot what I was going to say.":
            mol "Oh...Ok then."
            mc "Bye."
            mol "Bye."
            return
    call molly_farm_menu
    return

label molly_milk_daily:
    mol "Oh, ok I will do it right away."
    mc_thought "Its so funny the way she is 'always ready' when I call her."
    show farm 46
    mol "Here mr [player.name]."
    menu:
        "Good, now lets get going.":
            mol "Yes sir."
        "Good job.":
            mol "I know right?"
        "Yeah Yeah, right":
            mol "So strict."
    if molly_milked_count > 3:
        call molly_stressed
        return
    $ phrase = renpy.random.choice(["Im ready mr", "Im in position mr", "My breasts are ready for you"])
    mol "[phrase]."
    show farm 48
    mc_thought "Man I love this job."
    menu:
        "You seem to be happy.":
            mol "I am always happy to provide milk to those in need."
            mc "You spoke like a true hero."
            mol "Oh, you are so kind."
        "Get those breasts ready.":
            mol "Yes sir!"
    show farm 64
    mol "You are so cute today."
    mc "Thanks Molly."
    menu:
        "Keep talking":
            pass
        "Lift her bra at once":
            call lift_molly_bra
            return
    show farm 67
    menu:
        "You are also very cute today.":
            mol "Oh [player.name], you trully know how to treat a cow when you milk her."
        "Your breasts are also very cute today.":
            mol "Oh [player.name], you trully know how to make a cow happy."
        "You are smelling good today.":
            mol "Oh, did you notice? thats my new shampoo."
    show farm 73
    mc "Now...its about time we begin."
    mol "I agree."
    show farm 77
    mc "They sure are big today."
    mol "They always are when you touch them mr [player.name]."
    mc "I will take that as a compliment."
    show farm 78
    mc "Sure one of the best feelings there is."
    mc_thought "What I like the most is that I can."
    menu:
        "Lift her bra":
            mc_thought "Move her bra up any time I want."
            pass
    show farm 80
    mc "Now."
    menu:
        "How does it fell?":
            mol "So good this freedom feeeling."
        "Now they are all mine to do as I like.":
            mol "So possessive."
    show farm 84
    mc "Indeed."
    mc "But Im enjoying this."
    mol "Me too."
    menu:
        "Grab her breast a little stronger.":
            pass
    show farm 85
    mc "Everything ok?"
    mol "Yes, everything ok."
    mc_thought "I love watching her reactions."
    call molly_after_bra
    return
    

label lift_molly_bra:
    show farm 85:
    mol "Oh, so rough all of sudden"
    menu:
        "Sometimes its necessary.":
            mol "Oh, I understand."
        "Who is on command again?":
            mol "You are mr[player.name]."
        "Say \"Thank you\" Molly.":
            mol "Ahn...Thanks mr [player.name]."
    mc_thought "I just love watching her reactions."
    call molly_after_bra
    return

label molly_after_bra:
    mc "Now lets begin."
    show farm 86
    $ phrase = renpy.random.choice(["Aw", "Ah!", "Huu"])
    mol "[phrase]."
    mc "What was it?"
    mol "I dont know its just...my nipples are kind of sensitive."
    mc "I see, you always react in somewhey when I start messing with them."
    mol "*breathing*"
    mc "But its time to move on."
    show farm 88
    mc_thought "Man...her nipples are bigger right now, I know she likes it."
    mc "Like this..."
    mc "I fell your nipples getting bigger here."
    mol "I feel it too."
    mol "My breasts are more sensitive right now."
    menu:
        "play and turn her nipples a bit":
            pass
    show farm 89
    mol "Ahhh."
    mc "Steady now, you are doing good."
    mol "*breathing faster* Ah, ok. Im holding on."
    mc "Yes you are."
    show farm 90
    mc "A little more sensitive now right?"
    mol "*breathing* Yes."
    mc "we are advancing."
    menu:
        "But we need milk here!":
            mol "I know."
        "All very fun but I still see no milk.":
            mol "Im sorry."
            mc "Its ok, we are getting there."
    show farm 95
    mc "See?"
    mc "There is a little of milk already."
    mol "*breathing* Yes, thats good."
    mol "Oh, good."
    mc "Good indeed."
    mc "Even the smell of your milk is good."
    mol "Do you think?"
    mc "Yes I do."
    mol "Thanks, hehe."
    menu:
        "Now lets fill that bucket!":
            pass
    mol "What?"
    mol "How?"
    show farm 96
    mc "Like this!" with vpunch    
    mol "Haaaaaa!"
    mc "Calm down Molly."
    mc "Just a little big more."
    menu:
        mc_thought "Im feeling confident today, I think I could grab her ass right now."
        "Grab her ass":
            show farm 103
            mol "Ahhhhhh."
            mc_thought "At this point she just goes with it."
            mc_thought "I feel like im in charge here."
            return
        "Just keep pressing her breast in a stronger way":
            mc_thought "Not yet...Im enjoying it like this"
    mol "Ahhhhh."
    mc "Endure it."
    show farm 97
    mc "You are doing very good!"
    mol "Am I?"
    mc "Yes you are."
    mc "Look at how much milk there is already."
    mol "Than..."
    show farm 98
    mol_shout "THAAAAAANKS!!!!!"
    mol_shout "HAAAAAAAAA!!!"
    mc "We need to keep going or we wont fill the bucket."
    mc_thought "I need to start caressing her making keep her mood up."
    show farm 100
    mc "what was this?"
    mol "*heavily breathing* Nothing its just..."
    mc "Just?"
    mol "..."
    show farm 98
    mc "Its ok, you are doing so well today!"
    mol "Am I really?"
    show farm 100
    mc "Yes you are."
    mc "And because of that your milk is going to be even tastier than before."
    mol "Th-*breathing* Thanks [player.name], your words really made my day."
    menu:
        "Grab her boob harder":
            mol "ahhh!"
        "Now just give yourself away to me and relax.":
            mol "Okay"
    show farm 101
    mc "Thats it, good girl!"
    mc "Good girl!"
    mol "[player.name]."
    mc "What?"
    mol "*breathing*...ahh."
    mc_thought "Man she is totally gone."
    show farm 107
    mc_thought "She is crying and feeling pleasure at the same time."
    mc_thought "I can´t even imagine what she is going through."
    mc_thought "Must be fun being a cow."
    mc_thought "What the hell am I even thinking."
    menu:
        mc "Now for our grand finale!"
        "Squeeze her breast with both hands as strong as I can.":
            pass
    show farm 108
    mol_shout "HAAAAAAAAAAAAAAAA!!!!!!!" with vpunch
    mol_shout "SO HAAAAAAAAAAAARD!" with vpunch
    mc "I need to do it or the bucket wont be full."
    mol_shout "I KNOOOOOWWWWWWW!!!!" with vpunch
    mol "*HEAVILY BREATHING*"
    menu:
        "Keep squeezing as long as you can.":
            show farm 109
            mc "Just a little more and we will be done."
            mc_thought "Man, she isnt even responding anymore."
            mc_thought "She just looks and agrees."
            show farm 110 
            mc "I think she is finally empty."
            mc "Not even a single drop is comming out anymore."
        "Stop":
            pass
    mc "Such a good job we did today didnt we?"
    mol "*slowly breathing*"
    mc "Molly?"
    mc "Han...Molly?"
    mc "You really pass out every time dont you?"
    show farm 113
    mc "Well, we did a good job Molly."
    mc "We really did."
    show farm 114
    mc "Always nice to look at that ass."
    mc_thought "Better to deliver this bucket to Mayumi."
    show farm 3
    may "Good job kid."
    may "Take you can take your bottles now."
    $ cow_milked = True
    $ player_inventory.add_item(301, 2)
    $ molly_milked_count += 1
    "{color=#FFAA00}You got 2 bottles of milk.{/color}"
    call time_next
    return

label molly_stressed:
    if molly_stressed_first == True:
        show farm 91
        mc "So strange."
        mc "We tried everything we always do but...the milk stopped coming out."
        mc "And it doesnt seem to be back again any time soon."
        mol "Im sorry I dont know what to say."
        mol "Maybe its the fact that this week was so stressfull."
        mol "Im really sorry."
        mc "Its ok."
        mol "Its probably my stress, Im sorry, cows get stressed every here and there I think."
        mc "We will figure it out."
        mc_thought "Now that Im thinking about it."
        mc_thought "I think I saw something related to cows stress in the internet once."
        mc_thought "If im not mistaken." 
        mc_thought "They need to walk around listen to music or do something they like in order to de-stress."
        mc_thought "But...how to free her from her stress?"
        mc_thought "I think I got an idea"
        show farm 119
        mol "Han, [player.name]? what are you doing?"
        mc "Its nothing I just....I had an idea that may help you and your stress."
        mol "I see, in this case just go ahead then."
        mc "Do you trust me?"
        mol "Yes, I ...I do."
        mc "Then everything will be allright."
        mol "Ok then"
    menu:
        mc_thought "Mayumi doesnt seem to be around."
        "Pull her panties down and take your dick off":
            pass
    show farm 120
    mol "Han...what is this?"
    mc "Its ok just...just trust me ok?"
    mol "Err....ok then."
    mc "Good, now relax."
    show farm 121
    mol "Im trying."
    mc "Everything will be allright."
    mc "Just enjoy it."
    mol "Enjoy what?"
    menu:
        mol "Enjoy what?"
        "Shove your dick inside her pussy":
            pass
    show farm 125
    mol_shout "AAAAAAH!!!!" with vpunch
    mc_thought "Im in."
    mol_shout "What are you doing?" with vpunch
    mc_thought "Its too late now, I cant stop now."    
    mc_thought "I have to keep going."
    show farm vid2 with dissolve
    mc "You will thank me later."
    mc_thought "Or this or im going to be fired."
    mol "*Moaning* I will what? Ahhh!!!"
    mc "Just relax, you stress will pass you will see."
    mc "Just a little more."
    mol "*Moaning*"
    mc "Can you fell it? a good sensation feeling you up?"
    show farm vid4 with dissolve
    mol "*Moaning*"
    mol "Ahhh, Yes I think."
    mol "I think I can."
    mc_thought "Man this is awesome, she is totally into it!"
    mc "Good, just keep focusing on the sensation."
    mol "Ok mr [player.name]."
    mol "*Moaning*, So big!"
    mc_thought "Man, her pussy fells so good, I even though we are doing it slowly."
    mc_thought "She is very tight."
    menu:
        "Can you fell the stress leaving as we go?":
            pass
        "Can you fell my dick entering and the stress leaving?":
            pass
        "Can you fell a good sensation as we go?":
            pass
    show farm vid5 with dissolve
    mol "Ahhh."
    mol "Ah, Y-yes I can, I think I can."
    mc "This means its working."
    mol "I fell it as you shove inside."
    mol "And when you take it out, the only thing I can think is that I want it inside of me again."
    mol "Your dick is so big, it hurts a bit, but its so good when it feels me up."
    mol "Oh mr [player.name], Im in such a shame."
    mc "Its ok, no need to feel shame."
    mc "This is a totally normal phenomenon to free cows from their stress."
    mc_thought "At least from now on it is."
    mol "Oh, is it?"
    mc "Yes."
    mol "Oh in this case I think its ok."
    mc "Do you want me to make it faster?"
    mol "No, I like this way."
    mol "Besides, your dick is too big."
    mol "I dont think I could take it any stronger."
    may_shout "WHAT THE FUCK ARE YOU DOING?" with vpunch
    show farm 132
    mc_thought "SHIT! Thats it, molly, it was nice to know your pussy."
    mc_thought "This is how I get fired."
    may_shout "ANSWER DAMN IT!" with vpunch
    menu:
        mc "I....I...I..."
        "Im taking the stress out of molly so she can produce milk...":
            pass
        "Molly wasnt producing any milk so I had to...":
            pass
        "This is a special method to make the cow produce more milk.":
            pass
    may_shout "Thats not that you idiot!"
    mc_thought "Oh, Man..I cant hold on even with ms Mayumi here..."
    mc_thought "I need to keep fucking her."
    mc_thought "Even if she kills me, there is no stopping it now."
    show farm vid10 with dissolve
    mc_thought "Just what is she doing down there"
    may "You idiots forgot to place the bucket at the right place."
    mc "What?"
    may "You are wasting the cows milk!"
    mol "Im sorry May May."
    may "No need to be sorry Molly, only mind the bucket the next time."
    mc_thought "I didnt even realize that her breasts were dripping milk."
    mc_thought "But, isnt she mad because Im fucking molly in the middle of the farm?"
    may "Now, just a little bit to the right."
    may "And.......all set."
    mc_thought "Man...I dont know why but...the fact she is down there, makes me even more excited."
    may "No, a little more to the left."
    may "Now it is in the right place."
    show farm vid11 with dissolve
    mc_thought "Now she will stay and watch?"
    mc_thought "Fine, watch all you want, your cowgirl is mine now."
    mc "Im sorry for the bucket miss Ma...."
    may "You have to be more firm."
    mc "What?"
    may "Cows like when you show dominance"
    may "Your dick sure is big and beautifull, but you must make it stronger to show her who is on command."
    mol "Miss molly I think this way is just good enough"
    may "Sorry molly. You are not to decide it."
    mc_thought "She said the cows are free to come and go as they wish."
    mc_thought "But, man, the way she talks with Molly, its almost like she owns her."
    mc_thought "Man I want to fuck her even more now."
    may "Are you listening [player.name]?"
    mc "Hun? What?"
    may "Make it stronger!"
    mc "But Molly told me."
    may_shout "Just do it!" with vpunch
    menu:
        "Fuck her faster!":
            pass
    show farm vid9 with dissolve
    mol_shout "Ahhhhh!!! I dont think I can take it!"
    mol_shout "Its just too much!"
    mol "*moaning harder*"
    mc "*Breathing* you are doing very well Molly."
    mol "AAAAAAH! thanks [player.name]!!!"
    mol "My pussy never felt anything like this!"
    mol "I dont think I can take it!!!!"
    may "Keep going [player.name], she can take it."
    mc_thought "Mayumi doesnt have any sense of compasion here."
    mc_thought "Even I am getting near my limit here."
    show farm vid12 with dissolve
    may "HARDER!"
    mol_shout "AAAAAAAAAH!"
    may "Yes, like this."
    may "Fuck her like you own her!" with vpunch
    menu:
        "Ok!":
            pass
        "Got it!":
            pass
    mc_thought "I dont think...."
    mol "May May, this is too much for me!"
    may "Yes you can."
    mc_thought "She is at her limit."
    mc_thought "Even her voice changed."
    mol "Ahhhhhh!"
    mol "I dont think so."
    mol "*moaning*"
    may "Keep going [player.name]."
    may "She can take it, she will take it!"
    mc "I dont think I...can go much longer either!"
    may "She is already having an orgasrsm so you need to keep going."
    may "Dont stop."
    mc "But I.."
    mol "You are just going too rough on me!"
    mc "Ms Mayumi, Im..."
    may "What?"
    mc "Im about to cum!"
    may "Hold it, not yet."
    mc "I dont think I can do it much longer!"
    may "Just a little more."
    may "You are owning her right now."
    mol_shout "Ahhhhhhhhh!!!!"
    mc "Im cumming!!!!" with vpunch
    may "Keep going!"
    mc "What?"
    may "You listened, keep going!"
    mc "I dont know if I...."
    mc_thought "This is crazy"
    mol "I can feel it, I can feel it inside me."
    menu:
        "Keep going":
            may "Keep fucking her till your limit"
            mc "Im ....fucking her!"
            may "Yes show her."
            mc "I...I dont know if I can..."
            mc "I cant anymore, this is my limit."
        "Just stop":
            pass
    show farm 137
    mc "*breathing*"
    mc "Oh man, that was crazy."
    mol "*heavily breathing*"
    mc_thought "I never...had any sex like this in my life."
    mc_thought "So intense."
    mc_thought "Mayumi turned this into something else."
    may "Good!"
    mol "Than-*breathing*-Thanks."
    may "Very good"
    mc "What?"
    may "No she knows you are on command."
    mol "*heavily breathing*"
    may "do this in a more frequent rithim and your milking life will get a lot easyer from now on."
    mc "Oh...I see"
    show farm 141
    mc_thought "Man..I hate to admit it but, even my dick is tired."
    may "Your dick is all wet and full of cum."
    mol "*heavily breathing*"
    mc "I know.."
    may "It seems like its not as hard as before but is still hard."
    mc "Yes *breathing*, at least for a while."
    may "Then put it back in."
    mol "What?"
    mc "What?"
    may "Put it back inside."
    mc "But we finished."
    may "Your dick says otherwise."
    may "Even if you dont have enough energy, put it back inside and do it slowly."
    show farm vid13 with dissolve
    pause 0.9
    show farm vid11 with dissolve
    mol "Please miss mayumi."
    may "Not now Molly, be a good cowgirl and do your job."
    mol "Okay."
    scene black with Dissolve(1.0)
    mc_thought "She made me fuck her again."
    mc_thought "I cant really complain."
    mc_thought "But Im so tired!"
    hide blacked
    show farm 156 with dissolve
    mc_thought "And she passed out again."
    mc_thought "Beautifull view though."
    $ molly_milked_count = 0
    call time_next
    call time_next
    $ fuck_molly_first = True
    return

    




    



    

    
    


    

    
    