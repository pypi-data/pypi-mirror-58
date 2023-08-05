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
import os
import platform
import re
from .utils import now
from .cogroo4py.cogroo4py import Cogroo
from .orthography import Orthography

current_dir = os.path.dirname(os.path.abspath(__file__))
on_windows = platform.system() == "Windows"


class Lemma:

    prefixes = [
        'contra',
        'supra-',
        'super-',
        'arqui-',
        'supra',
        'super',
        'arqui',
        'ultra',
        'intra',
        'sobre',
        'hiper',
        'vice-',
        'anti-',
        'anti',
        'ambi',
        'ante',
        'endo',
        'hipo',
        'vice',
        'pré-',
        'pós-',
        'pre',
        'aná',
        'ana',
        'epí',
        'epi',
        'des',
        'com',
        'con',
        'sim',
        'sin',
        'ex-',
        'co',
        'si',
        'in',
        'an',
        'di',
        'bi',
        'im',
        'en',
        'em',
        'ex',
        're',
        'e',
        'a',
        '',
    ]

    vbs = {
        # 4 primeiros: ir; particípio ['-RA', '-D', '-SD', '-SR']
        # 'SR': ['-PP'],
        # 'HV': ['-P', '-PP', '-AN-F', '-AN-F-P'],
        # 'ET': ['-PP'],
        # 'TR': ['-I', '-PP', '-AN-F', '-AN-F-P'],
        # 'VB': ['-AN', '-AN-F', '-AN-P', '-AN-F-P'],
    }

    poss_pro_f = {
        'minha': 'meu',
        'minhas': 'meus',
        'tua': 'teu',
        'tuas': 'teus',
        'sua': 'seu',
        'suas': 'seus',
        'nossa': 'nosso',
        'nossas': 'nossos',
        'vossa': 'vosso',
        'vossas': 'vossos',
    }

    object_pronouns = {
        'comigo': 'com eu',
        'contigo': 'com tu',
        'consigo': 'com tu',
        'conosco': 'com nós',
        'convosco': 'com vós',
    }

    verbose = 0

    def __init__(cls, verbose=0, wout_bpe=False):
        cls.verbose = verbose
        cls.cogroo = Cogroo.instance()
        cls.orthography = Orthography(wout_bpe=wout_bpe)

    def _verbo(self, tag):

        is_verb = True
        if tag[1].startswith('HV'):
            tag[0] = 'haver'
            return tag, is_verb
        elif tag[1].startswith('ET'):
            tag[0] = 'estar'
            return tag, is_verb
        elif tag[1].startswith('TR'):
            tag[0] = 'ter'
            return tag, is_verb
        elif tag[1].startswith('SR'):  # and\
                # not tag[1].endswith(self.vbs['SR']):

            if not tag[0].startswith('f'):
                tag[0] = 'ser'
            # ser / ir
            else:
                tag[0] = self.lemmatize(tag[0])

            return tag, is_verb
        # VB
        else:

            lemma = self.lemmatize(tag[0])

            # successful or did not make difference
            if lemma.endswith('r') or tag[0] == lemma:
                tag[0] = lemma
                return tag, is_verb

            # failed to lemmatize
            is_verb = False
            return tag, is_verb

    def _special_case(self, tag):

        # ções -> ção; ços|çaís -> ço|çaí
        is_special_case = True

        if 'ç' in tag[0][-4:]:

            if tag[0].endswith('ões'):
                tag[0] = tag[0][:-3] + 'ão'
            elif tag[0].endswith('s'):
                tag[0] = tag[0][:-1]
            else:
                is_special_case = False

        elif 'mento' in tag[0][-6:]:
            if tag[0].endswith('s'):
                tag[0] = tag[0][:-1]

        elif 'dor' in tag[0][-5:]:
            sufixes = ['dores', 'doras', 'dora', 'dor']

            for sufix in sufixes:
                radical = tag[0].replace(sufix, '')
                # Fix for adoras, dor, dores, adora
                if len(radical) > 1:
                    if tag[0].endswith(sufix):
                        tag[0] = tag[0][:-len(sufix)] + 'dor'

        elif tag[0] == 'quaisquer':
            tag[0] = 'qualquer'

        elif tag[0] == 'quanta':
            tag[0] = 'quanto'

        else:
            is_special_case = False

        return tag, is_special_case

    def _contracao(self, tag):
        is_contracao = True

        if tag[0] == 'dalém':
            tag[0] = 'além'

        elif tag[0] in ['donde', 'aonde', 'daonde', 'donde']:
            tag[0] = 'onde'

        elif tag[0] in ['ao', 'aos', 'à', 'às']:
            tag[0] = ''

        elif tag[0].startswith('co'):
            if tag[0] in self.object_pronouns:
                tag[0] = self.object_pronouns[tag[0]]

        elif tag[1].startswith('P+'):
            tag[0] = self.lemmatize(tag[0]).split()[-1]
        else:
            is_contracao = False

        return tag, is_contracao

    def _artigo(self, tag):

        is_artigo = False
        if tag[0] in ['o', 'os', 'a', 'as']:
            tag[0] = ''
            is_artigo = True

        return tag, is_artigo

    def _pronome_possessivo(self, tag):
        is_pronome_possessivo = False

        if tag[1].startswith('PRO$'):
            is_pronome_possessivo = True

            if 'F' in tag[1] and tag[0] in self.poss_pro_f:
                tag[0] = self.poss_pro_f[tag[0]]

            plural = tag[0].endswith('s')
            tag[0] = self.lemmatize(tag[0])

            if plural and not tag[0].endswith('s'):
                tag[0] += 's'

        return tag, is_pronome_possessivo

    def _determiner(self, tag):
        is_determiner = True

        if self._artigo(tag)[1]:
            return tag, is_determiner

        elif tag[1].startswith('D'):
            if tag[1].startswith('D-UM') or\
                    tag[0] in ['um', 'uns', 'uma', 'umas']:
                tag[0] = ''
                return tag, is_determiner

            plural = tag[0].endswith('s')
            tag[0] = self.lemmatize(tag[0])

            if plural and not tag[0].endswith('s'):
                tag[0] += 's'
        else:
            is_determiner = False

        return tag, is_determiner

    def _preposicao(self, tag):
        is_preposicao = False

        if tag[1] == 'P':
            if tag[0] in ['em', 'de']:
                tag[0] = ''
                is_preposicao = True

        return tag, is_preposicao

    def _conjuncao(self, tag):
        is_conjuncao = False

        if tag[1].startswith('CONJ'):
            if tag[0] == 'e':
                tag[0] = ''
                is_conjuncao = True

        return tag, is_conjuncao

    # feitas -> feito; abraçados -> abraçado
    def _participio_passado(self, tag):
        is_participio_passado = False

        if tag[1].startswith('VB-AN'):
            is_participio_passado = True

            if tag[0].endswith('s'):
                tag[0] = tag[0][:-1]
            if tag[0].endswith('a'):
                tag[0] = tag[0][:-1] + 'o'

        return tag, is_participio_passado

    def lemmatize_aelius_tag(self, tag):

        if tag[1] == 'WL':
            return tag

        if self._special_case(tag)[1]:
            # is_special_case -> return processed tag
            return tag

        if self._conjuncao(tag)[1]:
            return tag

        if self._pronome_possessivo(tag)[1]:
            return tag

        # contração may result in preposição or determiner
        self._contracao(tag)

        if self._preposicao(tag)[1]:
            return tag

        if self._determiner(tag)[1]:
            return tag

        if self._verbo(tag)[1]:
            return tag

        # Default
        if 'N-P' == tag[1] or\
                tag[1] == 'NUM-F' or\
                tag[1].startswith('ADJ') or\
                tag[1].startswith('OUTRO') or\
                tag[1].startswith('WPRO') or\
                tag[1].startswith('WD') or\
                tag[1].startswith('Q'):

            # nas -> 'em o'
            if not tag[1].startswith('P+'):
                # print(f'{[now()]} formatting {tag[0]} -> {self.lemmatize(tag[0])}')
                tag[0] = self.lemmatize(tag[0])

        return tag

    def lemmatize(self, word):
        for prefix in self.prefixes:
            if word.startswith(prefix):

                lemma = self.lemmatize_cogroo(word)
                prefix_lemma = self.lemmatize_cogroo(prefix)
                resulting_lemma = ''

                # RECOVERING PREFIX
                # fix for: 'pré-oral' -> 'pré - oral'
                if lemma.startswith(prefix_lemma):
                    resulting_lemma = re.sub(r'^' + prefix_lemma + r'\s?', prefix, lemma)

                # fix for: 'desligar' -> 'ligar'
                elif not lemma.startswith(prefix):
                    resulting_lemma = prefix + lemma

                # fix for wrong lemmas: indo -> inir
                if resulting_lemma and self.orthography.check(resulting_lemma):
                    return resulting_lemma

                return lemma

        return self.lemmatize_cogroo(word)

    def lemmatize_sentence(self, sentence):

        lemmas = []

        for word in sentence.split():
            lemmas.append(self.lemmatize(word))

        return ' '.join(lemmas)

    def lemmatize_cogroo(self, word):
        # with timeout(10, exception=TimeoutError):
        if self.verbose > 2:
            print(f'{[now()]} Sending command to server for lemmatizing. Word:', word)

        word_lemma = self.cogroo.lemmatize(word)

        if self.verbose > 2:
            print(f'{[now()]} Received output from server. Lemma:', word_lemma)

        return word_lemma

    # lemmatize using only cogroo
    def lemmatize_sentence_cogroo(self, sentence):

        lemmas = []

        for word in sentence.split():
            lemmas.append(self.cogroo.lemmatize(word))

        return ' '.join(lemmas)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phrase', help='Phrases.')
    parser.add_argument('-c', '--cogroo', action='store_true', help='Use only cogroo for lemmatizing.')
    parser.add_argument('-a', '--aelius', action='store_true', help='Lemmatize Aelius tag.')
    args, _ = parser.parse_known_args()

    if args.aelius:
        word = args.phrase.split()[-1]
        print(Lemma().lemmatize_aelius_tag([word, args.tag]))
    elif args.cogroo:
        print(Lemma().lemmatize_cogroo(args.phrase))
    else:
        print(Lemma().lemmatize_sentence(args.phrase))


if __name__ == '__main__':
    main()
