import unittest

from day03.src.aoc import getSolutionPart1, getSolutionPart2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('input.txt', mode="r") as f:
            file_input = f.readlines()
        sum = getSolutionPart2(file_input)


        print(sum)


if __name__ == '__main__':
    unittest.main()
