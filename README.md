# ilotunimi

Toki Pona Tokenizer/Detokenizer

## how to use

### installation

```
pip install git+https://github.com/nymwa/ilonimi
```

### tokenization

```
nimi tu < text.txt > tokenized.txt

optional arguments:
  -h, --help        show this help message and exit
  --no-tokenize     without tokenization
  --no-normalize    without normalization
  --split           split decimal number by each number and proper noun by each syllable
  --no-sharp        without ## mark for splitted number and proper noun
  --convert-unk     convert unknown word into <proper>
  --convert-number  convert decimal number into <number>
  --convert-proper  convert proper noun into <proper>
```

### detokenization

```
nimi wan < tokenized.txt > detokenized.txt

optional arguments:
  -h, --help  show this help message and exit
  --merge     merge split numbers and proper nouns
  --no-sharp  merge numbers and proper nouns without ## marks
```

### kanaization

```
nimi kana < text.txt > kanaized.txt

optional arguments:
  -h, --help       show this help message and exit
  --no-link        without linking (e.g. ろなら -> ろんあら)
  --no-palatalize  without palatalization (e.g. やんそにゃ -> やんそんや)
  --no-comma       delete 「、」
  --space-period   replace 「。」 to 「　」
  --space-colon    replace 「：」 to 「　」
```

