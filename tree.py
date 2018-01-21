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

        last_locn = None
        locn = self.start
        while locn != None:
            next_lcon = locn.enter(self, stdscr, last_locn)
            last_locn = locn
            locn = next_lcon
