import numpy as np
from aocd import submit, get_data

data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


data = get_data(day=13)


def get_points_and_folds():
    points, folds = data.split("\n\n")
    points = points.split("\n")
    points = [tuple(list(map(int, p.split(",")))) for p in points]

    folds = folds.split("\n")
    folds = [tuple([p.split(" ")[-1].split("=")[0], int(p.split(" ")[-1].split("=")[1])]) for p in folds]

    return points, folds


def do_fold(points, fold):
    axis, v = fold
    if axis == 'y':
        return [tuple([x, y if y < v else 2 * v - y]) for x, y in points]
    elif axis == 'x':
        return [tuple([x if x < v else 2 * v - x, y]) for x, y in points]


def solve_part_a():
    points, folds = get_points_and_folds()
    points = set(do_fold(points, folds[0]))
    answer = len(points)
    print(answer)
    submit(answer, day=13, part='a')


def solve_part_b():
    points, folds = get_points_and_folds()
    for fold in folds:
        points = set(do_fold(points, fold))
    mx = 0
    my = 0

    for x, y in points:
        mx = max(mx, x)
        my = max(my, y)

    m = np.zeros((my+1, mx+1), dtype=np.int32)
    for x, y in points:
        m[(y, x)] = 1
    for l in np.where(m==1, '#', ' '):
        print("".join(l))

    #  #   ## ###  #  # #### #  # ###   ##
    # #     # #  # # #  #    #  # #  # #  #
    ##      # ###  ##   ###  #  # ###  #
    # #     # #  # # #  #    #  # #  # # ##
    # #  #  # #  # # #  #    #  # #  # #  #
    #  #  ##  ###  #  # ####  ##  ###   ###
    # KJBKEUBG
    submit("KJBKEUBG", day=13, part='b')


# solve_part_a()
solve_part_b()
