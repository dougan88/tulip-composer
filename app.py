from src.Bouquet import Bouquet
from src.Composer import Composer
from src.Flowers import Flowers

if __name__ == '__main__':
    file = open('sample.txt', 'r')
    input_text = file.read()
    bouquets_input = list(map(lambda x: x.strip(), input_text.split('\n\n')))
    bouquet_specs = bouquets_input[0].split('\n')
    flowers_list = bouquets_input[1].split('\n')
    bouquet_specs = [Bouquet(bouquet) for bouquet in bouquet_specs]
    composer = Composer(bouquet_specs, Flowers(flowers_list))
    print('\n'.join(composer.compose()))


