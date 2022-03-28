# yaml w/words
#  each word has info on posible placement
import yaml
from random import choice, randint

# filter dictionary by attribute
def _filter_by(dictionary, filter_attr):
    return list(filter(lambda x: filter_attr in x['def'].lower(), dictionary))

def gen_word(word_order, dictionary):
    _verbs = _filter_by(dictionary, 'verb')
    _nouns = _filter_by(dictionary, 'noun')
    _map = {
        'v': lambda: choice(_verbs),
        's': lambda: choice(_nouns),
        'o': lambda: choice(_nouns),
    }

    word = ''
    definitions = []
    for func_code in word_order:
        elem = _map[func_code]()
        word += elem['word'] + ' '
        definitions.append(elem['def'])

    return word, definitions

lang = 'example'

with open(f'{lang}/example.yaml') as yaml_file:
    dictionary = yaml.load(yaml_file, Loader=yaml.FullLoader)

with open(f'{lang}/config.yaml') as yaml_file:
    cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

print(cfg)
if not 'word-order' in cfg or len(cfg['word-order']) == 0:
    raise Exception(f'no \'word order\' specified in {lang}/config.yaml')

wo = choice(cfg['word-order']) if len(cfg['word-order']) > 0 else cfg['word-order'][0]
word, definitions = gen_word(wo, dictionary)
print('word order:', wo)
print('word:', word)
# print('definitions:', definitions)
