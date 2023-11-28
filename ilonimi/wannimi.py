import sys
from .modules.joiner import Joiner
from .modules.detokenizer import Detokenizer


def wannimi_args(first):
    parser = first.add_parser('wan', description = 'Toki Pona Detokenization')
    parser.add_argument(
            '--merge',
            action = 'store_true',
            help = 'merge split numbers and proper nouns')
    parser.add_argument(
            '--no-sharp',
            action = 'store_true',
            help = 'merge numbers and proper nouns without ## marks')
    parser.set_defaults(handler = wannimi_main)


def wannimi(merge = False, no_sharp = False):
    joiner = Joiner(no_sharp = no_sharp)

    detokenizer = Detokenizer()

    for x in sys.stdin:
        if merge:
            x = joiner(x)
        x = detokenizer(x)
        print(x)


def wannimi_main(args):
    try:
        wannimi(merge = args.merge, no_sharp = args.no_sharp)
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

