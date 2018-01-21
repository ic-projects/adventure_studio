import curses

class Tree:
    def __init__(self, start, locations):
        self.start = start
        self.locations = locations
        self.inventory = {}
    def execute(self):
        # Setup curses
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        stdscr.keypad(True)

        locn = self.start
        while locn != None:
            locn = locn.enter(self, stdscr)
