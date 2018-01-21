import sys, time, random, select, curses

# from curses import wrapper

def print_at_speed(text, speed, stdscr):
    stdscr.nodelay(1)
    for i in range(len(text)):
        stdscr.addstr(text[i])
        stdscr.refresh()
        if stdscr.getch() == curses.ERR:
            time.sleep(random.random() *10.0/speed)
        else:
            stdscr.addstr(text[i + 1:])
            break
    stdscr.addstr('\n') #newline
    curses.flushinp()
    stdscr.nodelay(0)
