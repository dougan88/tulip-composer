import re


class Flowers:

    def __init__(self, flowers_list: list):
        self.flowers_list = flowers_list
        self.is_flowers_list_valid()

    def is_flowers_list_valid(self):
        for flower in self.flowers_list:
            if re.match(r'^[a-z][LS]$', flower) is None:
                raise Exception('Flower doesn\'t match expected pattern')

    def get_flowers_dict(self):
        return {i: self.flowers_list.count(i) for i in self.flowers_list}
