import sys

sys.stdin = open('kakao_01.txt', 'r')

for tc in range(4):
    s = input()

    char_to_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for key, val in char_to_num.items():
        s = s.replace(key, val)

    print(int(s))
