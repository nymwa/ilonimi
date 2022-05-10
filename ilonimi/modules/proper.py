import re

class ProperChecker:

    def __init__(self):
        self.pattern = re.compile(r'^([AIUEO]|[KSNPML][aiueo]|[TJ][aueo]|W[aie])n?(([ksnpml][aiueo]|[tj][aueo]|w[aie])n?)*$')

    def __call__(self, x):
        return self.pattern.match(x) and ('nm' not in x) and ('nn' not in x)


def split_proper(word):

    word = word.lower() + '$'
    state = 0

    lst = []
    tmp = ''

    for index, char in enumerate(word):

        if state == 0:

            if char in 'klmnpsjtw':
                state, tmp = 1, tmp + char
            elif char in 'aouei':
                state, tmp = 2, tmp + char
            elif char == '$':
                if tmp != '':
                    lst.append(tmp)
                state, tmp = 4, ''
            else:
                if tmp != '':
                    lst.append(tmp)
                state, tmp = 0, char

        elif state == 1:

            if char in 'aouei':
                state, tmp = 2, tmp + char
            elif char == '$':
                if tmp != '':
                    lst.append(tmp)
                state, tmp = 4, ''
            else:
                if tmp != '':
                    lst.append(tmp)
                state, tmp = 0, char

        elif state == 2:

            if char in 'klmpsjtw':
                lst.append(tmp)
                state, tmp = 1, char
            elif char == 'n':
                state = 3
            elif char == '$':
                if tmp != '':
                    lst.append(tmp)
                state = 4
            else:
                if tmp != '':
                    lst.append(tmp)
                state, tmp = 0, char

        elif state == 3:

            if char in 'klmnpsjtw':
                lst.append(tmp + 'n')
                state, tmp = 1, char
            elif char in 'aouei':
                lst.append(tmp)
                state, tmp = 2, 'n' + char
            elif char == '$':
                lst.append(tmp + 'n')
                state, tmp = 4, ''
            else:
                if tmp != '':
                    lst.append(tmp)
                state, tmp = 0, char

        elif state == 4:
            assert False

        else:
            assert False

    return lst

