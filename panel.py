import curses
from curses import panel
import time
import atexit
import threading

def cleanup(): 
    curses.nocbreak()
    curses.echo() 
    curses.endwin()

def display(win, interval=1):
    try:
        while 1:
            win.addstr("interval:" + str(interval))
            interval+=1
            win.refresh()
    except:
        pass
    
def main():
    global my_wins0
    global my_wins1
    win = curses.initscr()
    curses.cbreak()
    curses.noecho()
    (y,x) = win.getmaxyx()
    lines = (y-1*3)/2
    cols = (x-1*3)/2
    my_wins0 = curses.newwin(lines,cols,0,0)
    my_wins1 = curses.newwin(lines,cols,0,cols)
    my_wins2 = curses.newwin(lines,cols,lines,0)
    my_wins3 = curses.newwin(lines,cols,lines,cols)
#    my_wins2 = curses.newwin(lines,cols,y+2,x+50)
#    my_wins2 = curses.newwin(lines,cols,y+2,x+50)
    my_wins2.box()
    my_wins3.box()
    my_wins1.box()
    my_wins0.box()
    my_panels1 = panel.new_panel(my_wins0)
    my_panels2 = panel.new_panel(my_wins1)
    my_panels3 = panel.new_panel(my_wins2)
    my_panels4 = panel.new_panel(my_wins3)
    #display(my_panels1)
    global a
    a=1
    while 1:
        go1()
        go2()
        curses.panel.update_panels()
        curses.doupdate()

def go1():
#    global a
    #while 1:
    my_wins1.addstr(1,1,"hahaa:")
#        my_wins0.addstr(1,1,"wocao:" + str(a))
#        a+=1
        #curses.panel.update_panels()
        #curses.doupdate()
#    except:
#        win.getch()
#        curses.endwin()
    
def go2():
#    global a
    #while 1:
 #       my_wins1.addstr(1,1,"hahaa:" + str(a))
    my_wins0.addstr(1,1,"wocao:")
        #curses.panel.update_panels()
        #curses.doupdate()
if __name__ == "__main__":
    main()
