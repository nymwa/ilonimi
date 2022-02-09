import re

class Detokenizer:
    def __init__(self):
        self.punct_pattern = re.compile(r' ([!,.:?])')
        self.quot_pattern1 = re.compile(r'" ([^"]*) "')
        self.quot_pattern2 = re.compile(r'\' ([^\']*) \'')

    def __call__(self, x):
        if type(x) == list:
            x = ' '.join(x)
        x = x.strip()
        x = self.punct_pattern.sub('\\1', x)
        x = self.quot_pattern1.sub('"\\1"', x)
        x = self.quot_pattern2.sub('"\\1"', x)
        return x

