
import curses


class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = []
        self.isprites = []
        self.map_collision = {'left': [], 'right': [],
                               'up': [], 'down': [],
                               'left_up': [], 'left_dwn': [],
                               'right_up': [], 'right_dwn': []}
        self.color1 = 10
        self.color2 = 11
        self.color3 = 12
        self.color4 = 13
        self.color5 = 14
        self.color6 = 15
        self.color7 = 16
        self.color8 = 17
        self.render_sign = 1
        curses.start_color()
        curses.init_color(201, 700, 700, 700)
        curses.init_pair(111, 201, curses.COLOR_BLACK)

# TODO функция формирующая карту коллизий спрайта по направлением (векторам)
    def sprite(self, sprite):
        self.sprites = sprite

        for y in range(0, len(sprite)):
            for x in range(0, len(sprite[y])):
                if self.sprites[y][x] > 0:
                    self.isprites.append((y, x))

        for i in self.isprites:
            y = i[0]
            x = i[1]
            try:
                if self.sprites[y + 1][x] == 0:  # down
                    self.map_collision['down'].append((y + 1, x))
            except IndexError:
                pass
            try:
                if self.sprites[y - 1][x] == 0:  # up
                    self.map_collision['up'].append((y - 1, x))
            except IndexError:
                pass
            try:
                if self.sprites[y][x + 1] == 0:  # right
                    self.map_collision['right'].append((y, x + 1))
            except IndexError:
                pass
            try:
                if self.sprites[y][x - 1] == 0:  # left
                    self.map_collision['left'].append((y, x - 1))
            except IndexError:
                pass
            try:
                if self.sprites[y - 1][x - 1] == 0:  # left & up
                    self.map_collision['left_up'].append((y - 1, x - 1))
            except IndexError:
                pass
            try:
                if self.sprites[y + 1][x + 1] == 0:
                    self.map_collision['right_dwn'].append((y + 1, x + 1))
            except IndexError:
                pass
            try:
                if self.sprites[y + 1][x - 1] == 0:
                    self.map_collision['left_dwn'].append((y + 1, x - 1))
            except IndexError:
                pass
            try:
                if self.sprites[y - 1][x + 1] == 0:
                    self.map_collision['right_up'].append((y - 1, x + 1))
            except IndexError:
                pass

    def render_rect(self, wnd=curses.window, rectangle=(), x=0, y=0):
        for yy in range(0, rectangle[0]):
            for xx in range(0, rectangle[1]):

                if self.sprites[y + yy][x + xx] == 0:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "░", curses.color_pair(111))

                if self.sprites[y + yy][x + xx] == self.render_sign:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color1))

                if self.sprites[y + yy][x + xx] == 2:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color2))

                if self.sprites[y + yy][x + xx] == 3:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color3))

                if self.sprites[y + yy][x + xx] == 4:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color4))

                if self.sprites[y + yy][x + xx] == 5:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color5))

                if self.sprites[y + yy][x + xx] == 6:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color6))

                if self.sprites[y + yy][x + xx] == 7:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color7))

                if self.sprites[y + yy][x + xx] == 8:
                    wnd.addch(self.y + yy + y, self.x + xx + x, "█", curses.color_pair(self.color8))

        wnd.refresh()

    def render(self, wnd=curses.window):
        for i in range(0, len(self.sprites)):
             for x in range(0, len(self.sprites[0])):

                if self.sprites[i][x] == 0:
                    wnd.addch(self.y + i, self.x + x, "░", curses.color_pair(111))

                if self.sprites[i][x] == self.render_sign:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color1))

                if self.sprites[i][x] == 2:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color2))

                if self.sprites[i][x] == 3:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color3))

                if self.sprites[i][x] == 4:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color4))

                if self.sprites[i][x] == 5:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color5))

                if self.sprites[i][x] == 6:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color6))

                if self.sprites[i][x] == 7:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color7))

                if self.sprites[i][x] == 8:
                    wnd.addch(self.y + i, self.x + x, "█", curses.color_pair(self.color8))

        wnd.refresh()

    def restore(self, isp, x=0, y=0):
        for i in isp:
            self.sprites[y + i[0]][x + i[1]] = 0

# TODO нуж
    def draw(self, isp, x=0, y=0):
        for i in isp:
            self.sprites[y + i[0]][x + i[1]] = self.render_sign

# TODO universal 185

    def rotate_right_clock(self):
        out = []
        tmp = []
        cm = [in_mat[:] for in_mat in self.sprites]

        for yyy in range(0, len(cm)):
            sss = cm[::-1][yyy]
            tmp.append(sss)

        for xi in range(0, len(tmp[0])):
            sss = []
            for yi in range(0, len(tmp)):
                sss.append(tmp[yi][xi])
            out.append(sss)

        self.isprites = []
        self.map_collision = {'left': [], 'right': [], 'up': [], 'down': [], 'left_up': [], 'left_dwn': [],
                              'right_up': [], 'right_dwn': []}

        return out

    def rotate(self):
        out = []
        tmp = []
        cm = [in_mat[:] for in_mat in self.sprites]

        for yyy in range(0, len(cm)):
            sss = cm[yyy][::-1]
            tmp.append(sss)

        for xi in range(0, len(tmp[0])):
            sss = []
            for yi in range(0, len(tmp)):
                sss.append(tmp[yi][xi])
            out.append(sss)

        self.isprites = []
        self.map_collision = {'left': [], 'right': [], 'up': [], 'down': [], 'left_up': [], 'left_dwn': [],
                              'right_up': [], 'right_dwn': []}

        return out

    def get_copy_sprites(self):
        out = [in_mat[:] for in_mat in self.sprites]
        return out

    def intersect(self,  rcv_isprites=[], x=0, y=0):
        for i in rcv_isprites:
            if self.sprites[y + i[0]][x + i[1]] > 0:
                return True
        return False




