
import curses
import app.universal


class Game:
    def __init__(self):
        print("Game")
        self.m = 0
        self.scr = curses.window
        self.maxX = 0
        self.maxY = 0
        self.universal = app.universal.Universal()
        self.menudict = {'Show scores': 1, 'New Games': 0, 'About': 0, 'Exit': 0}

    def intro(self):
        pass

    def onInit(self):
        print("Init Game")
        self.scr = curses.initscr()
        self.maxX = self.scr.getmaxyx()[1]
        self.maxY = self.scr.getmaxyx()[0]
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        self.scr.refresh()
        return True

    def drawmenu(self):
        i = 0
        for key in self.menudict:
            self.scr.move((int(self.maxY / 2) - len(self.menudict)) + i, int(self.maxX / 2) - 10)

            if self.menudict[key] == 1:
                self.scr.attron(curses.A_REVERSE)

            if self.menudict[key] == 0:
                self.scr.attroff(curses.A_REVERSE)

            self.scr.addstr(key)
            self.scr.refresh()
            i += 2

    def kbhit(self):
        ch = self.scr.getch()
        if ch == -1:
            return False
        else:
            curses.ungetch(ch)
            return ch

    def menu(self):
        self.m += 1
        self.drawmenu()
        self.scr.nodelay(True)
        self.scr.keypad(True)

        menu_keys = list(self.menudict.keys())
        max_pos_menu = len(menu_keys) - 1
        index = 0

        while (chh := self.kbhit()) != 27:
            if not chh:
                continue

            if chh:
                curses.flushinp()

                if chh == 259:  # up
                    self.menudict[menu_keys[index]] = 0
                    index -= 1
                    if index < 0:
                        index = max_pos_menu
                    self.menudict[menu_keys[index]] = 1
                    self.drawmenu()

                if chh == 258:  # down
                    self.menudict[menu_keys[index]] = 0
                    index += 1
                    if index > max_pos_menu:
                        index = 0
                    self.menudict[menu_keys[index]] = 1
                    self.drawmenu()

                if chh == 10:  # enter
                    break

        return [menu_keys[index], index]

    def start(self):
        self.universal.go(self.scr, self.maxX, self.maxY)
        return True

    def __del__(self):
        self.scr.clear()
        curses.endwin()
        pass

