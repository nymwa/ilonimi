import sys
from argparse import ArgumentParser
from .normalizer import Normalizer
from .tokenizer import Tokenizer

def main():
    parser = ArgumentParser()
    parser.add_argument('--convert-number', action = 'store_true')
    parser.add_argument('--convert-proper', action = 'store_true')
    args = parser.parse_args()

    normalizer = Normalizer()
    tokenizer = Tokenizer(convert_number = args.convert_number, convert_proper = args.convert_proper)

    for x in sys.stdin:
        x = x.strip()
        x = normalizer(x)
        x = tokenizer(x)
        print(x)

