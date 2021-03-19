import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def p_set(k, _sum, check):
    global min_num
    if _sum < min_num:
        for i in range(N):
            if not check & 2 ** i:
                temp_sum = _sum + table[k][i]

                if k == N-1:
                    if temp_sum < min_num:
                        min_num = temp_sum
                else:
                    p_set(k+1, temp_sum, check + 2 ** i)

for tc in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    min_num = 999999999999999
    check = 0
    p_set(0, 0, check)

    print('#{} {}'.format(tc+1, min_num))