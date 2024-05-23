#Typing Test

import curses
from curses import wrapper
def main(stdscr):
    stdscr.clear()
    stdscr.addstr('Hello Welcome!')
    stdscr.refresh()
    stdscr.getkey()
    
wrapper(main)