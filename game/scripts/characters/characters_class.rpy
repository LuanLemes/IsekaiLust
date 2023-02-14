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
