import sys
from argparse import ArgumentParser
from .normalizer import Normalizer
from .tokenizer import Tokenizer
from .splitter import Splitter

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--no-tokenize', action = 'store_true')
    parser.add_argument('--no-normalize', action = 'store_true')
    parser.add_argument('--convert-unk', action = 'store_true')
    parser.add_argument('--convert-number', action = 'store_true')
    parser.add_argument('--convert-proper', action = 'store_true')
    parser.add_argument('--split', action = 'store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    normalizer = Normalizer()
    tokenizer = Tokenizer(
            convert_unk = args.convert_unk,
            convert_number = args.convert_number,
            convert_proper = args.convert_proper)
    splitter = Splitter()

    for x in sys.stdin:
        x = x.strip()

        if not args.no_normalize:
            x = normalizer(x)

        if not args.no_tokenize:
            x = tokenizer(x)

        if args.split:
            x = splitter(x)

        print(x)

