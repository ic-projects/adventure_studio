import printing

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.carryable = False 
    
    def make_carryable(self):
        self.carryable = True

    def pickup(self, this, key):
        if self.carryable:
            printing.print_at_speed("You pickup the " + self.name + ".", 120)
            this.inventory[key] = self
        else:
            printing.print_at_speed("Can't pickup " + self.name + "!!!", 120)

