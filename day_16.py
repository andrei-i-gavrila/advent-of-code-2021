import numpy as np
from aocd import get_data, submit

data = """D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780"""

data = """C200B40A82
04005AC33890
880086C3E88112
CE00C43D881120
D8005AC2A8F0
F600BC2D8F
9C005AC2F8F0
9C0141080250320F1802104A08"""
data = get_data(day=16)


trans = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def to_bits(hexa):
    return "".join(trans[a] for a in hexa)


def to_int(bits):
    return int(bits, 2)


def get_version(bits):
    return to_int(bits[:3])


def get_type(bits):
    return to_int(bits[3:6])


def get_type_length(bits):
    return to_int(bits[6])


def get_subpacket_length(bits):
    return to_int(bits[7:22])


def get_subpacket_count(bits):
    return to_int(bits[7:18])


def get_nth_literal(bits, n):
    return to_int(bits[6 + n * 5: 6 + (n + 1) * 5])


def get_subpackets(bits):
    type = get_type(bits)
    version = get_version(bits)
    if type == 4:
        literals = []
        while True:
            literal = get_nth_literal(bits, len(literals))
            if literal < 16:
                literals.append(literal)
                break
            else:
                literals.append(literal - 16)
        return version, bits[6 + (len(literals)) * 5:], literals
    else:
        length_id = get_type_length(bits)
        if length_id == 0:
            current = bits[22:]
            used_length = 0
            length = get_subpacket_length(bits)
            results = []
            while True:
                sub_version, remaining, result = get_subpackets(current)
                print(result)

                results.extend(result)
                used_length += len(current) - len(remaining)
                current = remaining
                version += sub_version
                if used_length == length:
                    break
        else:
            current = bits[18:]
            count = get_subpacket_count(bits)
            results = []

            for i in range(count):
                sub_version, remaining, result = get_subpackets(current)
                print(result)
                results.extend(result)
                version += sub_version
                current = remaining
        if type == 0:
            return version, current, [np.sum(results)]
        elif type == 1:
            return version, current, [np.prod(results)]
        elif type == 2:
            return version, current, [min(results)]
        elif type == 3:
            return version, current, [max(results)]
        elif type == 5:
            return version, current, [1 if results[0] > results[1] else 0]
        elif type == 6:
            return version, current, [1 if results[0] < results[1] else 0]
        elif type == 7:
            return version, current, [1 if results[0] == results[1] else 0]

def solve_part_a():
    total = 0
    for l in data.split("\n"):
        print(l)
        total += get_subpackets(to_bits(l))[0]
    print(total)
    submit(total, day=16, part="a")



def solve_part_b():
    for l in data.split("\n"):
        print(l)
        answer = get_subpackets(to_bits(l))[2]
        print(answer)
    # print(total)
    # submit(total, day=16, part="a")


# solve_part_a()
solve_part_b()
