import curses
import time
q = 0
head = ">"
win = curses.initscr()
border = win.getmaxyx()
heady = int(int(border[0])/2)
headx = int(int(border[1])/2)
direct = 8
body = lng 

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
    time.sleep(0.1)

def move():
    global head, q, heady, headx, direct
    direct = 0
    q = -1
    headx, heady = int(int(border[1])/2),int(int(border[0])/2)
    while q != ord("q"):
        win.clear()
        forward()
        win.addstr(heady, headx, head, curses.color_pair(2))
        forward()
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
win = curses.initscr()
border = win.getmaxyx()
move()
curses.endwin()
#cd Codecool/Python/FPG/FirstPythonGame
