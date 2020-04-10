import re


class Bouquet:

    def __init__(self, bouquet_spec: str):
        self.bouquet = ''
        self.bouquet_spec = bouquet_spec
        if not self.__is_bouquet_spec_valid():
            raise Exception('Bouquet spec is of the incorrect format')
        self.not_specified_quantity = int(self.get_total()) - int(self.get_specified_quantity())
        if self.not_specified_quantity < 0:
            raise Exception('Flowers quantities are inconsistent')

    def get_flowers_dict(self):
        size = self.bouquet_spec[1]
        flowers = re.findall(r'\d+[a-z]', self.bouquet_spec)
        return {val[-1]+size: int(val[:-1]) for val in flowers}

    def get_total(self):
        return re.search(r'\d+$', self.bouquet_spec).group()

    def get_specified_quantity(self):
        quantity_list = re.findall(r'\d+', self.bouquet_spec)
        quantity_list = list(map(lambda x: int(x), quantity_list))
        return sum(quantity_list[:-1])

    def get_not_specified_quantity(self):
        return self.not_specified_quantity

    def get_size(self):
        return self.bouquet_spec[1]

    def get_initial_design(self):
        return re.search(r'^[A-Z][LS](\d+[a-z])+', self.bouquet_spec).group()

    def set_bouquet(self, bouquet: str):
        self.bouquet = self.__remove_duplicates(bouquet)

    def get_bouquet(self):
        return self.bouquet

    def __is_bouquet_spec_valid(self):
        return not re.match(r'^[A-Z][LS](\d+[a-z])+\d+$', self.bouquet_spec) is None

    @staticmethod
    def __remove_duplicates(bouquet_design: str):
        flowers = re.findall(r'(\d+)([a-z])', bouquet_design)
        flowers_dict = dict()
        for flower in flowers:
            flowers_dict[flower[1]] = int(flower[0]) if flower[1] not in flowers_dict \
                else flowers_dict[flower[1]] + int(flower[0])

            bouquet_design = bouquet_design[:2]
        for flower, quantity in flowers_dict.items():
            bouquet_design += str(quantity) + flower

        return bouquet_design
