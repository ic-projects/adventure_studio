import printing
import asciipictures

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.carryable = False 
        self.image = ""
        self.pickup_cmd = []
    
    def add_pickup_cmd(self, cmd):
        self.pickup_cmd.append(cmd)
    
    def make_carryable(self):
        self.carryable = True
    
    def add_image(self, image):
        self.image = image
    
    def show(self):
        if self.image == "":
            return "No pictures available"
        else:
            return asciipictures.display(self.image)

    def pickup(self, this, key, stdscr):
        stdscr.clear()
        for cmd in self.pickup_cmd:
            cmd.execute()
        if self.carryable:
            printing.print_at_speed("You pickup the " + self.name + ".\n", 100, stdscr)
            this.inventory[key] = self
        else:
            printing.print_at_speed("Can't pickup " + self.name + "!\n", 100, stdscr)
        stdscr.getch()
        stdscr.refresh()

