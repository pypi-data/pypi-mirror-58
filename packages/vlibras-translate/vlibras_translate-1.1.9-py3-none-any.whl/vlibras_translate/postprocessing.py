#---------------------------------
#
# Author: Caio Moraes
# Email: <caiomoraes.cesar@gmail.com>
# GitHub: MoraesCaio
#
# LAViD - Laboratório de Aplicações de Vídeo Digital
#
#---------------------------------

import re
from unidecode import unidecode
from .number import Number
from .char_preprocessing import LATIN_CHARS


class Postprocessor():

    def __init__(self, number_instance=None):
        self._number = Number(cardinal=True) if not number_instance else number_instance
        self.acceptable = [unidecode(num) for num in Number.acceptable]

    def _convert_spelled_num_to_cardinal(self, sentence):
        return self._number.parse_every_spelled_num(sentence)

    def _convert_directionals(self, sentence):
        '''Convert PERGUNTAR_1S_3S -> 1S_PERGUNTAR_3S.'''
        return re.sub(rf'([{LATIN_CHARS}]+)_([123][SP])(_[123][SP])', r'\2_\1\3', sentence)

    def _remove_repeated_words(self, sentence):
        '''Remove repeated words: A B B C -> A B C.'''
        last_word = None
        final_sentence = []
        for word in sentence.split():
            if word == last_word:
                continue

            final_sentence.append(word)
            last_word = word

        return ' '.join(final_sentence)

    def _fix_for_presiden(self, sentence_before_dl, sentence_after_dl):
        '''Hard fix for PRESIDENTE/PRESIDENCIAL turning into PRESIDIÁRIO in some sentences.'''
        if 'PRESIDEN' in sentence_before_dl and 'PRESIDIÁRIO' in sentence_after_dl:
            return re.sub(r'PRESIDIÁRIO', rf'PRESIDENTE', sentence_after_dl)

        return sentence_after_dl

    def postprocess(self, sentence, sentence_before_dl=None):
        '''Run all postprocessing methods in sequence and return final sentence.'''

        # NMT specific postprocessing
        if sentence_before_dl:
            sentence = self._fix_for_presiden(sentence_before_dl, sentence)

        sentence = self._convert_directionals(sentence)
        sentence = self._convert_spelled_num_to_cardinal(sentence)
        sentence = self._remove_repeated_words(sentence)

        return sentence
