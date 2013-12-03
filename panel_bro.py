import curses
from curses import panel
import atexit

def cleanup(): 
    curses.nocbreak()
    curses.echo() 
    curses.endwin()
    
def init_wins(wins, n):
    lines = 10
    cols = 40
    y = 2
    x = 10
    i = 0
    while i < n:
        win + str(i) = curses.newwin(lines,cols,y,x) 
        
    
    
def main():
    y = 2
    x = 4
    win = curses.initscr()
    win.start_color()
    curses.cbreak()
    curses.noecho()
    win.keypad(1)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    my_wins0 = curses.newwin(lines,cols,y,x)
    my_wins1 = curses.newwin(lines,cols,y+1,x+5)
    my_wins2 = curses.newwin(lines,cols,y+2,x+50)
    my_wins2.box()
    my_wins1.box()
    my_wins0.box()
    my_panels1 = panel.new_panel(my_wins0)
    my_panels2 = panel.new_panel(my_wins1)
    my_panels3 = panel.new_panel(my_wins2)
    curses.panel.update_panels()
    curses.doupdate()
    win.getch()
    curses.endwin()

def main_panels(win):
    global stdscr, nap_msec, mod
    stdscr = win
    stdscr.refresh()
    
    
#
# one fine day there'll be the menu at this place
#
curses.wrapper(main_panels)
