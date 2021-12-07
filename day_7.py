from aocd import submit, get_data

data = "16,1,2,0,4,2,7,1,2,14"


data = get_data(day=7)


def solve_part_a():
    crabs = sorted(list(map(int, data.split(","))))
    midpoint = crabs[len(crabs) // 2]

    submit(sum(abs(x - midpoint) for x in crabs), day=7, part='a')


def find_saddle(left, right, eval_f):
    midpoint = round((left + right) / 2)
    a = eval_f(midpoint - 1)
    b = eval_f(midpoint)
    c = eval_f(midpoint + 1)

    if a >= b >= c:
        return find_saddle(midpoint, right, eval_f)
    elif a >= b <= c:
        return b
    elif a <= b <= c:
        return find_saddle(left, midpoint, eval_f)

    print("Wtf")


def solve_part_b():
    crabs = sorted(list(map(int, data.split(","))))

    def eval(i):
        return sum((abs(x - i) * (abs(x - i) + 1)) // 2 for x in crabs)

    print(find_saddle(crabs[0], crabs[-1], eval))
    submit(find_saddle(crabs[0], crabs[-1], eval), day=7, part='b')


solve_part_a()
solve_part_b()
