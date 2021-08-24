from .proper import (
        ProperChecker,
        ProperSplitter)

class Splitter:

    def __init__(self):
        self.checker = ProperChecker()
        self.splitter = ProperSplitter()

    def split_number(self, x):
        if x.isdecimal():
            first = x[0]
            rest = ['##' + digit for digit in x[1:]]
            x = ' '.join([first] + rest)
        return x

    def split_proper(self, x):
        if self.checker(x):
            x = self.splitter(x)
            first = x[0].upper()
            rest = ['##' + token.upper() for token in x[1:]]
            x = ' '.join([first] + rest)
        return x

    def __call__(self, x):
        x = x.split()
        x = [self.split_number(token) for token in x]
        x = [self.split_proper(token) for token in x]
        x = ' '.join(x)
        return x
