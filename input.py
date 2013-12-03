import curses

mesg = "Enter a string: "
win = curses.initscr()
(y,x) = win.getmaxyx()
win.addstr(y/2,(x-len(mesg))/2,"%s" % mesg)
string = win.getstr()
win.addstr(y-2,0,"You Entered: %s" % string)
win.getch()
curses.endwin()
