from collections import deque

from aocd import submit, get_data
from aocd.transforms import lines

data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

data = get_data(day=10)

pairs = {
    '}': '{',
    '>': '<',
    ')': '(',
    ']': '['
}

starts = {'(', '<', '[', '{'}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
    None: 0
}


def get_first_illegal(line):
    stack = deque()

    for char in line:
        if char in starts:
            stack.append(char)
        if char in pairs:
            pair = stack.pop()
            if pair != pairs[char]:
                return char


def is_illegal(line):
    return get_first_illegal(line) is not None


def get_completion_score(line):
    stack = deque()

    for char in line:
        if char in starts:
            stack.append(char)
        if char in pairs:
            stack.pop()

    score = 0
    while len(stack):
        last = stack.pop()
        score = score * 5 + scores[last]

    return score


def get_score_of_completion(completion):
    return sum(scores[char] for char in completion)


def solve_part_a():
    answer = sum(scores[get_first_illegal(line)] for line in lines(data))
    print(answer)
    submit(answer, day=10, part='a')


def solve_part_b():
    completions = sorted([get_completion_score(line) for line in lines(data) if not is_illegal(line)])
    answer = completions[len(completions) // 2]
    print(answer)
    submit(answer, day=10, part='b')


# solve_part_a()
solve_part_b()
