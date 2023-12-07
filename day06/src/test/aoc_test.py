import unittest
from functools import reduce

from day05.src.aoc import getSolutionPart2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('input.txt') as file:
            file_input = file.read()
            res = getSolutionPart2(file_input)
            print(res)




if __name__ == '__main__':
    unittest.main()
