import re

class SharpWordJoiner:

    def __init__(self):
        self.merge_pattern = re.compile(r' ##')

    def __call__(self, x):
        x = self.merge_pattern.sub('', x)
        return x


class NoSharpWordJoiner:

    def __call__(self, x):
        x = x.split()

        merged = x[0]
        for i in range(len(x) - 1):
            if x[i].isupper() and x[i+1].isupper():
                pass
            elif x[i].isnumeric() and x[i+1].isnumeric():
                pass
            else:
                merged += ' '
            merged += x[i+1]
        return merged


class Joiner:

    def __init__(self, no_sharp = False):
        if no_sharp:
            self.word_joiner = NoSharpWordJoiner()
        else:
            self.word_joiner = SharpWordJoiner()

    def upper_to_title(self, x):
        if x.isupper():
            x = x.lower().title()
        return x

    def __call__(self, x):
        if type(x) == list:
            x = ' '.join(x)
        x = x.strip()
        x = self.word_joiner(x)
        x = x.split()
        x = [self.upper_to_title(token) for token in x]
        x = ' '.join(x)
        return x

