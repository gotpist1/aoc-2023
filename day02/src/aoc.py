from os import environ

bag_content = {"red": 12, "green": 13, "blue": 14}


class Game:
    def __init__(self, id, cube_subsets):
        self.id = id
        self.cube_subsets = cube_subsets

    def is_valid(self):
        for cube_subset in self.cube_subsets:
            for key, value in cube_subset.items():
                value_in_bag = bag_content[key]
                if value > value_in_bag:
                    return False
        return True

    def get_power(self):
        max_dict = {k: max(d[k] for d in self.cube_subsets if k in d) for k in bag_content.keys()}
        return max_dict["red"] * max_dict["green"] * max_dict["blue"]


def get_subset_list_map(subset_list):
    tmp_list = []
    for entry in [subset.split(",") for subset in subset_list]:
        sb_map = {key[1]: int(key[0]) for key in [key for row in entry for key in [row.strip().split(" ")]]}
        tmp_list.append(sb_map)
    return tmp_list


def map_to_game(line):
    tmp = line.split(":")
    id = tmp[0].replace("Game ", "")
    subset_list = [x.strip() for x in tmp[1].split(";")]
    return Game(id, get_subset_list_map(subset_list))


def getSolutionPart1(input_list):
    # 2512 answer
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    games = [map_to_game(line) for line in scrubbed]
    valid_game_ids = [int(game.id) for game in games if game.is_valid()]
    return sum(valid_game_ids)


def getSolutionPart2(input_list):
    # 67335 answer
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    games = [map_to_game(line) for line in scrubbed]
    game_powers = [game.get_power() for game in games]
    return sum(game_powers)


with open('input.txt', mode="r") as f:
    file_input = f.readlines()

part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
else:
    print(getSolutionPart2(file_input))
