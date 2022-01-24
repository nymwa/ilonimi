import re

class ProperChecker:

    def __init__(self):
        self.pattern = re.compile(r'^([AIUEO]|[KSNPML][aiueo]|[TJ][aueo]|W[aie])n?(([ksnpml][aiueo]|[tj][aueo]|w[aie])n?)*$')

    def __call__(self, x):
        return self.pattern.match(x) and ('nm' not in x) and ('nn' not in x)


class ProperSplitter:

    def __init__(self):
        self.pattern = re.compile(r'[AIUEO]n?|[KSNPMLksnpml][aiueo]n?|[TJtj][aueo]n?|[Ww][aie]n?')

    def __call__(self, x):
        return self.pattern.findall(x)

