from argparse import ArgumentParser
from .tunimi import tunimi_args
from .wannimi import wannimi_args
from .lukin import lukin_args
from .ud import ud_args
from .kana import kana_args


def main():
    parser = ArgumentParser()
    first = parser.add_subparsers()

    tunimi_args(first)
    wannimi_args(first)
    lukin_args(first)
    ud_args(first)
    kana_args(first)

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

