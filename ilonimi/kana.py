import sys
from .modules.normalizer import Normalizer
from .modules.tokenizer import Tokenizer
from .modules.kanaizer import Kanaizer


def kana_args(first):
    parser = first.add_parser('kana', description = 'Toki Pona Kanaization')

    parser.add_argument(
            '--link',
            action = 'store_true',
            help = 'kanaize with linking (e.g. ろんあら -> ろなら)')

    parser.add_argument(
            '--palatalize',
            action = 'store_true',
            help = 'kanaize with palatalization (e.g. やんそんや -> やんそにゃ)')

    parser.add_argument(
            '--comma-as',
            type = str,
            default = '、',
            help = 'Comma "," is converted into the designated string. Default: 「、」')

    parser.add_argument(
            '--period-as',
            type = str,
            default = '。',
            help = 'Period "." is converted into the designated string. Default: 「。」')

    parser.add_argument(
            '--colon-as',
            type = str,
            default = '：',
            help = 'Colon ":" is converted into the designated string. Default: 「：」')

    parser.set_defaults(handler = kana_main)


def kana(
        link,
        palatalize,
        comma_as,
        period_as,
        colon_as):

    normalizer = Normalizer()
    tokenizer = Tokenizer()
    kanaizer = Kanaizer(
            link,
            palatalize, 
            comma_as,
            period_as,
            colon_as)

    for x in sys.stdin:
        x = normalizer(x)
        x = tokenizer(x)
        x = kanaizer(x)
        print(x)


def kana_main(args):
    try:
        kana(
            link = args.link,
            palatalize = args.palatalize,
            comma_as = args.comma_as,
            period_as = args.period_as,
            colon_as = args.colon_as)
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

