import sys
from ilonimi.util import (
        tunimi_common_args,
        preproc,
        tunimi_common_main)

def template_args(second):
    parser = second.add_parser('template')
    tunimi_common_args(parser)
    parser.add_argument('--start', type = int, default = 1)
    parser.set_defaults(handler = template_main)


def run_template(
        args,
        normalizer,
        tokenizer,
        splitter):

    for sent_index, sent in enumerate(sys.stdin, start = args.start):

        sent = preproc(normalizer, tokenizer, splitter, sent)
        line = '# {}: {}'.format(
                sent_index,
                sent)
        print(line)

        for word_index, word in enumerate(sent.split()):

            line = '{}\t{}\tX\t0\tX'.format(
                    word_index,
                    word)
            print(line)

        print()


def template_main(args):
    tunimi_common_main(run_template, args)

