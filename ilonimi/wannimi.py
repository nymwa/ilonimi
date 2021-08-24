import re
import sys
from argparse import ArgumentParser
from .joiner import Joiner

class Detokenizer:
    def __init__(self):
        self.punct_pattern = re.compile(r' ([!,.:?])')
        self.quot_pattern = re.compile(r'" ([^"]*) "')

    def __call__(self, x):
        if type(x) == list:
            x = ' '.join(x)
        x = x.strip()
        x = self.punct_pattern.sub('\\1', x)
        x = self.quot_pattern.sub('"\\1"', x)
        return x


def main():
    parser = ArgumentParser()
    parser.add_argument('--merge-proper', action = 'store_true')
    args = parser.parse_args()

    joiner = Joiner()
    detokenizer = Detokenizer()

    for x in sys.stdin:
        if args.merge_proper:
            x = joiner(x)
        x = detokenizer(x)
        print(x)

