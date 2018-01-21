import sys, time, random, select, curses

# from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

# wrapper(main)

def slow_print(main, direction):
    speed = 60
    for l in main:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() *10.0/speed)
        if select.select([sys.stdin,],[],[],0.0)[0]:
            print(main)
            sys.stdin.flush ()
            return
    print ('') #newline
    for l in direction:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.03)
    print ('')


def print_at_speed(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() *10.0/speed)
        if select.select([sys.stdin,],[],[],0.0)[0]:
            print(text, "\n")
            sys.stdin.flush ()
            return
    print ('') #newline

# stdscr.clear()
# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)
# slow_print("HELLOOOOOOOOOOOOOOOOOOOO\n", "Love <33333")
# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()