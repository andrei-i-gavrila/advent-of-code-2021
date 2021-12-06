from functools import lru_cache, cache

import numpy
from aocd import submit, get_data
from aocd.transforms import lines

data = "3,4,3,1,2"
data = get_data(day=6)



@cache
def get_after_days(counter_now: int, days: int):
    if days == 0:
        return 1

    if counter_now == 0:
        return get_after_days(6, days-1) + get_after_days(8, days-1)

    return get_after_days(counter_now-1, days-1)

def solve_part_a():
    submit(sum(get_after_days(int(f), 80) for f in data.split(",")), day=6, part='a')

def solve_part_b():
    submit(sum(get_after_days(int(f), 256) for f in data.split(",")), day=6, part='b')




solve_part_a()
solve_part_b()
