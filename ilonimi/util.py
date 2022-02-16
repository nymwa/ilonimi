from .modules.normalizer import Normalizer
from .modules.tokenizer import Tokenizer
from .modules.splitter import Splitter

def tunimi_common_args(parser):
    parser.add_argument('--no-tokenize', action = 'store_true')
    parser.add_argument('--no-normalize', action = 'store_true')
    parser.add_argument('--no-sharp', action = 'store_true')
    parser.add_argument('--convert-unk', action = 'store_true')
    parser.add_argument('--convert-number', action = 'store_true')
    parser.add_argument('--convert-proper', action = 'store_true')
    parser.add_argument('--split', action = 'store_true')


def preproc(normalizer, tokenizer, splitter, x):
    x = x.strip()

    if normalizer is not None:
        x = normalizer(x)

    if tokenizer is not None:
        x = tokenizer(x)

    if splitter is not None:
        x = splitter(x)

    return x


def tunimi_common_func(args, run_func):

    if not args.no_normalize:
        normalizer = Normalizer()
    else:
        normalizer = None

    if not args.no_tokenize:
        tokenizer = Tokenizer(
                convert_unk = args.convert_unk,
                convert_number = args.convert_number,
                convert_proper = args.convert_proper)
    else:
        tokenizer = None

    if args.split:
        splitter = Splitter(sharp = not args.no_sharp)
    else:
        splitter = None

    run_func(args, normalizer, tokenizer, splitter)


def tunimi_common_main(run_func, args):
    try:
        tunimi_common_func(args, run_func)
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

