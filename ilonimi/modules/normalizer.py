import re

class Normalizer:
    def __init__(self):
        self.split_punct_pattern = re.compile(r'[^ !"\',.;:?()]+|[!"\',.;:?()]')
        self.conv_table = str.maketrans({
            '“': '"',
            '„': '"',
            '”': '"'})
        self.hyphen_pattern = re.compile(r'([^ ])-([^ ])')

    def __call__(self, x):
        x = x.translate(self.conv_table)
        x = self.split_punct_pattern.findall(x)
        x = ' '.join(x)
        x = self.hyphen_pattern.sub('\\1 - \\2', x)
        return x

