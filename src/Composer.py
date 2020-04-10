from typing import List
from src.Flowers import Flowers
from .Bouquet import Bouquet
from collections import Counter
from copy import deepcopy


class Composer:

    SMALL_SIGN = 'S'
    LARGE_SIGN = 'L'

    def __init__(self, bouquets: List[Bouquet], flowers_list: Flowers):
        self.bouquets = bouquets
        self.flowers_list = flowers_list
        self.flowers_dict = self.flowers_list.get_flowers_dict()

        bouquet_sum = Counter()
        for bouquet in self.bouquets:
            bouquet_sum += Counter(bouquet.get_flowers_dict())
        self.bouquet_flowers_dict = dict(bouquet_sum)

    def compose(self):
        self.__subtract_flowers()

        return [bouquet.get_bouquet() for bouquet in self.bouquets]

    def __subtract_flowers(self):
        flowers_dict = self.flowers_dict
        for name, quantity in self.bouquet_flowers_dict.items():
            if name not in flowers_dict or flowers_dict[name] - quantity < 0:
                raise Exception('Not enough flowers')
            flowers_dict[name] -= quantity

        flowers_dict = {k: v for k, v in flowers_dict.items() if v != 0}

        sized_flowers_dict = dict()

        sized_flowers_dict[self.SMALL_SIGN] = {k: v for k, v in flowers_dict.items() if k[-1] == self.SMALL_SIGN}
        sized_flowers_dict[self.LARGE_SIGN] = {k: v for k, v in flowers_dict.items() if k[-1] == self.LARGE_SIGN}

        for bouquet in self.bouquets:
            bouquet_design = bouquet.get_initial_design()
            not_specified_quantity = bouquet.get_not_specified_quantity()
            sized_flowers_dict_copy = deepcopy(sized_flowers_dict.get(bouquet.get_size()))

            if bouquet.get_not_specified_quantity() == 0:
                bouquet.set_bouquet(bouquet_design)
                continue

            for flower, quantity in sized_flowers_dict.get(bouquet.get_size()).items():
                if quantity - not_specified_quantity < 0:
                    bouquet_design += str(quantity) + flower[0]
                    del sized_flowers_dict_copy[flower]
                    not_specified_quantity -= quantity
                elif quantity - not_specified_quantity == 0:
                    bouquet_design += str(quantity) + flower[0]
                    del sized_flowers_dict_copy[flower]
                    not_specified_quantity = 0
                    break
                else:
                    bouquet_design += str(not_specified_quantity) + flower[0]
                    sized_flowers_dict[bouquet.get_size()][flower] = quantity - not_specified_quantity
                    sized_flowers_dict_copy[flower] = quantity - not_specified_quantity
                    not_specified_quantity = 0
                    break
            sized_flowers_dict[bouquet.get_size()] = sized_flowers_dict_copy

            if not_specified_quantity != 0:
                raise Exception('Not enough flowers')
            bouquet.set_bouquet(bouquet_design)
