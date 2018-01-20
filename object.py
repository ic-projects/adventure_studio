import printing

class Object:
    def __init__(self, name, description, carryable):
        self.name = name
        self.description = description
        self.carryable = carryable

    def pickup(self):
        printing.print_at_speed("You pickup the " + self.name + ".", 120)
