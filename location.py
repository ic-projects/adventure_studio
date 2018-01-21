import curses

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = {}
        self.navigation = {}

    def add_nav(self, dirn, dest):
        self.navigation[dirn] = dest

    def add_obj(self, obj_id, obj):
        self.objects[obj_id] = obj

    def enter(self, stdscr):
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
            self.objects[operand].pickup()

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

        stdscr.refresh()

        return (count, command, operand)
