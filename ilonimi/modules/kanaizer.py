from ilonimi.vocab.vocabulary import Vocabulary
from .proper import ProperChecker
from .split_kana import split_kana
import re

punct_dict = {
    ' ': '　',
    '!': '！',
    '#': '＃',
    '$': '＄',
    '%': '％',
    '&': '＆',
    '(': '（',
    ')': '）',
    '*': '＊',
    '+': '＋',
    ',': '、',
    '-': 'ー',
    '.': '。',
    '/': '／',
    '\\': '＼',
    ':': '：',
    ';': '；',
    '<': '＜',
    '=': '＝',
    '>': '＞',
    '?': '？',
    '@': '＠',
    '[': '［',
    ']': '］',
    '^': '＾',
    '_': '＿',
    '`': '｀',
    '{': '｛',
    '|': '｜',
    '}': '｝',
    '~': '〜'}


number_dict = {
    '0': '０',
    '1': '１',
    '2': '２',
    '3': '３',
    '4': '４',
    '5': '５',
    '6': '６',
    '7': '７',
    '8': '８',
    '9': '９'}


class Kanaizer:

    def __init__(self, link, palatalize, no_comma, space_period, space_colon):
        self.link = link
        self.palatalize = palatalize
        self.no_comma = no_comma
        self.space_period = space_period
        self.space_colon = space_colon

        self.vocab = Vocabulary()
        self.proper_checker = ProperChecker()
        self.quot_pattern1 = re.compile(r'"([^"]*)"')
        self.quot_pattern2 = re.compile(r'\'([^\']*)\'')

    def split_kana(self, word):
        return split_kana(word, self.palatalize)

    def kanaize_no_link(self, sent):
        output = ''

        for word in sent:
            if word in self.vocab.word_set:
                output = output + self.split_kana(word)
            elif word in punct_dict:
                output = output + punct_dict[word]
            elif word.isdecimal():
                output = output + ''.join([number_dict[num] for num in word])
            elif self.proper_checker(word):
                output = output + self.split_kana(word.lower())
            else:
                output = output + word

        return output

    def kanaize_link(self, sent):
        output = ''
        buf = ''

        for word in sent:
            if word in self.vocab.word_set:
                buf = buf + word
            elif word in punct_dict:
                output = output + ''.join(self.split_kana(list(buf)))
                output = output + punct_dict[word]
                buf = ''
            elif word.isdecimal():
                output = output + ''.join(self.split_kana(list(buf)))
                output = output + ''.join([number_dict[num] for num in word])
                buf = ''
            elif self.proper_checker(word):
                 buf = buf + word.lower()
            else:
                output = output + ''.join(self.split_kana(list(buf)))
                output = output + word
                buf = ''

        if buf != '':
            output = output + ''.join(self.split_kana(list(buf)))

        return output

    def __call__(self, sent):
        sent = sent.split()

        if self.link:
            output = self.kanaize_link(sent)
        else:
            output = self.kanaize_no_link(sent)

        output = self.quot_pattern1.sub('「\\1」', output)
        output = self.quot_pattern2.sub('「\\1」', output)

        if self.no_comma:
            output = output.replace('、', '')

        if self.space_period:
            output = output.replace('。', '　').strip()

        if self.space_colon:
            output = output.replace('：', '　').strip()

        return output

