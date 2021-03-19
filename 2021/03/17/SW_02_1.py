import sys

sys.stdin = open('input_02.txt', 'r')


def explore():


for tc in range(int(input())):
    jongyangs = []
    N, M = map(int, input().split())

    max_n = 0

    for n in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        cur_max_n = max(x1, x2, y1, y2)
        if max_n < cur_max_n:
            max_n = cur_max_n

        jongyangs.append([[min(x1, x2), max(x1, x2)], [min(y1, y2), max(y1, y2)]])

    result = 0
    for k in range(1, max_n + 1):
        for y in range(max_n - k + 1):
            for x in range(max_n - k + 1):
                recur = 0
                max_j_x, max_j_y = x + k, y + k
                for j in jongyangs:
                    if x <= j[0][0] and j[0][1] <= max_j_x and y <= j[1][0] and j[1][1] <= max_j_y:
                        recur += 1

                    if recur >= N - M:
                        result = k
                        break

    print('#{} {}'.format(tc + 1, result))
