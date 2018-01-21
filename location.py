import curses
import printing, utils
import myevent
import object

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = {}
        self.navigation = {}
        self.events = {}

    def add_nav(self, dirn, dest):
        self.navigation[dirn] = dest
    
    def add_events(self, events):
        for event in events:
            self.events[event] = myevent.Event(events[event]['prob'],  events[event]['description'])

    def add_objects(self, objs):
        for obj in objs:
            self.objects[obj] = object.Object(objs[obj]['name'], objs[obj]['description'])
            try:
                if objs[obj]['carryable'] == 'yes':
                    self.objects[obj].make_carryable()
            except:
                KeyError

    def enter(self, this, stdscr):
        next_locn = self

        selection = 0
        command = ""
        operand = ""

        while(True):
            count, command, operand = self.print_menu(stdscr, selection)

            key = stdscr.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                break
            elif key == curses.KEY_UP:
                selection = (selection - 1) % count
            elif key == curses.KEY_DOWN:
                selection = (selection + 1) % count
    
        if command == "go":
            return self.navigation[operand]
        if command == "pickup":
            self.objects[operand].pickup(this, operand)
        if command == "inventory":
            self.print_inventory(this, stdscr)

    def print_menu(self, stdscr, selection):
        count = 0
        command = ""
        operand = ""
        
        stdscr.clear()
        stdscr.addstr(self.description + "\n")

        for dirn, dest in self.navigation.items():
            stdscr.addstr("To the " + dirn + " there is " + dest.name + "\n")

        for dirn, dest in self.navigation.items():
            if count == selection:
                stdscr.addstr("* : Go " + dirn + "\n")
                command = "go"
                operand = dirn
            else:
                stdscr.addstr(str(count + 1) + " : Go " + dirn + "\n")
            count += 1

        for obj_id, obj in self.objects.items():
            if count == selection:
                stdscr.addstr("* : Pickup " + obj_id + "\n")
                command = "pickup"
                operand = obj_id
            else:
                stdscr.addstr(str(count + 1) + " : Pickup " + obj_id + "\n")
            count += 1

        if count == selection:
            stdscr.addstr("* : Inventory\n")
            command = "inventory"
        else:
            stdscr.addstr(str(count + 1) + " : Inventory\n")
        count += 1

        stdscr.refresh()

        return (count, command, operand)

    def print_inventory(self, this, stdscr):
        stdscr.addstr("Inventory:\n\n")
        for item in this.inventory:
            stdscr.addstr(this.inventory[item].name + ": " + this.inventory[item].description + "\n")

        stdscr.getchr()