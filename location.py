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
            try:
                self.objects[obj].add_image(objs[obj]['image'])
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
            next_locn = self.navigation[operand]
        if command == "pickup":
            self.objects[operand].pickup(this, operand, stdscr)
        if command == "inventory":
            self.print_inventory(this, stdscr)

        return next_locn

    def print_menu(self, stdscr, selection):
        count = 0
        command = ""
        operand = ""
        
        stdscr.clear()
<<<<<<< HEAD
        stdscr.addstr(self.description + "\n")
        
        for event in self.events:
            self.events[event].trigger(stdscr)
=======
        stdscr.addstr(self.description + "\n\n")
>>>>>>> c067f0588ad96f7e6053f81d1844d251670ffb10

        for dirn, dest in self.navigation.items():
            stdscr.addstr("To the " + dirn + " there is " + dest.name + ".\n")
        stdscr.addstr("\n")

        for dirn, dest in self.navigation.items():
            menu_string = "-> Go " + dirn + "\n"
            if count == selection:
                stdscr.addstr(menu_string, curses.A_REVERSE)
                command = "go"
                operand = dirn
            else:
                stdscr.addstr(menu_string)
            count += 1

        for obj_id, obj in self.objects.items():
            menu_string = "-> Pickup " + obj_id + "\n"
            if count == selection:
                stdscr.addstr(menu_string, curses.A_REVERSE)
                command = "pickup"
                operand = obj_id
            else:
                stdscr.addstr(menu_string)
            count += 1

        menu_string = "-> Inventory\n"
        if count == selection:
            stdscr.addstr(menu_string, curses.A_REVERSE)
            command = "inventory"
        else:
            stdscr.addstr(menu_string)
        count += 1

        stdscr.refresh()

        return (count, command, operand)

    def print_inventory(self, this, stdscr):
        stdscr.clear()
        stdscr.addstr("Inventory:\n\n")
        for item in this.inventory:
            stdscr.addstr(this.inventory[item].name + ": " + this.inventory[item].description + "\n")
        stdscr.refresh()

        stdscr.getch()