import sys
from .pos import pos_args
from .template import template_args

def ud_args(first):
    parser = first.add_parser('ud')
    second = parser.add_subparsers()
    pos_args(second)
    template_args(second)

