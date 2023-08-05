#---------------------------------
#
# Author: Caio Moraes
# Email: <caiomoraes.cesar@gmail.com>
# GitHub: MoraesCaio
#
# LAViD - Laboratório de Aplicações de Vídeo Digital
#
#---------------------------------

import argparse
import re
from collections import Counter
from os import path
from .name_checking import NameChecking
from .orthography import Orthography
from .singleton import Singleton
from .utils import is_sublist
from .char_preprocessing import LATIN_CHARS


class WordProcessing(metaclass=Singleton):

    synonyms = {}
    places = {}
    people = {}
    sorted_synonyms_keys = []
    synonyms_with_removables = {}
    sorted_synonyms_with_removables_keys = []
    famous_people = []
    names = []
    numbers = []
    errors = []
    whitelist_words = []
    found_whitelist_words = []
    name_checking = None
    orthography = None
    wout_bpe = False

    def __init__(self, wout_bpe=False):

        this_file_path = path.abspath(__file__)
        directory = path.dirname(this_file_path)
        self.wout_bpe = wout_bpe
        self.name_checking = NameChecking()
        self.orthography = Orthography(wout_bpe=wout_bpe)

        with open(path.join(directory, 'palavras_compostas_e_sinonimos'), 'r', encoding='utf-8') as file:

            for line in file:

                key, value = [part for part in line.replace('\n', '').split(';')]

                if key not in self.synonyms:
                    self.synonyms[key] = value
                    self.sorted_synonyms_keys.append(key)

            self.sorted_synonyms_keys.sort(key=lambda x: -len(x))

        with open(path.join(directory, 'expressoes_com_palavras_removiveis'), 'r', encoding='utf-8') as file:

            for line in file:

                key, value = [part for part in line.replace('\n', '').split(';')]

                if key not in self.synonyms:
                    self.synonyms_with_removables[key] = value
                    self.sorted_synonyms_with_removables_keys.append(key)
                    self.whitelist_words.append(key.lower().split())

            self.sorted_synonyms_with_removables_keys.sort(key=lambda x: -len(x))

        with open(path.join(directory, 'lugares'), 'r', encoding='utf-8') as file:

            for line in file:

                key, value = line.replace('\n', '').split(':')

                self.places[key] = value
                self.whitelist_words.append(key.lower().split())

        with open(path.join(directory, 'famosos'), 'r', encoding='utf-8') as file:

            for line in file:

                key, value = line.replace('\n', '').split(':')

                self.people[key] = value
                self.whitelist_words.append(key.lower().split())

    def whitelist_tag_sentence(self, tag_sentence):
        occurrences = []

        for whitelist_word in self.whitelist_words:
            idxs = is_sublist([t[0] for t in tag_sentence], whitelist_word)
            if idxs:
                occurrences.append(idxs)

        for occurrence in occurrences:
            whitelist_word_length = len(occurrence[0])
            idxs = occurrence[1]
            for idx in idxs:
                for i in range(whitelist_word_length):
                    tag_sentence[idx + i][1] = 'WL'

    def replace_synonyms(self, sentence):

        for key in self.sorted_synonyms_keys:
            # replace only if is not part of a word
            # underline prevents errors like
            #  prisão domiciliar -> prisão_casa (correct translation: prisão_domiciliar)
            sentence = re.sub(rf'(?:^|(?<=[^{LATIN_CHARS}_]))' + key + rf'(?=[^{LATIN_CHARS}_]|$)', self.synonyms[key], sentence)

        return sentence

    def replace_synonyms_with_removables(self, sentence):

        for key in self.sorted_synonyms_with_removables_keys:
            # replace only if is not part of a word
            # underline prevents errors like
            #  prisão domiciliar -> prisão_casa (correct translation: prisão_domiciliar)
            sentence = re.sub(rf'(?:^|(?<=[^{LATIN_CHARS}_]))' + key + rf'(?=[^{LATIN_CHARS}_]|$)', self.synonyms_with_removables[key], sentence)

        return sentence

    def replace_places_and_people(self, sentence):

        for key in self.places:
            sentence = re.sub(rf'(?:^|(?<=[^{LATIN_CHARS}_]))' + key + rf'(?=[^{LATIN_CHARS}_]|$)', self.places[key], sentence)

        for key in self.people:
            sentence = re.sub(rf'(?:^|(?<=[^{LATIN_CHARS}_]))' + key + rf'(?=[^{LATIN_CHARS}_]|$)', self.people[key], sentence)

        return sentence

    def mask_tag_sentence(self, tag_sentence, name_symbol='"', number_symbol="'", error_symbol='#', input_lang=''):

        # SUBSTITUIÇÃO POR SÍMBOLOS
        # se é arquivo de teste, NÃO substitui NOMES, NÚMEROS e ERROS ORTOGRÁFICAOS por símbolos
        for tag in tag_sentence:

            if self.wout_bpe and re.match(rf'[{LATIN_CHARS}_]+&(cidade|estado|país|região|famoso|famosa)', tag[0]):
                tag[0] = name_symbol

            elif tag[1] == 'WL':
                if input_lang == 'gi':
                    tag[0] = name_symbol
                else:
                    continue

            elif input_lang == 'gi' and re.match(rf'[{LATIN_CHARS}_]+&(cidade|estado|país|região|famoso|famosa)', tag[0]):
                continue

            # NÚMERO
            elif 'NUM' in tag[1] and not tag[0].isalpha():
                self.numbers.append(tag[0])
                tag[0] = re.sub(r'\d+', number_symbol, tag[0])

            # NOME PRÓPRIO (DETECÇÃO DO AELIUS)
            elif input_lang == 'pt' and 'NPR' in tag[1]:
                self.names.append(tag[0])
                tag[0] = name_symbol

            # NOME PRÓPRIO (DETECÇÃO DO DICIONÁRIO DE NOMES)
            # não é verbo ser, estar, haver, ter ou outro verbo
            # PS.: encontrei muitos nomes homônimos de verbos;
            #       talvez não seja mais necessário verificar isso
            elif self.name_checking.is_tag_name(tag):
                self.names.append(tag[0])
                tag[0] = name_symbol
                tag[1] = 'NPR'

            # ERRO ORTOGRÁFICO
            # 'não é pontuação, símbolo reservado, número ou nome e está errado'
            elif not tag[1].startswith('SPT') and\
                    not self.orthography.check(tag[0]) and\
                    '-' not in tag[0]:
                self.errors.append(tag[0])
                tag[0] = error_symbol

        return tag_sentence

    # legacy
    def mask_tag_sentence_gr_gi(self, rule_tag_sentence, interpreter_tag_sentence, name_symbol='"', number_symbol="'", error_symbol='#'):

        famous_people = Counter()
        places = Counter()

        for interpreter_tag in interpreter_tag_sentence:
            interpreter_tag[0] = re.sub(r'\d+(?![sp])', number_symbol, interpreter_tag[0])
            if interpreter_tag[0].endswith('_famoso'):
                interpreter_tag[1] = 'FAM'
                famous_people += Counter(interpreter_tag[0].replace('_famoso', '').split('_'))
            else:
                for place_sufix in ['_cidade', '_estado', '_país']:
                    if interpreter_tag[0].endswith(place_sufix):
                        places += Counter(interpreter_tag[0].replace(place_sufix, '').split('_'))
                        interpreter_tag[1] = 'LOC'

        for rule_tag in rule_tag_sentence:
            rule_tag[0] = re.sub(r'\d+(?![sp])', number_symbol, rule_tag[0])

            if rule_tag[0] in famous_people:

                rule_tag[1] = 'FAM'
                famous_people[rule_tag[0]] -= 1

            elif rule_tag[1] in places:

                rule_tag[1] = 'LOC'
                places[rule_tag[0]] -= 1

            elif self.name_checking.is_tag_name(rule_tag):

                for interpreter_tag in interpreter_tag_sentence:
                    if rule_tag[0] == interpreter_tag[0]:
                        interpreter_tag[0] = name_symbol
                        interpreter_tag[1] = 'NPR'
                        break

                rule_tag[0] = name_symbol
                rule_tag[1] = 'NPR'

            elif not rule_tag[1].startswith('SPT') and\
                    not self.orthography.check(rule_tag[0]):

                for interpreter_tag in interpreter_tag_sentence:
                    if rule_tag[0] == interpreter_tag[0]:
                        rule_tag[0] = error_symbol
                        interpreter_tag[0] = error_symbol

        return rule_tag_sentence, interpreter_tag_sentence

    def mask_tag_sentence_pt_glosa(self, tag_sentence, tag_sentence_glosa, name_symbol='"', number_symbol="'", error_symbol='#'):
        # TODO fazer exeção pra quando não achar correspondente
        # SUBSTITUIÇÃO POR SÍMBOLOS
        # se é arquivo de teste, NÃO substitui NOMES, NÚMEROS e ERROS ORTOGRÁFICAOS por símbolos
        for tag_glosa in tag_sentence_glosa:
            tag_glosa[0] = re.sub(r'\d+', number_symbol, tag_glosa[0])

        for tag in tag_sentence:

            # NÚMERO
            if 'NUM' in tag[1] and not tag[0].isalpha():
                tag[0] = re.sub(r'\d+', number_symbol, tag[0])

            # NOME PRÓPRIO (DETECÇÃO DO AELIUS)
            elif 'NPR' in tag[1]:
                for tag_glosa in tag_sentence_glosa:
                    if (tag_glosa[0] == tag[0]):
                        tag_glosa[0] = name_symbol
                        break
                tag[0] = name_symbol

            # NOME PRÓPRIO (DETECÇÃO DO DICIONÁRIO DE NOMES)
            # não é verbo ser, estar, haver, ter ou outro verbo
            # PS.: encontrei muitos nomes homônimos de verbos;
            #       talvez não seja mais necessário verificar isso
            elif self.name_checking.is_tag_name(tag):
                for tag_glosa in tag_sentence_glosa:
                    if (tag_glosa[0] == tag[0]):
                        tag_glosa[0] = name_symbol
                        tag_glosa[1] = 'NPR'
                        break
                tag[0] = name_symbol
                tag[1] = 'NPR'

            # ERRO ORTOGRÁFICO
            # 'não é pontuação, símbolo reservado, número ou nome e está errado'
            elif not tag[1].startswith('SPT') and\
                    not self.orthography.check(tag[0]) and\
                    '-' not in tag[0]:
                for tag_glosa in tag_sentence_glosa:
                    if (tag_glosa[0] == tag[0]):
                        tag_glosa[0] = error_symbol
                        break
                tag[0] = error_symbol

        return tag_sentence, tag_sentence_glosa

    def mask_whitelist_words(self, tag_sentence, whitelist_symbol='@'):

        # print('tag_sentence', tag_sentence)

        for token in tag_sentence:

            if token[0] in self.whitelist_words:
                self.found_whitelist_words.append(token[0])
                token[0] = whitelist_symbol

        # print('tag_sentence', tag_sentence)

        return tag_sentence

    def restore_whitelist_words(self, sentence, whitelist_symbol='@'):

        for word in self.found_whitelist_words:
            sentence = re.sub(whitelist_symbol, word.upper(), sentence, count=1)

        self.found_whitelist_words = []

        return sentence

    def restore_named_entities(self, sentence, name_symbol='"', number_symbol="'", error_symbol='#'):

        for name in self.names:
            sentence = re.sub(name_symbol, name.upper(), sentence, count=1)

        for number in self.numbers:
            for part in number.replace(' ', '').split(','):
                sentence = re.sub(number_symbol, part, sentence, count=1)

        for error in self.errors:
            sentence = re.sub(error_symbol, error.upper(), sentence, count=1)

        self.names, self.numbers, self.errors = [], [], []

        return sentence


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence')
    args, _ = parser.parse_known_args()

    wp = WordProcessing()
    print(wp.replace_synonyms(args.sentence))


if __name__ == '__main__':
    main()
