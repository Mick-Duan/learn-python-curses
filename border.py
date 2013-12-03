import curses
import atexit

def cleanup(): 
    curses.nocbreak() 
    win.keypad(0) 
    curses.echo() 
    curses.endwin() 


def create_newwin(nlines,nclos,begin_y,begin_x):
    local_win = curses.newwin(nlines,nclos,begin_y,begin_x)
    local_win.attron(curses.color_pair(2))
    local_win.border('|', '|', '-', '-', '+', '+', '+', '+')
    local_win.refresh()
    local_win.attroff(curses.color_pair(2))
    return local_win

def destroy_win(win):
    win.border()
    win.clear()
    win.refresh()


def main():
    global win
    win = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    win.keypad(1)
    atexit.register(cleanup) 
    height = 5
    width = 10
    (lines,clos) = win.getmaxyx()
    starty = (lines - height) / 2
    startx = (clos - width) / 2
    win.attron(curses.color_pair(1))
    win.addstr("Press F1 to exit")
    win.refresh()
    win.attroff(curses.color_pair(1))
    my_win = create_newwin(height, width, starty, startx)
    ch = int()
    while ch != curses.KEY_F1:
        ch = win.getch()
        if ch == curses.KEY_LEFT:
            destroy_win(my_win)
            startx-=1
            my_win = create_newwin(height, width, starty, startx)
        if ch == curses.KEY_RIGHT:
            destroy_win(my_win)
            startx+=1
            my_win = create_newwin(height, width, starty, startx)
        if ch == curses.KEY_UP:
            destroy_win(my_win)
            starty-=1
            my_win = create_newwin(height, width, starty, startx)
        if ch == curses.KEY_DOWN:
            destroy_win(my_win)
            starty+=1
            my_win = create_newwin(height, width,starty, startx)
    curses.endwin()

if __name__ == "__main__":
    main()
