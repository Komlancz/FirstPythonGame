import curses
import time
def declarations():
    win = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
    win.bkgd("." , curses.color_pair(1))
    return
def move(worm,head):
    q = -1
    x, y = 0, 0
    Vertical = 1
    Horizontal = 1
    while q != ord("q"):
        win.clear()
        win.addstr(y, x, worm + head, curses.color_pair(2))
        win.refresh()
        q = win.getch()
        if q == ord("8") and y > 0:
            y -=1
        elif q == ord("2") and y < border[0] - 1:
            y +=1
        elif q == ord("6") and x < border[1] - len(worm + head):
            x +=1
        elif q == ord("4") and x > 0:
            x -=1
        if y == border[0]-1 and x == border[1] - len(worm + head):
            if q == ord("2"):
                y -= 1
            elif q == ord("6"):
                x -= 1
    time.sleep(0)
#def wormbody(x,y,q)
declarations()
head = ">"
worm = "<oo:"
win = curses.initscr()
border = win.getmaxyx()
#ground = curses.newwin(border[0], border[1], 0, 0)
#ground.refresh()
move(worm,head)
time.sleep(0)
#curses.endwin()
