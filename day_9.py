import networkx as nx
import numpy as np
from aocd import submit, get_data
from aocd.transforms import lines

data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = get_data(day=9)


def get_neighbours(m, p):
    return [m[(p[0] - 1, p[1])], m[(p[0] + 1, p[1])], m[(p[0], p[1] - 1)], m[(p[0], p[1] + 1)]]


def get_peaks(m):
    peaks = []
    for x in range(1, len(m) - 1):
        for y in range(1, len(m[0]) - 1):
            if all(m[(x, y)] < n for n in get_neighbours(m, (x, y))):
                peaks.append(m[(x, y)])

    return peaks


def solve_part_a():
    m = np.pad(np.array([[int(l) for l in line] for line in lines(data)]), 1, constant_values=2 ** 31)
    answer = sum(1 + p for p in get_peaks(m))
    submit(answer, day=9, part='a')


def solve_part_b():
    m = np.array([[int(l) for l in line] for line in lines(data)])
    g = nx.grid_graph(m.shape, periodic=False)
    for (x, y) in np.argwhere(m == 9):
        g.remove_node((y, x))
    components = list(nx.algorithms.connected_components(g))
    answer = np.prod(sorted(map(lambda c: len(c), components), reverse=True)[:3])
    print(answer)
    submit(answer, day=9, part='bK')


solve_part_a()
solve_part_b()
