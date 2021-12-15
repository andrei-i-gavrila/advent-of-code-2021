import networkx as nx
import numpy as np
from aocd import submit, get_data

data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


data = get_data(day=15)


def get_matrix():
    return np.array([[int(i) for i in line] for line in data.split("\n")])


def get_graph(m):
    g = nx.DiGraph()
    for (x, y), w in np.ndenumerate(m):
        g.add_edge((x - 1, y), (x, y), weight=w)
        g.add_edge((x, y - 1), (x, y), weight=w)
        g.add_edge((x, y + 1), (x, y), weight=w)
        g.add_edge((x + 1, y), (x, y), weight=w)

    return g


def solve_part_a():
    m = get_matrix()
    g = get_graph(m)
    M, N = m.shape
    path = nx.dijkstra_path(g, (0, 0), (N - 1, M - 1))

    weight = nx.path_weight(g, path, 'weight')
    print(weight)

    submit(weight, day=15, part='a')


def extend_matrix(m):
    M, N = m.shape

    large_m = np.resize(m, (5 * M, 5 * N))
    for (x, y), w in np.ndenumerate(large_m):
        newVal = (m[(x % M, y % N)] + x // M + y // N)
        large_m[(x, y)] = newVal % 10 + newVal // 10

    return large_m


def solve_part_b():
    m = get_matrix()
    m = extend_matrix(m)
    M, N = m.shape
    g = get_graph(m)
    weight = nx.dijkstra_path_length(g, (0, 0), (M - 1, N - 1))
    submit(weight, day=15, part='b')

solve_part_a()
solve_part_b()
