import re

class Normalizer:
    def __init__(self):
        self.split_punct_pattern = re.compile(r'[^ !",.:?]+|[!",.:?]')
        self.conv_table = str.maketrans({
            '“': '"',
            '„': '"',
            '”': '"'})

    def __call__(self, x):
        x = x.translate(self.conv_table)
        x = self.split_punct_pattern.findall(x)
        x = ' '.join(x)
        return x

