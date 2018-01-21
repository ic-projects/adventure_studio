import curses

class Tree:
    def __init__(self, start, locations):
        self.start = start
        self.locations = locations
    def execute(self):
        # Setup curses
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        locn = self.start
        while locn != None:
            locn = locn.enter(stdscr)
