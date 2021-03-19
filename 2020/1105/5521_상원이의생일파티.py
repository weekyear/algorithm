import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    p_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    f_list = []
    res = 0
    for _ in range(M):
        a, b = map(int, input().split())
        p_list[b][a] = 1
        p_list[a][b] = 1

        if a == 1:
            f_list.append(b)
            res += 1
        elif b == 1:
            f_list.append(a)
            res += 1

    if f_list:
        f_list.sort()
        prev_f = f_list[0]

        for f in f_list:
            for p in range(prev_f + 1, N + 1):
                if p_list[f][p] == 1 and not p_list[1][p]:
                    res += 1
            prev_f = f

    print('#{} {}'.format(tc + 1, res))