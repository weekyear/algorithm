import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def checkTripleletOrRun(card_list, idx):
    if card_list[idx] == 3:
        return True
    else:
        count = 0
        for i in range(10):
            if card_list[i] > 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False


for tc in range(T):
    cards = list(map(int, input().split()))
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]

    for c in range(len(cards)):
        if c % 2:
            player2[cards[c]] += 1

            if len(player2) > 2 and checkTripleletOrRun(player2, cards[c]):
                print('#{} {}'.format(tc+1, 2))
                break
        else:
            player1[cards[c]] += 1

            if len(player1) > 2 and checkTripleletOrRun(player1, cards[c]):
                print('#{} {}'.format(tc + 1, 1))
                break
    else:
        print('#{} {}'.format(tc + 1, 0))