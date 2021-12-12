import networkx as nx
import numpy as np
from aocd import submit, get_data
from aocd.transforms import lines

data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


data = get_data(day=11)


def get_matrix_and_graph():
    m = np.array([[int(i) for i in line] for line in lines(data)])
    g = nx.grid_graph(m.shape)
    g.add_edges_from(
        ((x, y), (x + 1, y + 1)) for x in range(9) for y in range(9)
    )
    g.add_edges_from(
        ((x + 1, y), (x, y + 1)) for x in range(9) for y in range(9)
    )
    return m, g


def run_step(m, g):
    m += np.ones(m.shape, dtype=np.int32)
    requires_pass = True

    flashes = set()
    while requires_pass:
        # print("pass")
        # print(m)

        requires_pass = False
        for node in g:
            if m[node] > 9 and node not in flashes:
                flashes.add(node)
                for neighbour in g[node]:
                    if neighbour not in flashes:
                        m[neighbour] += 1
                        if m[neighbour] == 10:
                            requires_pass = True
    # print(m)
    for flash in flashes:
        m[flash] = 0
    return len(flashes)


def solve_part_a():
    m, g = get_matrix_and_graph()
    total = 0
    # print(m)
    for i in range(100):
        total += run_step(m, g)
        # print(m)

    submit(total, day=11, part='a')

def solve_part_b():
    m, g = get_matrix_and_graph()
    step = 0
    while True:
        step += 1
        flashes = run_step(m, g)
        if flashes == 100:
            break
    print(step)
    submit(step, day=11, part='b')

solve_part_a()
solve_part_b()
