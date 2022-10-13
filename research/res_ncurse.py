

import curses

figure_t = [[0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0],
            [0, 5, 5, 5, 0],
            [0, 0, 0, 0, 0]]

status_string = {"full_pos": [], "degr_pos": []}

for str_m in figure_t[:-1]:
    print("+")
    for elm in str_m:
        if elm == 0:
            continue
        print(elm, end="")
    print("")

status_string['full_pos'] = []
print(">>>" + str(len(status_string['full_pos'])))
status_string['full_pos'].append(0)
print(">>>" + str(len(status_string['full_pos'])))



