import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def solve(N, lines):
    result = 99999
    for i in range(N - 2):
        fir_num = 0
        for k in range(i + 1):
            fir_num += lines[k][1] + lines[k][2]
        for k in range(i + 1, i + 2):
            fir_num += lines[k][0] + lines[k][2]
        for k in range(i + 2, N):
            fir_num += lines[k][0] + lines[k][1]

        if result > fir_num:
            result = fir_num

        for j in range(i + 2, N - 1):
            ch_num = fir_num
            ch_num -= lines[j-1][0] + lines[j-1][2]
            ch_num += lines[j][0] + lines[j][1]

            if result > ch_num:
                result = ch_num

    return result


for test_case in range(T):
    N, M = map(int, input().split())
    lines = []
    for _ in range(N):
        _data = input()
        line = (_data.count('W'), _data.count('B'), _data.count('R'))
        lines.append(line)

    print('#{} {}'.format(test_case + 1, solve(N, lines)))