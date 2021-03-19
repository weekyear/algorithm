import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    data = input()

    l = len(data)
    cards = {'S': '', 'D': '', 'H': '', 'C': ''}
    for i in cards:
        cards[i] = [0 for _ in range(14)]

    num_cards = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    isError = False

    for i in range(0, l, 3):
        type = data[i]
        num = int(data[i+1:i+3])

        if not cards[type][num]:
            cards[type][num] = 1
            num_cards[type] -= 1
        else:
            isError = True
            break

    print('#{}'.format(tc+1), end=' ')
    if isError:
        print('ERROR')
    else:
        for c in num_cards.values():
            print(c, end=' ')
        print()