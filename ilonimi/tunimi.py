import sys
from .util import (
        tunimi_common_args,
        preproc,
        tunimi_common_main)

def tunimi_args(first):
    parser = first.add_parser('tu')
    tunimi_common_args(parser)
    parser.set_defaults(handler = tunimi_main)


def tunimi(
        args,
        normalizer,
        tokenizer,
        splitter):

    for x in sys.stdin:
        x = preproc(normalizer, tokenizer, splitter, x)
        print(x)


def tunimi_main(args):
    tunimi_common_main(tunimi, args)

