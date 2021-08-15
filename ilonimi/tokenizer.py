from .vocabulary import Vocabulary
from .proper import ProperChecker

class Tokenizer:
    def __init__(self, vocab = None, convert_number = False, convert_proper = False):
        if vocab is None:
            self.vocab = Vocabulary()
        else:
            self.vocab = vocab

        self.convert_number = convert_number
        self.convert_proper = convert_proper

        self.proper_checker = ProperChecker()

    def convert(self, x):
        if x in self.vocab.token_set:
            return x
        elif x.isdecimal():
            if self.convert_number:
                return self.vocab.number
            else:
                return x
        elif self.proper_checker(x):
            if self.convert_proper:
                return self.vocab.proper
            else:
                return x
        else:
            return self.vocab.unk

    def __call__(self, x):
        x = x.split()
        x = [self.convert(token) for token in x]
        x = ' '.join(x)
        return x

