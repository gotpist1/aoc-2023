import re
from os import environ

mapped_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                 "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def get_calibration_values(line):
    first_num = re.findall(r'\d', line)[0]
    last_num = re.findall(r'\d', line)[-1]
    print(first_num, last_num)
    return int(first_num + last_num)

def get_calibration_values_with_words(line):
    line = (line.replace("oneight", "oneeight")
            .replace("threeight","threeeight")
            .replace("fiveight","fiveeight")
            .replace("nineight","nineeight")
            .replace("twone","twoone")
            .replace("sevenine","sevennine")
            .replace("eightwo","eighttwo"))
    pattern = r'(?:one|two|three|four|five|six|seven|eight|nine|\d)'
    match = re.findall(pattern, line)
    print(match)
    if match:
        first_num = match[0]
        last_num = match[-1]
        if first_num in mapped_digits.keys():
            first_num = mapped_digits[first_num]
        if last_num in mapped_digits.keys():
            last_num = mapped_digits[last_num]
        combined = first_num + last_num
        print(combined, line)
        return int(combined)



def getSolutionPart1(input_list):
    calibration_values = []
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    for line in scrubbed:
        calibration_values.append(get_calibration_values(line))
    return sum(calibration_values)


def getSolutionPart2(input_list):
    calibration_values = []
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    for line in scrubbed:
        calibration_values.append(get_calibration_values_with_words(line))
    return sum(calibration_values)


with open('input.txt', mode="r") as f:
    file_input = f.readlines()

part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
else:
    print(getSolutionPart2(file_input))

