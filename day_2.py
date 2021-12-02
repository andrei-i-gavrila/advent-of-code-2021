from aocd import get_data, submit
from aocd.transforms import lines

data = lines(get_data(day=2))


def solve_part_a():
    horizontal = 0
    depth = 0
    for line in data:
        command, argument = line.split(" ")
        if command == "forward":
            horizontal += int(argument)
        elif command == "up":
            depth -= int(argument)
        elif command == "down":
            depth += int(argument)
    submit(horizontal * depth, day=2, part='a')


def solve_part_b():
    horizontal = 0
    depth = 0
    aim = 0
    for line in data:
        command, argument = line.split(" ")
        if command == "forward":
            horizontal += int(argument)
            depth += aim * int(argument)
        elif command == "up":
            aim -= int(argument)
        elif command == "down":
            aim += int(argument)
    submit(horizontal * depth, day=2, part='b')


solve_part_a()
solve_part_b()
