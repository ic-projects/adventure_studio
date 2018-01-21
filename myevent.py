import random
import printing

class Event:
    def __init__(self, prob, description):
        self.prob = prob
        self.description = description
        self.fight = False
    
    def add_room_fighter(figher):
        self.fight = True
        self.fighter = fighter

    def trigger(self):
        if random.random() <= self.prob:
            printing.print_at_speed(self.description, 140)
            if self.fight:
                fight(self.ennemy)