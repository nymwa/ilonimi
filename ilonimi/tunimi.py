import sys
from .modules.normalizer import Normalizer
from .modules.tokenizer import Tokenizer
from .modules.splitter import Splitter

def tunimi_args(first):
    parser = first.add_parser('tu')
    parser.add_argument('--no-tokenize', action = 'store_true')
    parser.add_argument('--no-normalize', action = 'store_true')
    parser.add_argument('--no-sharp', action = 'store_true')
    parser.add_argument('--convert-unk', action = 'store_true')
    parser.add_argument('--convert-number', action = 'store_true')
    parser.add_argument('--convert-proper', action = 'store_true')
    parser.add_argument('--split', action = 'store_true')
    parser.set_defaults(handler = tunimi_main)


def tunimi(
        no_tokenize = False,
        no_normalize = False,
        no_sharp = False,
        convert_unk = False,
        convert_number = False,
        convert_proper = False,
        split = False):

    normalizer = Normalizer()
    tokenizer = Tokenizer(
            convert_unk = convert_unk,
            convert_number = convert_number,
            convert_proper = convert_proper)
    splitter = Splitter(sharp = not no_sharp)

    for x in sys.stdin:
        x = x.strip()

        if not no_normalize:
            x = normalizer(x)

        if not no_tokenize:
            x = tokenizer(x)

        if split:
            x = splitter(x)

        print(x)


def tunimi_main(args):
    try:
        tunimi(
            no_tokenize = args.no_tokenize,
            no_normalize = args.no_normalize,
            no_sharp = args.no_sharp,
            convert_unk = args.convert_unk,
            convert_number = args.convert_number,
            convert_proper = args.convert_proper,
            split = args.split)
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

