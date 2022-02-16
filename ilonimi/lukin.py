import sys
from collections import defaultdict
from .util import (
        tunimi_common_args,
        preproc,
        tunimi_common_main)

def lukin_args(first):
    parser = first.add_parser('lukin')
    tunimi_common_args(parser)
    parser.add_argument('--sort-by-freq', action = 'store_true')
    parser.set_defaults(handler = lukin_main)


def lukin(
        args,
        normalizer,
        tokenizer,
        splitter):

    dct = defaultdict(int)
    for sent in sys.stdin:
        sent = preproc(normalizer, tokenizer, splitter, sent)
        for word in sent.split():
            dct[word] += 1

    lst = list(dct.items())

    lst.sort()
    if args.sort_by_freq:
        lst.sort(key = lambda x: -x[1])

    for word, freq in lst:
        print('{}\t{}'.format(word, freq))


def lukin_main(args):
    tunimi_common_main(lukin, args)

