import curses

win = curses.initscr()
win.addstr("Hello World !!!")
win.refresh()
win.getch()
curses.endwin()
