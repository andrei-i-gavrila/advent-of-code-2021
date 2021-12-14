from collections import defaultdict
from functools import cache

from aocd import submit, get_data

data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


data = get_data(day=14)


def get_input():
    seq, transforms = data.split("\n\n")
    transforms = map(lambda l: l.split(" -> "), transforms.split("\n"))
    transforms = {k: v for k, v in transforms}
    return seq, transforms


def do_step(sequence, transforms):
    new_sequence = []

    for a, b in zip(sequence[:-1], sequence[1:]):
        new_sequence.append(a)
        if f"{a}{b}" in transforms:
            new_sequence.append(transforms[f"{a}{b}"])

    new_sequence.append(sequence[-1])

    return "".join(new_sequence)


def get_frequencies(seq):
    freq = defaultdict(int)
    for s in seq:
        freq[s] += 1
    return sorted(freq.values())


def solve_part_a():
    seq, transforms = get_input()
    for i in range(10):
        seq = do_step(seq, transforms)
    freq = get_frequencies(seq)
    answer = freq[-1] - freq[0]
    print(answer)
    submit(answer, day=14, part='a')


def merge_freq(*fs):
    r = {}
    for f in fs:
        for k, v in f.items():
            if k in r:
                r[k] += v
            else:
                r[k] = v
    return r


def solve_part_b():
    seq, transforms = get_input()

    @cache
    def get_after_steps(a, b, steps):
        if steps == 0:
            return merge_freq({a: 1})

        ab = f"{a}{b}"

        if steps == 1:
            if ab in transforms:
                return merge_freq({a: 1}, {transforms[ab]: 1})
            return merge_freq({a: 1})

        if ab in transforms:
            return merge_freq(
                get_after_steps(a, transforms[ab], steps - 1),
                get_after_steps(transforms[ab], b, steps - 1)
            )
        else:
            return merge_freq({a: 1})

    freq = {seq[-1]: 1}
    for a, b in zip(seq[:-1], seq[1:]):
        freq = merge_freq(freq, get_after_steps(a, b, 40))

    freq = sorted(freq.items(), key=lambda l: l[1])
    answer = freq[-1][1] - freq[0][1]
    print(answer)
    submit(answer, day=14, part='b')


solve_part_a()
solve_part_b()
