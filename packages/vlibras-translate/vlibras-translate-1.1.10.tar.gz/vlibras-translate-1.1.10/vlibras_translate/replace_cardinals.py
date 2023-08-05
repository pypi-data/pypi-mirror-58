import re
from dExtenso import dExtenso


def to_extenso(sentence):

    extenso = dExtenso()

    for token in sentence.split():

        if re.fullmatch(r'(\d*\.)?\d+', token):

            if '.' in token:

                integers, decimals = token.split('.')
                ext_integers = extenso.getExtenso(integers) if integers != '' else 'zero'
                ext_decimals = extenso.getExtenso(decimals)

                new_token = (ext_integers + ' VÍRGULA ' + ext_decimals).replace(' e', ' ')

            else:

                new_token = extenso.getExtenso(token)

            sentence = re.sub(fr'(^|\s){token}(\s|$)', fr'\1{new_token}\2', sentence, count=1)
    return sentence


def fix_wrong_directionals(sentence):

    sentence = re.sub(r'([SP])([123])', r'\2\1', sentence)
    return sentence


# print(to_extenso('2 1S_dar_3P 2 . 6 reais 0.4 2 3'))
with open('a') as f:
    for l in f:
        print(fix_wrong_directionals(l))
