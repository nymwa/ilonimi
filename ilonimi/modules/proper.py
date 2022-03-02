import re

class ProperChecker:

    def __init__(self):
        self.pattern = re.compile(r'^([AIUEO]|[KSNPML][aiueo]|[TJ][aueo]|W[aie])n?(([ksnpml][aiueo]|[tj][aueo]|w[aie])n?)*$')

    def __call__(self, x):
        return self.pattern.match(x) and ('nm' not in x) and ('nn' not in x)


class ProperSplitter:

    def __init__(self):
        pairs = [
            (' klmnps', 'aeiou'),
            ('jt', 'aeou'),
            ('w', 'aei')]
        syllables = [
            (c + v).strip()
            for cs, vs in pairs
            for c in cs
            for v in vs]
        self.pattern = re.compile(r'|'.join(['n?' + x[::-1] for x in syllables[::-1]]))

    def __call__(self, orig):
        lst = self.pattern.findall(orig.lower()[::-1])
        hyp = [syll[::-1] for syll in lst][::-1]
        return hyp

