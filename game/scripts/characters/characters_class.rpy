init python:
    class Girl(object):
        def __init__(self, id, name, revealed, phase, race, role, relationship, pregnant, book_phrase, max_phase, marital_status, curiosity):
    # default linda = Girl(01, "Linda", True, 0, "linda_frame", "Human", "", "Friendly", 0, "Nothing for now", 1, "Single")
            self.id = id
            self.name = name
            self.revealed = revealed
            self.phase = phase
            self.race = race
            self.role = role
            self.relationship = relationship
            self.pregnant = pregnant
            self.book_phrase = book_phrase
            self.max_phase = max_phase
            self.marital_status = marital_status
            self.curiosity = curiosity
            if self in all_girls:
                pass
            else:
                all_girls.append(self)
        
        def book_check(self):
            # update the other ones
            if aphrodite.phase == 0:
                aphrodite.phase = 1
                aphrodite.book_phrase = "this and that"
            if ashley.phase == 0:
                ashley.phase = 1
            if sarah.phase == 0 and flowers_sarah_level == 2:
                sarah.phase = 1
            if makoto.phase == 0 and witch_talk_first == True:
                makoto.phase = 1
            if monica.phase == 2 and aphrodite.revealed == True and linda.phase == 3:
                monica.phase = 3
            # update everyone
            if self.phase == 0:
                return
            self.book_phrase = str(eval (self.name.lower() + "_phase" + str(self.phase)))
            return