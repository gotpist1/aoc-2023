import re
from itertools import groupby
from os import environ


class Symbol:
    def __init__(self, value, idx, row, line_length):
        self.value = value
        self.idx = idx
        self.row = row
        self.line_length = line_length


class Number:
    def __init__(self, value, start_idx, end_idx, row, line_length):
        self.value = value
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.row = row
        self.line_length = line_length
        self.adjacent_key = None

    def is_adjacent(self, symbol_index_map):
        key = str(self.row) + "-" + str(self.start_idx)
        left_key = str(self.row) + "-" + str(self.start_idx - 1)
        right_key = str(self.row) + "-" + str(self.end_idx + 1)
        down_key = str(self.row + 1) + "-" + str(self.start_idx)
        down_key_end = str(self.row + 1) + "-" + str(self.end_idx)
        down_key_middle = str(self.row + 1) + "-" + str(self.start_idx + 1)
        down_key_left = str(self.row + 1) + "-" + str(self.start_idx - 1)
        down_key_right = str(self.row + 1) + "-" + str(self.end_idx + 1)
        up_key = str(self.row - 1) + "-" + str(self.start_idx)
        up_key_end = str(self.row - 1) + "-" + str(self.end_idx)
        up_key_middle = str(self.row - 1) + "-" + str(self.start_idx + 1)
        up_key_left = str(self.row - 1) + "-" + str(self.start_idx - 1)
        up_key_right = str(self.row - 1) + "-" + str(self.end_idx + 1)
        if key in symbol_index_map.keys():
            self.adjacent_key = key
            return True
        elif left_key in symbol_index_map.keys():
            self.adjacent_key = left_key
            return True
        elif right_key in symbol_index_map.keys():
            self.adjacent_key = right_key
            return True
        elif down_key in symbol_index_map.keys():
            self.adjacent_key = down_key
            return True
        elif down_key_end in symbol_index_map.keys():
            self.adjacent_key = down_key_end
            return True
        elif down_key_left in symbol_index_map.keys():
            self.adjacent_key = down_key_left
            return True
        elif down_key_right in symbol_index_map.keys():
            self.adjacent_key = down_key_right
            return True
        elif down_key_middle in symbol_index_map.keys():
            self.adjacent_key = down_key_middle
            return True
        elif up_key in symbol_index_map.keys():
            self.adjacent_key = up_key
            return True
        elif up_key_end in symbol_index_map.keys():
            self.adjacent_key = up_key_end
            return True
        elif up_key_left in symbol_index_map.keys():
            self.adjacent_key = up_key_left
            return True
        elif up_key_right in symbol_index_map.keys():
            self.adjacent_key = up_key_right
            return True
        elif up_key_middle in symbol_index_map.keys():
            self.adjacent_key = up_key_middle
            return True
        else:
            return False


def get_symbol_index_map(scrubbed):
    symbol_index_map = {}
    r1 = re.compile(r'[^.\d+]$')
    r2 = re.compile(r'[a-zA-Z_#@:;\\/\\\\=!^() +-]+')
    for row_idx, line in enumerate(scrubbed):
        for idx, char in enumerate(line):
            if r1.match(char) or r2.match(char):
                symbol_index_map[str(row_idx) + "-" + str(idx)] = Symbol(char, idx, row_idx, len(line))
    return symbol_index_map


def getNumber(startIdx, line, row):
    curr_idx = 0
    for idx in range(startIdx, len(line)):
        curr_idx = idx
        if not line[idx].isdigit() or idx == len(line):
            return Number(line[startIdx:idx], startIdx, idx - 1, row, len(line))
    return Number(line[startIdx:curr_idx + 1], startIdx, curr_idx - 1, row, len(line))


def get_valid_numbers(scrubbed):
    numbers = []
    for row_idx, line in enumerate(scrubbed):
        number = None
        for idx, char in enumerate(line):
            if char.isdigit() and number is None or char.isdigit() and idx > number.end_idx:
                number = getNumber(idx, line, row_idx)
                numbers.append(number)
    return numbers


def getSolutionPart1(input_list):
    # answer 522726
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    symbol_index_map = get_symbol_index_map(scrubbed)
    valid_numbers = [int(number.value) for number in get_valid_numbers(scrubbed) if number.is_adjacent(symbol_index_map)]
    return sum(valid_numbers)


def getSolutionPart2(input_list):
    # answer 81721933
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    gear_index_map = {key: value.value for key, value in get_symbol_index_map(scrubbed).items() if value.value == "*"}
    valid_numbers = [number for number in get_valid_numbers(scrubbed) if number.is_adjacent(gear_index_map)]
    gears_map = {value.adjacent_key: [] for value in valid_numbers}
    for n in valid_numbers:
        gears_map[n.adjacent_key].append(int(n.value))
    gears_list = list(filter(lambda x: len(x) == 2, gears_map.values()))
    valid_gears = list(map(lambda x: x[0] * x[1], gears_list))
    return sum(valid_gears)


with open('input.txt', mode="r") as f:
    file_input = f.readlines()

part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
else:
    print(getSolutionPart2(file_input))
