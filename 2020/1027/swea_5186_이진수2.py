import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    num = float(input())
    result_list = []
    indice = -1
    while len(result_list) < 13:
        if num > 2 ** indice:
            result_list.append('1')
            num -= 2 ** indice
        elif abs(num - 2 ** indice) < 0.00000000000001:
            result_list.append('1')
            print('#{} {}'.format(tc + 1, ''.join(result_list)))
            break
        else:
            result_list.append('0')

        indice -= 1
    else:
        print('#{} {}'.format(tc+1, 'overflow'))