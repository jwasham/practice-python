import curses

win = curses.initscr()
key = win.getch()

print(str(key))
