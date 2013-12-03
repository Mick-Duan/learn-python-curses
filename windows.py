import curses
import atexit

def cleanup(): 
    curses.nocbreak() 
    win.keypad(0) 
    curses.echo() 
    curses.endwin() 


def create_newwin(nlines,nclos,begin_y,begin_x):
    local_win = curses.newwin(nlines,nclos,begin_y,begin_x)
    local_win.box()
    local_win.refresh()
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
    win.keypad(1)
    atexit.register(cleanup) 
    height = 3
    width = 10
    (lines,clos) = win.getmaxyx()
    starty = (lines - height) / 2
    startx = (clos - width) / 2
    win.addstr("Press F1 to exit")
    win.refresh()
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
