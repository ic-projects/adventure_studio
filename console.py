import curses

from curses import wrapper
from curses import panel

# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

def go_smwh(x):
    return l1[x]



l1 = ["North", "South", "West", "East"]
l2 = ["go", "actions", "...?"] 

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # p1 = curses.panel.new_panel(stdscr)

    # stdscr.addstr("Where do you want to go?\n", curses.A_BOLD)
    # for elem in l:
    #     stdscr.addstr("  {}\n".format(elem))

    # Create the menu
    menu = CursesMenu("This is the quest of thejhafjdhl\nYou are in the living room",
                    "What do you want to do?")

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Clicking on this will do nothing..?")

    # A FunctionItem runs a Python function when selected
    function_item = FunctionItem("West", go_smwh, [2])

    # TODO Use this to give possibility to save user's input
    # # A CommandItem runs a console command
    # command_item = CommandItem("Run a console command",  "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    for y in range(len(l1)):
        funitem = FunctionItem("West", go_smwh, [y])
        menu.append_item(funitem)
    
    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    # menu.append_item(menu_item)
    menu.append_item(function_item)
    # menu.append_item(command_item)
    menu.append_item(submenu_item)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

    function_item.get_return()

    stdscr.refresh()
    stdscr.getkey()


wrapper(main)

stdscr.keypad(False)
curses.nocbreak()
curses.echo()