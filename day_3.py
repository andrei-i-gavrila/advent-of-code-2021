from aocd import get_data, submit
from aocd.transforms import lines

data = lines(get_data(day=3))
# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".split("\n")


def solve_part_a():
    frequencies = [[0, 0] for position in data[0]]

    for line in data:
        for position, bit in enumerate(line):
            frequencies[position][int(bit)] += 1

    gamma = "".join("0" if position[0] > position[1] else "1" for position in frequencies)
    epsilon = "".join("0" if position[0] < position[1] else "1" for position in frequencies)

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    print(gamma, epsilon)
    submit(epsilon * gamma, day=3, part='a')


def solve_part_b():
    def most_common(frequencies):
        return ["0" if position[0] > position[1] else "1" for position in frequencies]

    def least_common(frequencies):
        return ["0" if position[0] <= position[1] else "1" for position in frequencies]

    o2 = int(filter_out(most_common), base=2)
    co2 = int(filter_out(least_common), base=2)
    submit(o2 * co2, day=3, part='b')


def compute_frequencies(values):
    frequencies = [[0, 0] for position in values[0]]
    for value in values:
        for position, bit in enumerate(value):
            frequencies[position][int(bit)] += 1
    return frequencies


def filter_out(criteria_function):
    values = data
    position = 0
    while len(values) > 1:
        # print(values)
        criteria = criteria_function(compute_frequencies(values))
        values = list(filter(lambda v: v[position] == criteria[position], values))
        position += 1
    return values[0]


# solve_part_a()
solve_part_b()
