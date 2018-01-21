import printing
import asciipictures

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.carryable = False 
        self.image = ""
    
    def make_carryable(self):
        self.carryable = True
    
    def add_image(self, image):
        self.image = image
    
    def show(self):
        if self.image == "":
            return "No pictures available"
        else:
            return asciipictures.display(self.image)

    def pickup(self, this, key):
        if self.carryable:
            printing.print_at_speed("You pickup the " + self.name + ".", 120)
            this.inventory[key] = self
        else:
            printing.print_at_speed("Can't pickup " + self.name + "!!!", 120)

