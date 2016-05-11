import curses
import random
import time

q = 0
head = ">"
win = curses.initscr()
border = win.getmaxyx()
heady = int(int(border[0])/2)
headx = int(int(border[1])/2)
yAppl = random.randrange(0, border[0])
xAppl = random.randrange(0, border[1])
points = 0
direct = 8

win.nodelay(1)
def declarations():
    win = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
    win.bkgd("." , curses.color_pair(1))

declarations()

def food():
    global q, heady, headx, yAppl, xAppl, points
    win.addch(yAppl, xAppl, "#", curses.color_pair(2))
    if heady == yAppl and headx == xAppl:
        points += 1
        win.delch(yAppl, xAppl)
        yAppl = random.randrange(0, border[0])
        xAppl = random.randrange(0, border[1])
        win.refresh()
    win.addstr(0, 0, "Points:" + str(points), curses.color_pair(2))

def forward():
    global q, heady, headx, direct
    if direct ==  4 and headx > 1:
        headx -= 1
    elif direct ==  6  and headx < border[1] - len(head):
        headx += 1
    elif direct == 5 and heady < border[0] - 1:
        heady += 1
    elif direct == 8 and heady > 0:
        heady -= 1
    time.sleep(0.15)

def move():
    global head, q, heady, headx, direct
    direct = 0
    q = -1
    headx, heady = int(int(border[1])/2),int(int(border[0])/2)
    while q != ord("q"):
        win.clear()
        food()
        forward()
        win.addstr(heady, headx, head, curses.color_pair(2))
        win.refresh()
        q = win.getch()
        if q == ord("8") and heady > 0:
            head = "^"
            direct = 8
        elif q == ord("5") and heady < border[0] - 1:
            head = "v"
            direct = 5
        elif q == ord("6") and headx < border[1] - len(head):
            head = ">"
            direct = 6
        elif q == ord("4") and headx > 0:
            head = "<"
            direct = 4
        if heady == border[0]-1 and headx == border[1] - len(head):
            if q == ord("5"):
                heady -= 1
            elif q == ord("6"):
                headx -= 1
        if heady == border[0]-1 and headx == border[1] - len(head):
            if q == ord("5"):
                heady -= 1
            elif q == ord("6"):
                headx -= 1
        time.sleep(0)

move()
curses.endwin()
