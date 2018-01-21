import random
import printing
import asciipictures

class Event:
    def __init__(self, prob, description):
        self.prob = prob
        self.description = description
        self.fight = False
        self.image = ""
        self.cond = None
        self.thenC = []
        self.elseC = []
    
    def add_cond(self, cond):
        self.cond = cond

    def append_then(self, x):
        self.thenC.append(x)
    
    def append_else(self, x):
        self.elseC.append(x)
    
    def add_room_fighter(figher):
        self.fight = True
        self.fighter = fighter
    
    def add_image(self, image):
        self.image = image

    def trigger(self, stdscr):
        if random.random() <= self.prob:
            printing.print_at_speed(self.description, 100, stdscr)
            if self.cond != None:
                if self.cond.eval():
                    for cmd in self.thenC:
                        cmd.execute()
                else:
                    for cmd in self.elseC:
                        cmd.execute()
            if self.fight:
                fight(self.ennemy)
            if self.image != "":
                stdscr.addstr(asciipictues.display(picture) + "\n")