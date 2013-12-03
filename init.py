import curses

win = curses.initscr()
curses.raw()
win.keypad(1)
curses.noecho()
win.addstr("Type any character to see it in bold\n")
ch = win.getch()
if ch == curses.KEY_F1:
    win.addstr("F1 Key pressed")
else:
    win.addstr("The pressed key is: ")
    win.attron(curses.A_BOLD)
    win.addstr("%c" % ch)
    win.attroff(curses.A_BOLD)
win.refresh()
win.getch()
curses.endwin()


