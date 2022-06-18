from pathlib import Path

def load_tokipona_vocabulary():
    path = Path(__file__).parent / 'vocabulary.txt'
    with open(path) as f:
        lst = [x.strip() for x in f]
    return lst

punct_list_string = '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'

class Vocabulary(list):

    def __init__(self):
        self.unk = '<unk>'
        self.number = '<number>'
        self.proper = '<proper>'

        self.punctuation_list = list(punct_list_string)
        self.punctuation_set = set(self.punctuation_list)
        self.word_list = load_tokipona_vocabulary()
        self.token_list = self.punctuation_list + self.word_list
        super().__init__(self.token_list)
        self.word_set = set(self.word_list)
        self.token_set = set(self.token_list)

