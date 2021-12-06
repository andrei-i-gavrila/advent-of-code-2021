import numpy
from aocd import submit, get_data
from aocd.transforms import lines

data = lines("""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""")
size = 10

data = lines(get_data(day=5))
size = 1000

def parse_tuples(line):
    a, b = line.split(" -> ")
    return tuple(map(int, a.split(","))), tuple(map(int, b.split(",")))


def is_line(pair_o_tuples):
    return pair_o_tuples[0][0] == pair_o_tuples[1][0] or pair_o_tuples[0][1] == pair_o_tuples[1][1]


def diagonal_to_lines(diagonal):
    x1 = diagonal[0][1]
    x2 = diagonal[1][1]
    y1 = diagonal[0][0]
    y2 = diagonal[1][0]
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1
    lines = [((y1,x1), (y1,x1))]
    cx = x1
    cy = y1
    while cx != x2:
        cx += dx
        cy += dy
        lines.append(((cy,cx), (cy,cx)))

    return lines

def solve_part_a():
    lines = [parse_tuples(line) for line in data if is_line(parse_tuples(line))]
    print(lines)
    board = numpy.zeros((size, size))
    for line in lines:
        x1 = line[0][1]
        x2 = line[1][1]
        y1 = line[0][0]
        y2 = line[1][0]
        board[min(x1, x2):max(x1, x2) + 1, min(y1, y2):max(y1, y2) + 1] += 1
    submit(numpy.where(board > 1, 1, 0).sum(), day=5, part='a')


def solve_part_b():
    lines = []
    for line in data:
        line = parse_tuples(line)
        if is_line(line):
            lines.append(line)
        else:
            lines.extend(diagonal_to_lines(line))

    print(lines)
    for line in lines:
        print(line)
    board = numpy.zeros((size, size))
    for line in lines:
        x1 = line[0][1]
        x2 = line[1][1]
        y1 = line[0][0]
        y2 = line[1][0]
        board[min(x1, x2):max(x1, x2) + 1, min(y1, y2):max(y1, y2) + 1] += 1
    # print(board.astype(numpy.int32))
    # print(numpy.where(board > 1, 1, 0).sum())
    submit(numpy.where(board > 1, 1, 0).sum(), day=5, part='b')


# solve_part_a()
solve_part_b()
