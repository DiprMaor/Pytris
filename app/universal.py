
import curses
import entity.entity
import entity.glassful
import entity.figure
import time
import random


class Universal:
    instance = False

    def __init__(self):
        self.scr = curses.window
        self.wnd = curses.window
        self.wnd_score = curses.window
        self.maxX = 0
        self.maxY = 0
        self.glass_ful = entity.glassful.Glassful
        self.figures = []
        self.figures_check_rotate = []
        self.achieve = curses.window
        self.new_figure = False
        self.current_figure = [[], []]
        self.speed = 900000000
        self.scores = 0
        self.lines = 0
        self.level = 0

        print("Universal")

    def collision_in_matrix_left(self, matrix_transmitting, matrix_receiving, x=0, y=0):
        out = 0
        for i in matrix_transmitting.map_collision['left']:
             yy = i[0]
             xx = i[1]
             out += matrix_receiving.sprites[y + yy][x + xx]
        if out == 0:
            return False
        return True

    def collision_in_matrix_right(self, matrix_transmitting, matrix_receiving, x=0, y=0):
        out = 0
        for i in matrix_transmitting.map_collision['right']:
            yy = i[0]
            xx = i[1]
            out += matrix_receiving.sprites[y+yy][x+xx]
        if out == 0:
            return False
        return True

    def collision_in_matrix_down(self, matrix_transmitting, matrix_receiving, x=0, y=0):
        out = 0
        for i in matrix_transmitting.map_collision['down']:
            yy = i[0]
            xx = i[1]
            out += matrix_receiving.sprites[y+yy][x+xx]
        if out == 0:
            return False
        return True

    def merge_matrix(self, matrix_transmitting, matrix_receiving, x=0, y=0):
        for yy in range(0, len(matrix_transmitting.sprites)):
            for xx in range(0, len(matrix_transmitting.sprites[yy])):

                if matrix_transmitting.sprites[yy][xx] != 0:
                    matrix_receiving.sprites[y + yy][x + xx] = matrix_transmitting.sprites[yy][xx]

    def on_init(self):
        self.scr.clear()
        self.scr.refresh()
        self.wnd = curses.newwin(self.maxY-10, self.maxX-200, 1, 1)
        self.wnd.border()
        self.wnd.refresh()

        self.wnd_score = curses.newwin(self.maxY-10, self.maxX-220, 1, self.maxX-199)
        self.wnd_score.border()
        self.wnd_score.addstr(2, 2, "Score: " + str(self.scores))
        self.wnd_score.addstr(3, 2, "Lines: " + str(self.lines))
        self.wnd_score.addstr(4, 2, "Level: " + str(self.level))
        self.wnd_score.addstr(5, 2, "Speed: " + str(self.speed / 100000000))
        self.wnd_score.refresh()

        sprite_glass_ful = []
        layer = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        layer_last = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        for i in range(0, 40):
            sprite_glass_ful.append(layer[:])

        sprite_glass_ful.append(layer_last)

        self.glass_ful = entity.glassful.Glassful(5, 5, 20, 40)
        self.glass_ful.sprite(sprite_glass_ful)

        self.figures.append(entity.figure.Figure(30, 10, 4, 3))
        figure_l = [[0, 0, 0, 0],
                    [0, 8, 0, 0],
                    [0, 8, 0, 0],
                    [0, 8, 8, 0],
                    [0, 0, 0, 0]]
        self.figures[0].sprite(figure_l)

        self.figures.append(entity.figure.Figure(40, 10, 4, 3))
        figure_z = [[0, 0, 0, 0],
                    [0, 7, 0, 0],
                    [0, 7, 7, 0],
                    [0, 0, 7, 0],
                    [0, 0, 0, 0]]
        self.figures[1].sprite(figure_z)

        self.figures.append(entity.figure.Figure(50, 10, 2, 5))
        figure_i = [[0, 0, 0],
                    [0, 6, 0],
                    [0, 6, 0],
                    [0, 6, 0],
                    [0, 6, 0],
                    [0, 0, 0]]
        self.figures[2].sprite(figure_i)

        self.figures.append(entity.figure.Figure(60, 10, 5, 3))
        figure_t = [[0, 0, 0, 0, 0],
                    [0, 0, 5, 0, 0],
                    [0, 5, 5, 5, 0],
                    [0, 0, 0, 0, 0]]
        self.figures[3].sprite(figure_t)

        self.figures.append(entity.figure.Figure(30, 20, 5, 3))
        figure_c = [[0, 0, 0, 0],
                    [0, 4, 4, 0],
                    [0, 4, 4, 0],
                    [0, 0, 0, 0]]
        self.figures[4].sprite(figure_c)

        self.figures.append(entity.figure.Figure(40, 20, 4, 3))
        figure_lz = [[0, 0, 0, 0],
                     [0, 0, 3, 0],
                     [0, 3, 3, 0],
                     [0, 3, 0, 0],
                     [0, 0, 0, 0]]
        self.figures[5].sprite(figure_lz)

        self.figures.append(entity.figure.Figure(50, 20, 4, 3))
        figure_rl = [[0, 0, 0, 0],
                     [0, 0, 2, 0],
                     [0, 0, 2, 0],
                     [0, 2, 2, 0],
                     [0, 0, 0, 0]]
        self.figures[6].sprite(figure_rl)
        self.figures[6].render_sign = 2

    def go(self, scr=curses.window, maxx=0, maxy=0):
        self.scr = scr
        self.maxX = maxx
        self.maxY = maxy
        self.on_init()

        self.glass_ful.render(self.wnd)
        #---------------------------------------->>>>>>
        # self.figures[0].render(self.wnd)
        # self.figures[1].render(self.wnd)
        # self.figures[2].render(self.wnd)
        # self.figures[3].render(self.wnd)
        # self.figures[4].render(self.wnd)
        # self.figures[5].render(self.wnd)
        # self.figures[6].render(self.wnd)

        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        self.scr.nodelay(True)
        self.scr.keypad(True)

        def kbhit(screen):
            ch = screen.getch()
            if ch == -1:
                return False
            else:
                curses.ungetch(ch)
                return ch

        t1 = time.time_ns()
        y = 0
        x = 2
        # self.current_figure = [inmat[:] for inmat in self.figures[0].sprites]
        sf = random.randint(0, len(self.figures) - 1)
        self.current_figure = self.figures[sf]
        # self.current_figure = self.figures[4]
        self.figures_check_rotate = entity.figure.Figure(1, 1, 1, 1)

        while (chh := kbhit(scr)) != 27:
            modify = 0
            if self.new_figure:
                self.new_figure = False
                sf = random.randint(0, len(self.figures) - 1)
                self.current_figure = self.figures[sf]
                y = 0
                x = 2

            if chh:
                curses.flushinp()  # Must be Clear buffer

            if chh == 259:

                self.glass_ful.restore(self.current_figure.isprites, x, y)
                rect = (len(self.current_figure.sprites), len(self.current_figure.sprites[0]))
                self.current_figure.sprite(self.current_figure.rotate())

                if not self.glass_ful.intersect(self.current_figure.isprites, x, y):
                    self.glass_ful.render_rect(self.wnd, rect, x, y)
                    self.merge_matrix(self.current_figure, self.glass_ful, x, y)
                else:
                    self.current_figure.sprite(self.current_figure.rotate_right_clock())
                    self.glass_ful.draw(self.current_figure.isprites, x, y)

            if chh == 260:
                if not self.collision_in_matrix_left(self.current_figure, self.glass_ful, x, y):
                    self.glass_ful.restore(self.current_figure.isprites, x, y)
                    x -= 1
                    self.merge_matrix(self.current_figure, self.glass_ful, x, y)

            if chh == 261:
                if not self.collision_in_matrix_right(self.current_figure, self.glass_ful, x, y):
                    self.glass_ful.restore(self.current_figure.isprites, x, y)
                    x += 1
                    self.merge_matrix(self.current_figure, self.glass_ful, x, y)

            if chh == curses.KEY_DOWN:
                modify = 899999900

            t2 = time.time_ns()

            if t2 - t1 > (self.speed - modify):
                t1 = t2

                if not self.collision_in_matrix_down(self.current_figure, self.glass_ful, x, y):
                    self.glass_ful.restore(self.current_figure.isprites, x, y)
                    y += 1
                    self.merge_matrix(self.current_figure, self.glass_ful, x, y)

                if self.collision_in_matrix_down(self.current_figure, self.glass_ful, x, y):
                    self.new_figure = True
                    if self.glass_ful.chk_full_str():
                        self.glass_ful.save_matrix_pos()
                        self.glass_ful.collapse_matrix()
                        self.glass_ful.render(self.wnd)
                        self.lines += len(self.glass_ful.status_string['full_pos'])
                        self.wnd_score.addstr(2, 2, "Score: " + str(self.scores))
                        self.wnd_score.addstr(3, 2, "Lines: " + str(self.lines))
                        self.wnd_score.addstr(4, 2, "Level: " + str(self.level))
                        self.wnd_score.addstr(5, 2, "Speed: " + str(self.speed / 100000000))
                        self.wnd_score.refresh()

                # self.wnd.addstr(30, 40, str(self.glass_ful.status_string))

            rect = (len(self.current_figure.sprites), len(self.current_figure.sprites[0]))
            self.glass_ful.render_rect(self.wnd, rect, x, y)

