import sys

def pos_args(second):
    parser = second.add_parser('pos')
    parser.set_defaults(handler = pos_main)


def parse_line(line):
    xs = line.split()
    assert len(xs) == 5
    dct = {
        'index': xs[0],
        'token': xs[1],
        'pos': xs[2],
        'head': xs[3],
        'dep': xs[4]}
    return dct


def run_pos():
    data = []
    sent = None

    for x in sys.stdin:
        x = x.strip()
        if x.startswith('#'):
            pass
        elif (sent is None) and (x != ''):
            sent = [parse_line(x)]
        elif (x != ''):
            sent.append(parse_line(x))
        elif (sent is not None):
            data.append(sent)
            sent = None

    for sent in data:
        x = [z['token'] for z in sent]
        y = [z['pos'] for z in sent]
        x = ' '.join(x)
        y = ' '.join(y)
        line = '{}\t{}'.format(x, y)
        print(line)


def pos_main(args):
    try:
        run_pos()
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

