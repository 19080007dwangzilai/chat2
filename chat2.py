def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker = 0
    viki_sticker = 0
    for line in lines:
        s = line.strip().split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '圖片':
                allen_sticker += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '圖片':
                viki_sticker += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen says', allen_word_count, 'words', ', and uploads', allen_sticker, 'pictures')
    print('Viki says', viki_word_count, 'words'', and uploads', viki_sticker, 'pictures')


def main():
    lines = read_file('-LINE-Viki.txt')
    convert(lines)


main()
