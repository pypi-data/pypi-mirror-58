################################################################
# LAViD - Laboratório de Aplicações de Vídeo Digital
################################################################
# Autor: Caio Moraes
# Email: caiomoraes.cesar@gmail.com
# GitHub: MoraesCaio
#
# LEMBRETE: Essa classe é muito sensível a reordenação
#            de linhas!
################################################################


from .ConverteExtenso import convert_extenso, roman_to_int
from .Iterator import Iterator
import argparse
from unidecode import unidecode
from collections import deque
import re
from .dExtenso import dExtenso


class Number:

    def __init__(self, cardinal=False):
        self.cardinal = cardinal

    cardinal = False

    acceptable = [
        'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'trinta',
        'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa',
        'cento', 'cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
        'seiscentos', 'setecentos', 'oitocentos', 'novecentos', 'mil',
        'milhao', 'milhoes', 'bilhao', 'bilhoes', 'trilhao', 'trilhoes',
        'catorze', 'cincoenta', 'uma', 'duas'
    ]

    ordinais = [
        'zerésimo', 'primeiro', 'segundo', 'terceiro', 'quarto', 'quinto',
        'sexto', 'sétimo', 'oitavo', 'nono'
    ]

    extenso = dExtenso()

    und_dict = {
        'zero': 0,
        'um': 1,
        'uma': 1,
        'uns': 1,
        'umas': 1,
        'dois': 2,
        'duas': 2,
        'três': 3,
        'quatro': 4,
        'cinco': 5,
        'seis': 6,
        'sete': 7,
        'oito': 8,
        'nove': 9,
        'ZERO': 0,
        'UM': 1,
        'UMA': 1,
        'UNS': 1,
        'UMAS': 1,
        'DOIS': 2,
        'DUAS': 2,
        'TRÊS': 3,
        'QUATRO': 4,
        'CINCO': 5,
        'SEIS': 6,
        'SETE': 7,
        'OITO': 8,
        'NOVE': 9,
    }

    teen_dict = {
        'dez': 10,
        'onze': 11,
        'doze': 12,
        'treze': 13,
        'quatorze': 14,
        'catorze': 14,
        'quinze': 15,
        'dezesseis': 16,
        'dezessete': 17,
        'dezoito': 18,
        'dezenove': 19,
        'DEZ': 10,
        'ONZE': 11,
        'DOZE': 12,
        'TREZE': 13,
        'QUATORZE': 14,
        'CATORZE': 14,
        'QUINZE': 15,
        'DEZESSEIS': 16,
        'DEZESSETE': 17,
        'DEZOITO': 18,
        'DEZENOVE': 19,
    }

    dez_dict = {
        'vinte': 20,
        'trinta': 30,
        'quarenta': 40,
        'cinquenta': 50,
        'cincoenta': 50,
        'sessenta': 60,
        'setenta': 70,
        'oitenta': 80,
        'noventa': 90,
        'VINTE': 20,
        'TRINTA': 30,
        'QUARENTA': 40,
        'CINQUENTA': 50,
        'CINCOENTA': 50,
        'SESSENTA': 60,
        'SETENTA': 70,
        'OITENTA': 80,
        'NOVENTA': 90,
    }

    cent_dict = {
        'cem': 100,
        'cento': 100,
        'duzentos': 200,
        'trezentos': 300,
        'quatrocentos': 400,
        'quinhentos': 500,
        'seiscentos': 600,
        'setecentos': 700,
        'oitocentos': 800,
        'novecentos': 900,
        'CEM': 100,
        'CENTO': 100,
        'DUZENTOS': 200,
        'TREZENTOS': 300,
        'QUATROCENTOS': 400,
        'QUINHENTOS': 500,
        'SEISCENTOS': 600,
        'SETECENTOS': 700,
        'OITOCENTOS': 800,
        'NOVECENTOS': 900,
    }

    milh_dict = {
        'mil': 1000,
        'milhão': 1000000,
        'milhões': 1000000,
        'bilhão': 1000000000,
        'bilhões': 1000000000,
        'MIL': 1000,
        'MILHÃO': 1000000,
        'MILHÕES': 1000000,
        'BILHÃO': 1000000000,
        'BILHÕES': 1000000000,
    }

    num_dict = dict(und_dict)
    num_dict.update(teen_dict)
    num_dict.update(dez_dict)
    num_dict.update(cent_dict)

    valid_dict = dict(num_dict)
    valid_dict.update(milh_dict)

    def set_ord(self, lista):

        for postag in lista:

            if re.fullmatch(r'\d+[ªº]', postag[0]):
                postag[0] = postag[0].replace('ª', 'º')
                postag[1] = 'ORD'
            else:
                postag[0] = postag[0].replace('º', '').replace('ª', '')

        return lista

    def to_ord_Libras(self, lista):

        for postag in lista:
            if postag[1] == 'ORD':
                postag[0] = postag[0].replace('º', '').replace('ª', '')

                try:
                    new_token = ''
                    for c in postag[0]:
                        new_token += self.ordinais[int(c)] + ' '
                    postag[0] = new_token[:-1]
                except Exception as e:
                    pass

        return lista

    def to_extenso(self, lista):
        for postag in lista:
            if re.fullmatch(r'(\d+\.)?\d+', postag[0]):
                if '.' in postag[0]:
                    integers, decimals = postag[0].split('.')
                    ext_integers = self.extenso.getExtenso(integers) if integers != '0' else 'zero'
                    ext_decimals = self.extenso.getExtenso(decimals)
                    postag[0] = (ext_integers + ' . ' + ext_decimals).replace(' e', ' ')
                else:
                    postag[0] = self.extenso.getExtenso(postag[0])

        return lista

    def get_grandeza(self, word):

        if word in self.und_dict or word in self.teen_dict:
            return 1
        elif word in self.dez_dict:
            return 2
        elif word in self.cent_dict:
            return 3
        else:
            return 4

    def spelled_to_cardinal(self, spelled_num):
        result = 0
        current_group = 0
        order = 0
        last_order = 4
        parsed = []
        # uncomment for testing
        # error = True

        for word in spelled_num.split():

            if word in ['e', 'E']:
                parsed.append(word)
                continue

            if word in self.valid_dict:
                error = False

                order = self.get_grandeza(word)
                if order != 4 and order >= last_order or \
                        last_order == 2 and word in self.teen_dict:
                    # uncomment for testing
                    # error = True
                    break

                parsed.append(word)

                if word in self.num_dict:
                    current_group += self.num_dict[word]
                elif word in self.milh_dict:
                    # 0 <= current_group
                    tmp = (current_group if current_group else 1) * self.milh_dict[word]
                    result += tmp
                    current_group = 0

                last_order = order

        result += current_group

        # uncomment for testing
        # if error:
        #     result = -1

        return result, ' '.join(parsed)

    def is_spelled_num_word(self, word):
        return word in ['e', 'E'] or word in self.valid_dict

    def get_one_spelled_num(self, phrase, starting_idx=0):

        spelled_num = []
        first_ext = False
        first_ext_idx = -1

        for i, word in enumerate(phrase.split()[starting_idx:]):

            is_spelled_num_word_bool = self.is_spelled_num_word(word)

            if not first_ext and is_spelled_num_word_bool:
                first_ext = True
                first_ext_idx = i

            if first_ext:
                if is_spelled_num_word_bool:
                    spelled_num.append(word)
                else:
                    break

        return ' '.join(spelled_num), first_ext_idx

    def parse_every_spelled_num(self, phrase):

        phrase = re.sub(r'\b[eE]\b', r'', phrase)
        phrase = re.sub(r' {2,}', r' ', phrase)

        spelled_num, first_ext_idx = self.get_one_spelled_num(phrase)

        while first_ext_idx != -1:
            cardinal, parsed = self.spelled_to_cardinal(spelled_num)
            phrase = re.sub(parsed, str(cardinal), phrase, count=1)
            spelled_num, first_ext_idx = self.get_one_spelled_num(phrase, starting_idx=first_ext_idx)

        return phrase

    def converter_extenso(self, lista):
        '''Converte número por extenso para sua forma numerica.
        '''
        lista_extensos = []
        indices_deletar = []
        count = 0
        is_sequence = False
        for i in range(len(lista)):
            token = lista[i][0]
            tag = lista[i][1]
            if tag.startswith("NUM") and token.isalpha() or\
                    (is_sequence and tag.startswith('D-UM') and not tag.endswith('-P')):
                # Verifico se não há sequência de obtenção de extenso em andamento para começar a obter um nova sequência
                # print('True' if is_sequence else 'False')
                if not is_sequence:  # and len(lista_extensos) == count (???)
                    lista_extensos.append([i, [token]])  # i = Posição do primeiro extenso encontrado, token = número por extenso
                    is_sequence = True
                else:
                    lista_extensos[count][1].append(token)  # Pego número por extenso que está na sequência e adiciona na lista
                    # print('indices_deletar.append(i)')
                    indices_deletar.append(i)  # Insiro indice na lista para ser removido depois
            elif is_sequence:
                # Se o token anterior e o próximo foram classificados como número, e o token atual como conjunção, significa que podemos remove-lo
                if ((i + 1 < len(lista)) and (lista[i - 1][1] == "NUM") and (lista[i + 1][1] == "NUM" or lista[i + 1][1].startswith("D-UM")) and (tag == "CONJ")):
                    indices_deletar.append(i)
                else:
                    # A sequência foi quebrada, o que significa que selecionamos o extenso do número por completo
                    # Podemos agora procurar por outra sequencia de número por extenso na lista
                    is_sequence = False
                    count += 1

        for extenso in lista_extensos:
            soma = convert_extenso(' '.join(extenso[1]))
            print(extenso, soma)

            lista[extenso[0]] = [str(soma), "NUM"]

        deque((list.pop(lista, i) for i in sorted(indices_deletar, reverse=True)), maxlen=0)
        return lista

    def simplificar_sentenca(self, lista):
        '''Simplifica a sentença para que possa evitar a ditalogia.
        Como por exemplo a troca de uma palavra no plural para singular.
        '''
        lista_simplificada = [list(x) for x in lista]
        it = Iterator()
        it.load(lista_simplificada)

        while(it.has_next()):

            try:
                num_romano = roman_to_int(it.get_word())
                if it.get_prev_ticket()[-2:] == "-F":
                    lista_simplificada[it.get_count()] = [num_romano + "ª", 'ORD']
                else:
                    lista_simplificada[it.get_count()] = [num_romano + "º", 'ORD']
            except:
                pass

        lista_simplificada = self.set_ord(lista_simplificada)

        if not self.cardinal:
            lista_simplificada = self.to_extenso(lista_simplificada)

        return lista_simplificada


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('extenso', help='Número por extenso')
    args, _ = parser.parse_known_args()

    n = Number()

    exs = unidecode(args.extenso.lower()).split()
    extensos = [e for e in exs if e in n.acceptable]
    print('result', convert_extenso(' '.join(extensos)))


if __name__ == '__main__':
    main()
