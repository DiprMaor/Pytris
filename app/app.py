
import app.game
import fcntl
# import termios


class App:
    app_name = "Pytris"
    app_version = "0.1-a"
    app_date = "27.08.2022"
    app = "App init...\nGame a %s\nVersion %s %s" % (app_name, app_version, app_date)

    def __init__(self):
        self.game = app.game.Game()
        self.ttysizeX = 0
        self.ttysizeY = 0
        print(App.app)
        try:
            ttysize = fcntl.ioctl(0, 21523, '0000')
            self.ttysizeX = ttysize[0]  # X
            self.ttysizeY = ttysize[2]  # Y
        except OSError as err:
            print("Oops!! {0} ".format(err))
            exit(1)

    def onInit(self):
        return True

    def execute(self):
        select_menu = 0

        if not self.onInit():
            return False

        if not self.game.onInit():
            return False

        select_menu = self.game.menu()

        if select_menu[1] == 0:
            self.game.scr.addstr(1, 1, select_menu[0] + " " + str(select_menu[1]))

        elif select_menu[1] == 1:  # New Games
            # self.game.scr.addstr(1, 1, select_menu[0] + " " + str(select_menu[1]))
            self.game.start()

        elif select_menu[1] == 2:
            self.game.scr.addstr(1, 1, select_menu[0] + " " + str(select_menu[1]))

        elif select_menu[1] == 3:
            self.game.scr.addstr(1, 1, select_menu[0] + " " + str(select_menu[1]))

        else:
            print("Noname")
        self.game.scr.nodelay(False)
        self.game.scr.refresh()
        self.game.scr.getch()
        return True

    def __del__(self):
        pass

