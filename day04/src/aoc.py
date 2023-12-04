import re
from os import environ


class Card:
    def __init__(self, card_id, winning_cards, handling_cards):
        self.card_id = card_id
        self.winning_cards = winning_cards
        self.handling_cards = handling_cards
        self.card_wins = self.__get_card_wins()
        self.card_copies = self.__get_card_copies()

    def __get_card_wins(self):
        sum_points = 0
        for handling_card in self.handling_cards:
            if handling_card in self.winning_cards:
                sum_points += 1
        return sum_points

    def __get_card_copies(self):
        return [self.card_id + 1 + i for i in range(self.card_wins)]


def map_to_card(line):
    r = re.compile(r'(\d+:)')
    tmp_list = line.split('|')
    card_id = re.search(r, tmp_list[0]).group(1).replace(":", "")
    winning_cards = list(filter(lambda x: x != '' and x != 'Card' and x != f'{card_id}:',
                                tmp_list[0].replace(f"Card {card_id}:", "").split(" ")))
    handling_cards = list(filter(lambda x: x != '', tmp_list[1].split(" ")))
    return Card(int(card_id), winning_cards, handling_cards)


def get_card_wins_and_copies(cards_map, card):
    total_cards = 0
    for card_id in card.card_copies:
        total_cards += 1
        total_cards += get_card_wins_and_copies(cards_map, cards_map.get(card_id))
    return total_cards


def getSolutionPart1(input_list):
    # 23678
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    card_points = []
    for card in [map_to_card(line) for line in scrubbed]:
        sum_points = 0
        for handling_card in card.handling_cards:
            if handling_card in card.winning_cards:
                sum_points += sum_points if sum_points != 0 else 1
        card_points.append(sum_points)

    return sum(card_points)


def getSolutionPart2(input_list):
    # 15455663
    scrubbed = list(map(lambda x: x.rstrip(), input_list))
    cards_map = {card.card_id: card for card in [map_to_card(line) for line in scrubbed]}
    total_scratch_cards = len(cards_map.values())
    for card_id, card in cards_map.items():
        total_scratch_cards += get_card_wins_and_copies(cards_map, card)

    return total_scratch_cards


with open('input.txt', mode="r") as f:
    file_input = f.readlines()

part = environ.get('part')

if part == 'part1':
    print(getSolutionPart1(file_input))
else:
    print(getSolutionPart2(file_input))
