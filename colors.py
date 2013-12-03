import sys
import curses
import atexit

def print_in_middle(stdscr, starty, startx, width,strings):
    
    

def main():
    win = curses.initscr()
    if not curses.has_colors():
        curses.endwin()
        print("Your terminal does not support color\n")
        sys.exit(1)
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    win.attron(curses.COLOR_PAIR(1));
    print_in_middle(win, LINES / 2, 0, 0, "Viola !!! In color ...")
    win.attroff(curses.COLOR_PAIR(1));
    win.getch()
    curses.endwin()
        

if __name__ = "__main__":
    main()