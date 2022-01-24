import re

class Joiner:

    def __init__(self):
        self.merge_pattern = re.compile(r' ##')

    def upper_to_title(self, x):
        if x.isupper():
            x = x.lower().title()
        return x

    def __call__(self, x):
        if type(x) == list:
            x = ' '.join(x)
        x = x.strip()
        x = self.merge_pattern.sub('', x)
        x = x.split()
        x = [self.upper_to_title(token) for token in x]
        x = ' '.join(x)
        return x

