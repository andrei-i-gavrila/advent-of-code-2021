import re

from aocd import submit, get_data

data = """target area: x=20..30, y=-10..-5"""


data = get_data(day=17)

def read_x_y():
    x1, x2, y1, y2 = map(int, re.findall(r"(-?\d+)", data))
    return (x1, x2), (y1, y2)


def in_bounds(v, vs):
    return vs[0] <= v <= vs[1]


def simulate(dx, dy):
    targetX, targetY = read_x_y()
    x, y = 0, 0

    while True:
        x += dx
        y += dy

        if in_bounds(x, targetX) and in_bounds(y, targetY):
            return True

        if x > targetX[1] or y < targetY[0]:
            return False

        dy -= 1
        if dx > 0:
            dx -= 1


def get_answer_a():
    xs, ys = read_x_y()
    speed = abs(ys[0])
    y = ys[0]

    while speed != 0:
        y += speed
        speed -= 1

    return y


def solve_part_a():
    submit(get_answer_a(), day=17, part='a')


def solve_part_b():
    xs, ys = read_x_y()
    maxY = abs(ys[0])
    success = []

    for x in range(0, xs[1] + 1):
        for y in range(ys[0], maxY + 1):
            if simulate(x, y):
                success.append((x, y))

    submit(len(success), day=17, part='b')

solve_part_a()
solve_part_b()
