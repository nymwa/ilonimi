import sys
from .modules.normalizer import Normalizer
from .modules.tokenizer import Tokenizer
from .modules.kanaizer import Kanaizer

def kana_args(first):
    parser = first.add_parser('kana', description = 'Toki Pona Kanaization')
    parser.add_argument(
            '--no-link',
            action = 'store_true',
            help = 'without linking (e.g. ろなら -> ろんあら)')
    parser.add_argument(
            '--no-palatalize',
            action = 'store_true',
            help = 'without palatalization (e.g. やんそにゃ -> やんそんや)')
    parser.add_argument(
            '--no-comma',
            action = 'store_true',
            help = 'delete 「、」')
    parser.add_argument(
            '--space-period',
            action = 'store_true',
            help = 'replace 「。」 to 「　」')
    parser.add_argument(
            '--space-colon',
            action = 'store_true',
            help = 'replace 「：」 to 「　」')
    parser.set_defaults(handler = kana_main)


def kana(link, palatalize, no_comma, space_period, space_colon):
    normalizer = Normalizer()
    tokenizer = Tokenizer()
    kanaizer = Kanaizer(link, palatalize, no_comma, space_period, space_colon)

    for x in sys.stdin:
        x = normalizer(x)
        x = tokenizer(x)
        x = kanaizer(x)
        print(x)


def kana_main(args):
    try:
        kana(
            link = not args.no_link,
            palatalize = not args.no_palatalize,
            no_comma = args.no_comma,
            space_period = args.space_period,
            space_colon = args.space_colon)
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

