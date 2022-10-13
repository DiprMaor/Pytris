

import entity.entity
import curses


class Figure(entity.entity.Entity):

    def __init__(self, x, y, width, height):
        entity.entity.Entity.__init__(self, x, y, width, height)
        self.color = 151
        curses.init_color(251, 200, 1000, 200)
        curses.init_pair(151, 251, curses.COLOR_BLACK)



