import networkx as nx
from aocd import get_data, submit
from aocd.transforms import lines

data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


data = get_data(day=12)


def get_graph():
    g = nx.Graph()
    g.add_edges_from([tuple(line.split('-')) for line in lines(data)])
    return g


def paths(g, node, target, visited, path, visited_lower_twice):
    path.append(node)
    visited.add(node)
    if node == target:
        return [path]
    ps = []
    for n in g[node]:
        if n.islower():
            if n in visited:
                if not visited_lower_twice and n not in {'start', 'end'}:
                    ps.extend(paths(g, n, target, set(visited), list(path), True))
            else:
                ps.extend(paths(g, n, target, set(visited), list(path), visited_lower_twice))
        else:
            ps.extend(paths(g, n, target, set(visited), list(path), visited_lower_twice))
    return ps


def solve_part_a():
    g = get_graph()
    ps = paths(g, 'start', 'end', set(), [], True)

    answer = len(ps)

    submit(answer, day=12, part='a')


def solve_part_b():
    g = get_graph()
    ps = paths(g, 'start', 'end', set(), [], False)

    answer = len(ps)
    print(answer)
    submit(answer, day=12, part='b')


solve_part_a()
solve_part_b()
