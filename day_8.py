from collections import defaultdict

from aocd import submit, get_data
from aocd.transforms import lines

data = lines("""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""")
data = lines("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")


data = lines(get_data(day=8))


def solve_part_a():
    outputs = []
    for line in data:
        outputs.extend(line.split(" | ")[1].split(" "))

    answer = sum(1 for out in outputs if len(out) in {2, 4, 3, 7})

    print(answer)
    # submit(answer, day=8, part="a")


def get_mappings(line):
    digits = line.split(" | ")[0].split(" ")

    frequency = defaultdict(int)

    for digit in digits:
        for letter in digit:
            frequency[letter] += 1

    digits = [set(digit) for digit in digits]
    m = {}
    m[1] = next(digit for digit in digits if len(digit) == 2)
    m[4] = next(digit for digit in digits if len(digit) == 4)
    m[7] = next(digit for digit in digits if len(digit) == 3)
    m[8] = next(digit for digit in digits if len(digit) == 7)
    m['a'] = m[7] - m[4]
    m['bd'] = m[4] - m[7]
    m['eg'] = m[8] - m[4] - m[7]
    m['b'] = set(next(letter for letter in frequency if frequency[letter] == 6))
    m['e'] = set(next(letter for letter in frequency if frequency[letter] == 4))
    m['f'] = set(next(letter for letter in frequency if frequency[letter] == 9))
    m['d'] = m['bd'] - m['b']
    m['g'] = m['eg'] - m['e']
    m['c'] = m[1] - m['f']

    m[0] = m[8] - m['d']
    m[2] = m[8] - m['b'] - m['f']
    m[3] = m[8] - m['b'] - m['e']
    m[5] = m[8] - m['c'] - m['e']
    m[6] = m[8] - m['c']
    m[9] = m[8] - m['e']

    return m


def reverse_mappings(mappings):
    return {"".join(sorted(value)): key for key, value in mappings.items()}

def get_output(line):
    translations = reverse_mappings(get_mappings(line))
    outputs = line.split(" | ")[1].split(" ")
    return int("".join([str(translations["".join(sorted(output))]) for output in outputs]))


def solve_part_b():
    answer = sum(get_output(line) for line in data)
    submit(answer, day=8, part="b")


solve_part_a()
solve_part_b()
