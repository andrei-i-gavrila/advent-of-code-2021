import re

import numpy
import numpy.typing
from aocd import get_data, submit

data = get_data(day=4)
# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# """


def parse_board(board_data):
    lines = board_data.split("\n")
    return numpy.array(list(map(lambda line: list(map(int, re.split(r"\s+", line.strip()))), lines)))


def is_board_complete(board: numpy.typing.NDArray):
    return board.any(axis=1).all() is None or board.any(axis=0).all() is None


def process_number(board: numpy.typing.NDArray, number: int):
    return numpy.where(board == number, None, board)


def solve_part_a():
    parts = list(map(str.strip, data.split("\n\n")))
    numbers = [int(i) for i in parts[0].split(",")]
    boards = [parse_board(board) for board in parts[1:]]

    win, number_win = get_winning_board(boards, numbers)

    submit(numpy.where(win == None, 0, win).sum() * number_win, day=4, part='a')


def get_winning_board(boards, numbers):
    for number in numbers:
        boards = [process_number(board, number) for board in boards]
        for b in boards:
            if is_board_complete(b):
                return b, number


def get_last_winning_board(boards, numbers):
    active_boards = boards
    for number in numbers:
        processed_boards = [process_number(board, number) for board in active_boards]
        active_boards = [board for board in processed_boards if not is_board_complete(board)]

        if len(processed_boards) == 1 and len(active_boards) == 0:
            return processed_boards[0], number

def solve_part_b():
    parts = list(map(str.strip, data.split("\n\n")))
    numbers = [int(i) for i in parts[0].split(",")]
    boards = [parse_board(board) for board in parts[1:]]

    loss, number_win = get_last_winning_board(boards, numbers)

    answer = numpy.where(loss == None, 0, loss).sum() * number_win
    print(answer)
    submit(answer, day=4, part='b')


# solve_part_a()
solve_part_b()
