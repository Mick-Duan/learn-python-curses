import curses

mesg = "mick test print"
win = curses.initscr()
(y,x) = win.getmaxyx()
win.addstr(y/2,(x-len(mesg))/2,"%s" % mesg)
win.addstr(y-2,0,"This screen has %d rows and %d columns\n" % (y,x))
win.addstr("Try resizing your window(if possible) and then run this program again")
win.refresh()
win.getch()
curses.endwin()
