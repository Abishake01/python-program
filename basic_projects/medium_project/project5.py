#Typing Test

import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome To the Speed Typing Test!')
    stdscr.addstr('\nPress any key to begin!')
    stdscr.refresh() 
    stdscr.getkey()
    
def wpm_test(stdscr):
    target_text='Hello World this is some test text for this app!'
    current_text=[]
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh() 
    
    while True:
        key=stdscr.getkey()
        current_text.append(key)
        
        stdscr.clear()
        stdscr.addstr(target_text)
        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))
        stdscr.refresh()
def main(stdscr):
    
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)#curses.init_pair(number,text color,background color)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    #stdscr.addstr(row ,col,'string')
    #stdscr.addstr('Hello Welcome!',curses.color_pair(1))
    start_screen(stdscr)
    wpm_test(stdscr)
     
    
wrapper(main)