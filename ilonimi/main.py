from argparse import ArgumentParser
from .tunimi import tunimi_args
from .wannimi import wannimi_args


def main():
    parser = ArgumentParser()
    first = parser.add_subparsers()
    tunimi_args(first)
    wannimi_args(first)
    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

