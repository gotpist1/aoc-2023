import re
from os import environ


class Seed:
    def __init__(self, chunk=[], min=None, max=None):
        self.min = chunk[0] if min is None else min
        self.max = chunk[0] + chunk[1] - 1 if max is None else max

    def set_min(self, min):
        self.min = min
        return self


class Range:
    def __init__(self, destination, source, length):
        self.destination = destination
        self.source = source
        self.length = length
        self.source_max = source + length - 1

    def is_in_range(self, seed):
        return self.source <= seed <= self.source + self.length

    def move(self, seed):
        return seed + self.destination - self.source


class Input:
    def __init__(self, array):
        self.seed_list = None
        self.mappings_dict = None
        self.__set_mappings(array)

    def __set_mappings(self, input_array):
        maps = {}
        seeds_list = []
        map_key = ''
        for input in input_array:
            if 'seeds:' in input:
                seeds_list = list(map(lambda x: int(x), filter(lambda x: x != '', input.split(':')[1].split(' '))))
                print(seeds_list)
            elif 'map' in input:
                map_key = input.split(' ')[0].strip()
                maps[map_key] = []
            else:
                numbers = list(
                    map(lambda x: Range(int(x[0]), int(x[1]), int(x[2])), re.findall(r'(\d+) (\d+) (\d+)', input)))
                numbers.sort(key=lambda x: x.source)
                maps[map_key].append(numbers)
        self.seed_list = seeds_list
        self.mappings_dict = maps


def getSolutionPart1(input_list):
    array = list(filter(lambda x: x != '', input_list.split('\n')))
    input = Input(array)
    maps = input.mappings_dict
    seeds_list = input.seed_list
    for map in maps.values():
        for i in range(len(seeds_list)):
            for range_obj in map:
                r = range_obj[0]
                if r.is_in_range(seeds_list[i]):
                    seeds_list[i] = r.move(seeds_list[i])
                    break
    print(seeds_list)
    return min(seeds_list)


def getSolutionPart2(input_list):
    # 59370572  slow solution needs to be improved
    array = list(filter(lambda x: x != '', input_list.split('\n')))
    input = Input(array)
    maps = input.mappings_dict
    seeds_list_chunks = [input.seed_list[i:i + 2] for i in range(0, len(input.seed_list), 2)]
    seeds_list = []
    for chunk in seeds_list_chunks:
        print(chunk)
        for i in range(chunk[0], chunk[0] + chunk[1] - 1):
            seeds_list.append(i)
    seeds_list.sort(key=lambda x: x)
    for map in maps.values():
        for i in range(len(seeds_list)):
            for range_obj in map:
                r = range_obj[0]
                if r.is_in_range(seeds_list[i]):
                    seeds_list[i] = r.move(seeds_list[i])
                    break

    return min(seeds_list)



with open('test_input.txt', mode="r") as f:
    file_input = f.read()
part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
elif part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart2(file_input))
