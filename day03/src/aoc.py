import re
import string
from os import environ


class Number:
    def __init__(self, value, start_idx, end_idx, row, line_length):
        self.value = value
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.row = row
        self.line_length = line_length
        self.adjacent_key = None

    def is_adjacent(self, symbol_index_map) -> bool:
        same_row_hit = self.get_adjacent_key(self.row, symbol_index_map)
        down_hit = self.get_adjacent_key(self.row + 1, symbol_index_map)
        up_hit = self.get_adjacent_key(self.row - 1, symbol_index_map)
        return up_hit or down_hit or same_row_hit

    def get_adjacent_key(self, key, symbol_index_map) -> bool:
        y = [
            self.start_idx,
            self.end_idx,
            self.start_idx + 1,
            self.start_idx - 1,
            self.end_idx + 1

        ]
        for value in y:
            coordinate = str(key) + "-" + str(value)
            if coordinate in symbol_index_map.keys():
                self.adjacent_key = coordinate
                return True


def get_symbol_index_map(scrubbed) -> dict[string, string]:
    symbol_index_map = {}
    r1 = re.compile(r'[^.\d+]$')
    r2 = re.compile(r'[a-zA-Z_#@:;\\/\\\\=!^() +-]+')
    for row_idx, line in enumerate(scrubbed):
        for idx, char in enumerate(line):
            if r1.match(char) or r2.match(char):
                symbol_index_map[str(row_idx) + "-" + str(idx)] = char
    return symbol_index_map


def get_number(start_idx, line, row) -> Number:
    curr_idx = 0
    for idx in range(start_idx, len(line)):
        curr_idx = idx
        if not line[idx].isdigit() or idx == len(line):
            return Number(line[start_idx:idx], start_idx, idx - 1, row, len(line))
    return Number(line[start_idx:curr_idx + 1], start_idx, curr_idx - 1, row, len(line))


def get_valid_numbers(scrubbed):
    numbers = []
    for row_idx, line in enumerate(scrubbed):
        number = None
        for idx, char in enumerate(line):
            if char.isdigit() and number is None or char.isdigit() and idx > number.end_idx:
                number = get_number(idx, line, row_idx)
                numbers.append(number)
    return numbers


def getSolutionPart1(input_list):
    # answer 522726
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    symbol_index_map = get_symbol_index_map(scrubbed)
    valid_numbers = [int(number.value) for number in get_valid_numbers(scrubbed) if
                     number.is_adjacent(symbol_index_map)]
    return sum(valid_numbers)


def getSolutionPart2(input_list):
    # answer 81721933
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    gear_index_map = {key: value for key, value in get_symbol_index_map(scrubbed).items() if value == "*"}
    valid_numbers = [number for number in get_valid_numbers(scrubbed) if number.is_adjacent(gear_index_map)]
    gears_map = {value.adjacent_key: [] for value in valid_numbers}
    for n in valid_numbers:
        gears_map[n.adjacent_key].append(int(n.value))
    valid_gears = list(map(lambda x: x[0] * x[1], list(filter(lambda x: len(x) == 2, gears_map.values()))))
    return sum(valid_gears)


with open('input.txt', mode="r") as f:
    file_input = f.readlines()

part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
else:
    print(getSolutionPart2(file_input))
