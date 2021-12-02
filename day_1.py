from aocd import get_data, submit
from aocd.transforms import numbers

data = numbers(get_data(day=1))


def solve_part_a():
    submit(sum(1 if data[i] > data[i - 1] else 0 for i in range(1, len(data))), part='a', day=1)


def solve_part_b():
    windowed = [sum(data[j] for j in range(i, i + 3)) for i in range(0, len(data) - 2)]
    submit(sum(1 if windowed[i] > windowed[i - 1] else 0 for i in range(1, len(windowed))), part='b', day=1)


solve_part_a()
solve_part_b()
