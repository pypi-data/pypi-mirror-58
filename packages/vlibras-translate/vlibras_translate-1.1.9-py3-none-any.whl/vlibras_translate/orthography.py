#---------------------------------
#
# Author: Caio Moraes
# Email: <caiomoraes.cesar@gmail.com>
# GitHub: MoraesCaio
#
# LAViD - Laboratório de Aplicações de Vídeo Digital
#
#---------------------------------


import string
import argparse
from .singleton import Singleton
from os import path
import re
import platform
from .char_preprocessing import LATIN_CHARS
if platform.system() == 'Linux':
    import hunspell


class Orthography(metaclass=Singleton):

    def __init__(cls, dic='hunspell/ptbr.dic', aff='hunspell/ptbr.aff', wout_bpe=False):
        cls.on_linux = platform.system() == 'Linux'
        cls.wout_bpe = wout_bpe

        if cls.on_linux:
            this_file_path = path.abspath(__file__)
            directory = path.dirname(this_file_path)
            cls.hunspell = hunspell.HunSpell(path.join(directory, dic), path.join(directory, aff))

    def check(cls, word):
        '''Return True if the word is correct in Pt-BR'''
        if not cls.on_linux:
            return True

        try:

            # context marker
            if word == '&':
                return True

            # compound word
            if not cls.wout_bpe and any([x in word for x in ['&famoso', '&cidade', '&estado', '&país']]):
                return True

            is_correct = all([cls.hunspell.spell(cls.remove_special_case(w)) for w in re.split(r'[_&]', word)])

        except UnicodeEncodeError:
            return False

        return is_correct

    def remove_special_case(cls, word):

        w = re.sub(r'[123][sp]', '', word)
        w = re.sub(rf'\([+-]+\)(?=[{LATIN_CHARS}])', '', w)
        w = re.sub(rf'(?<=[{LATIN_CHARS}])\([+-]+\)', '', w)

        return w


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phrase', help='Phrase')
    args, _ = parser.parse_known_args()

    orthography = Orthography()

    table = str.maketrans(dict.fromkeys("“”«»–’‘º" + string.punctuation))
    phrase = args.phrase.translate(table)

    for word in phrase.split():
        print(word)
        if not orthography.check(word):
            print('Error in:', word)


if __name__ == '__main__':
    main()
