kana_dict = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'si': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'ti': 'てぃ', 'tu': 'とぅ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ja': 'や', 'ji': 'い', 'ju': 'ゆ', 'je': 'いぇ', 'jo': 'よ',
    'ya': 'や', 'yi': 'い', 'yu': 'ゆ', 'ye': 'いぇ', 'yo': 'よ',
    'la': 'ら', 'li': 'り', 'lu': 'る', 'le': 'れ', 'lo': 'ろ',
    'wa': 'わ', 'wi': 'うぃ', 'wu': 'う', 'we': 'うぇ', 'wo': 'うぉ',
    'n': 'ん',
    'nja': 'にゃ', 'nji': 'に', 'nju': 'にゅ', 'nje': 'にぇ', 'njo': 'にょ',
    'nya': 'にゃ', 'nyi': 'に', 'nyu': 'にゅ', 'nye': 'にぇ', 'nyo': 'にょ'}


def split_kana(buf, palatalize):
    char_list = list(buf)
    char_list.append('EOS')
    state = 0
    kana_list = []
    tmp = ''

    for index, char in enumerate(char_list):

        if state == 0:

            if char in 'klmpsjytw':
                state, tmp = 1, char
            elif char in 'aouei':
                kana_list.append(kana_dict[char])
                state, tmp = 0, ''
            elif char == 'n':
                state, tmp = 2, char
            elif char == 'EOS':
                assert tmp == ''
                state, tmp = 4, ''
            else:
                state, tmp = 4, char

        elif state == 1:

            if char in 'aouei':
                kana_list.append(kana_dict[tmp + char])
                state, tmp = 0, ''
            elif char == 'EOS':
                assert tmp == ''
                state, tmp = 4, ''
            else:
                state, tmp = 4, char

        elif state == 2:

            if char in 'klmnpstw' or ((char in 'jy') and (not palatalize)):
                kana_list.append(kana_dict[tmp])
                state, tmp = 1, char
            elif char in 'aouei':
                kana_list.append(kana_dict[tmp + char])
                state, tmp = 0, ''
            elif (char in 'jy') and palatalize:
                state, tmp = 3, tmp + char
            elif char == 'EOS':
                assert tmp == 'n'
                kana_list.append(kana_dict[tmp])
                state, tmp = 0, ''
            else:
                assert tmp == 'n'
                kana_list.append(kana_dict[tmp])
                state, tmp = 4, char

        elif state == 3:

            if char in 'aoeui':
                kana_list.append(kana_dict[tmp + char])
                state, tmp = 0, ''
            elif char == 'EOS':
                assert False
            else:
                assert False

        elif state == 4:
            assert False

        else:
            assert False

    return ''.join(kana_list)

