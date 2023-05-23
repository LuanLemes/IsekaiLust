init python:
    class H_Event(object):
        def __init__(self, id, name, bigger_than, smaller_then, v_true, v_false, event_characters, event_label_name, event_tags):
            self.id = id
            self.name = name
            self.bigger_than = bigger_than
            self.smaller_then = smaller_then
            self.v_true = v_true
            self.v_false = v_false
            self.event_characters = event_characters
            self.event_label_name = event_label_name
            self.completed = "False"
        def completion_check(self):
            say(mc,"test")
            if self.bigger_than != "":
                if int(eval(self.bigger_than[0])) >= int(self.bigger_than[1]):
                    self.completed = True
                    return True
            if self.smaller_then != "":
                if int(eval(self.smaller_then[0])) <= int(self.smaller_then[1]):
                    self.completed = True
                    return True
            if self.v_true != "":
                if eval(self.v_true) == True:
                    self.completed = True
                    return True
            if self.v_false != "":
                if eval(self.v_false) == False:
                    self.completed = True
                    return True
            say (mc ,"deu rim")
            self.completed = False
            return False
            

    scene1 = H_Event(1, "Morning Hug", "", "", "linda.revealed", "", ["Linda"], "", [])
    scene2 = H_Event(2, "", "", "", "flower_camp_first", "flower_camp_first", ["Monica"], "", [])
    scene3 = H_Event(3, "Exercising", "", "", "ashley_danced", "", ["Ashley", "Monica"], "", [])
    scene4 = H_Event(4, "Looked (sofa)", "", "", "monica_looked", "", ["Linda","Monica"], "", [])
    scene5 = H_Event(5, "Guild exam first try", "", "", "witch_talk_first", "", ["Makoto"], "", [])
    scene6 = H_Event(6, "Sex with a wolf girl", "", "", "", "first_unknown_girl", ["Unknown Girl"], "", [])
    scene7 = H_Event(7, "The big snake", ["monica.phase1", 1] , "", "", "", ["Monica"], "", [])
    scene8 = H_Event(8, "Stuck Flower", "sarah_flowers_level_2_first", "", "", "", ["Sarah"], "", [])
    scene9 = H_Event(9, "Do you think Im a good mom?", "", "", "monica_shower_scene", "", ["Monica"], "", [])
    scene10 = H_Event(10, "I cant do that yet", "", "", "linda_touch_one", "", ["Linda"], "", [])
    scene11 = H_Event(11, "Watching the moon", "", "", "lilith.revealed", "", ["Lilith"], "", [])
    scene12 = H_Event(12, "Sunlit Freedom", "", "", "lilith.revealed", "", ["Monica"], "", [])
    scene13 = H_Event(13, "water drink ", "", "", "lilith.revealed", "", ["Sarah", "Monica"], "", [])
    scene13 = H_Event(13, "water drink ", "", "", "lilith.revealed", "", ["Sarah", "Monica"], "", [])





