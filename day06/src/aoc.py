import re
from functools import reduce
from os import environ

from operator import mul


def calc_wins(time, dist):
    winCount = 0
    for i in range(dist):
        calced_time = (time - i) * i
        if calced_time > dist:
            winCount += 1
            print(winCount, i)
        else:
            if winCount > 0:
                break
    return winCount

def getSolutionPart1(input_list):
    time_dist_map = dict(zip(map(int, re.findall(r'\d+', input_list[0])), map(int, re.findall(r'\d+', input_list[1]))))
    wins = [calc_wins(time, dist) for time, dist in time_dist_map.items()]
    print(reduce(mul, wins, 1))
    return ''


def getSolutionPart2(input_list):
    time = int(input_list[0].split(':')[1].replace(' ', ''))
    dist = int(input_list[1].split(':')[1].replace(' ', ''))
    print(calc_wins(time, dist))
    return ''



with open('input.txt', mode="r") as f:
    file_input = f.readlines()
part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
elif part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart2(file_input))
