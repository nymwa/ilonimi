import sys
from .modules.joiner import Joiner
from .modules.detokenizer import Detokenizer

def wannimi_args(first):
    parser = first.add_parser('wan')
    parser.add_argument('--merge', action = 'store_true')
    parser.set_defaults(handler = wannimi_main)


def wannimi(merge = False):
    joiner = Joiner()
    detokenizer = Detokenizer()

    for x in sys.stdin:
        if merge:
            x = joiner(x)
        x = detokenizer(x)
        print(x)


def wannimi_main(args):
    try:
        wannimi(merge = args.merge)
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

