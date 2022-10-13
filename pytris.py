#!/usr/bin/env python


import app.app
import os
from time import sleep

if __name__ == '__main__':
    app = app.app.App()

    if app.ttysizeX < 40 or app.ttysizeY < 100:
        print("X = %s Y = %s" % (app.ttysizeX, app.ttysizeY))
        try:
            out = os.system('wmctrl -r :ACTIVE: -e 0,40,50,1010,810 2>/dev/null')
            sleep(0.1)
            if out != 0:
                raise OSError("Wrong command", 127)
        except OSError as err:
            print(err)
            print('You will install wmctrl or resize konsole terminal tty or pty hand mode.')
            print('Sorry')
            exit(1)

    app.execute()

