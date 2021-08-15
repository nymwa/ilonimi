import re

class ProperChecker:
    def __init__(self):
        self.proper_pattern = re.compile(r'^([AIUEO]|[KSNPML][aiueo]|[TJ][aueo]|W[aie])n?(([ksnpml][aiueo]|[tj][aueo]|w[aie])n?)*$')

    def __call__(self, x):
        return self.proper_pattern.match(x) and ('nm' not in x) and ('nn' not in x)

