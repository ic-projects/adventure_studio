import random
import printing
import asciipictures

class Event:
    def __init__(self, prob, description):
        self.prob = prob
        self.description = description
        self.fight = False
        self.image = ""
    
    def add_room_fighter(figher):
        self.fight = True
        self.fighter = fighter
    
    def add_image(self, image):
        self.image = image

    def trigger(self, stdscr):
        if random.random() <= self.prob:
            printing.print_at_speed(self.description, 140)
            if self.fight:
                fight(self.ennemy)
            if self.image:
                stdscr.addstr(asciipictues.display(picture) + "\n")