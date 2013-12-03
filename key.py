import curses
import atexit

def cleanup(): 
    curses.nocbreak() 
    win.keypad(0) 
    curses.echo() 
    curses.endwin()

def print_menu(menu_win,highlight):
    global choices
    x = 2
    y = 2
    i = 0
    choices = [
               'Choice 1',
               'Choice 2',
               'Choice 3',
               'Choice 4',
               'Exit'
               ]
    menu_win.clear()
    menu_win.box()
    menu_win.refresh()
    while i < len(choices):
        if highlight == i+1:
            menu_win.attron(curses.A_REVERSE)
            menu_win.addstr(y,x,"%s" % choices[i])
            menu_win.attroff(curses.A_REVERSE)
        else:
            menu_win.addstr(y,x,"%s" % choices[i])
        y+=1
        i+=1
    menu_win.refresh()

def main():
    global win
    global menu_win
    win = curses.initscr()
    curses.noecho()
    curses.cbreak()
    win.clear()
    WIDTH = 30
    HEIGHT = 20
    highlight = 1
    startx = (80 - WIDTH) / 2
    starty = (24 - HEIGHT) / 2
    win.addstr("Use arrow keys to go up and down, Press enter to select a choice")
    win.refresh()
    atexit.register(cleanup) 
    global menu_win
    menu_win = curses.newwin(HEIGHT, WIDTH, starty, startx)
    menu_win.keypad(1)
    print_menu(menu_win, highlight)
    while True:
        ch = menu_win.getch()
        if ch == curses.KEY_UP:
            if highlight == 1:
                highlight = len(choices)
            else:
                highlight-=1
        elif ch == curses.KEY_DOWN:
            if highlight == len(choices):
                highlight = 1
            else:
                highlight+=1
        elif ch == 10:
            print_menu(menu_win, highlight)
            break
        else:
            win.addstr(24, 0, "Charcter pressed is = %3d Hopefully it can be printed as" % ch);
            win.refresh()
        print_menu(menu_win, highlight)
    win.addstr(23, 0, "You chose choice with choice string <%s> \n" % choices[highlight])
    win.clrtoeol()
    win.refresh()
    win.getch()
    curses.endwin()
            
if __name__ == "__main__":
    main()
