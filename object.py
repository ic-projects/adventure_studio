import printing

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.carryable = False 
    
    def make_carryable(self):
        self.carryable = True

    def pickup(self, this, key, stdscr):
        stdscr.clear()
        if self.carryable:
            stdscr.addstr("You pickup the " + self.name + ".\n")
            this.inventory[key] = self
        else:
            stdscr.addstr("Can't pickup " + self.name + "!\n")
        stdscr.getch()
        stdscr.refresh()

