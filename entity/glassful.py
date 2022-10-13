

import entity.entity
import curses


class Glassful(entity.entity.Entity):

    def __init__(self, x, y, width, height):
        entity.entity.Entity.__init__(self, x, y, width, height)
        self.status_string = {"full_pos": [], "degr_pos": []}
        self.save_part = []
        # self.color1 = 10
        # self.color2 = 11
        # self.color3 = 12
        curses.init_color(10, 1000, 0, 0)
        curses.init_color(11, 0, 1000, 0)
        curses.init_color(12, 0, 0, 1000)
        curses.init_color(13, 1000, 1000, 1000)
        curses.init_color(14, 1000, 1000, 0)
        curses.init_color(15, 0, 1000, 1000)
        curses.init_color(16, 1000, 0, 1000)
        curses.init_color(17, 500, 500, 1000)
        curses.init_color(0, 0, 0, 0)

        curses.init_pair(10, 10, curses.COLOR_BLACK)  # 1
        curses.init_pair(11, 11, curses.COLOR_BLACK)  # 2
        curses.init_pair(12, 12, curses.COLOR_BLACK)  # 3
        curses.init_pair(13, 13, curses.COLOR_BLACK)  # 4
        curses.init_pair(14, 14, curses.COLOR_BLACK)  # 5
        curses.init_pair(15, 15, curses.COLOR_BLACK)  # 6
        curses.init_pair(16, 16, curses.COLOR_BLACK)  # 7
        curses.init_pair(17, 17, curses.COLOR_BLACK)  # 8

    def getsprite(self):
        return self.sprites

    def chk_full_str(self):
        self.status_string['full_pos'] = []
        self.status_string['degr_pos'] = []
        flag_degr = False
        st = False
        i = 0
        for str_m in self.sprites[:-1]:
            summa = 0
            for elm in str_m:
                summa = summa + elm
                if elm == 0:
                    flag_degr = True
            if summa == 2:
                i += 1
                continue
            if flag_degr:
                self.status_string['degr_pos'].append(i)
            else:
                st = True
                self.status_string['full_pos'].append(i)
            i += 1
            flag_degr = False
        return st

    def clear_matrix_pos(self):
        for i in self.status_string['full_pos']:
            self.sprites[i] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1][:]

    def save_matrix_pos(self):
        self.save_part = []
        for i in self.status_string['degr_pos']:
            self.save_part.append(self.sprites[i][:])

    def collapse_matrix(self):
        max_pos = len(self.sprites) - 2
        for i in self.status_string['degr_pos']:
            self.sprites[i] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1][:]
        for i in self.status_string['full_pos']:
            self.sprites[i] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1][:]
        for i in reversed(range(len(self.save_part))):
            self.sprites[max_pos] = self.save_part[i][:]
            max_pos -= 1

    def remove_string(self, string=[]):
        self.sprites.pop(-2)
        self.sprites.insert(0, string)
