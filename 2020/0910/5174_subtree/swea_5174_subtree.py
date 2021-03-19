import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def cal_depth(n):
    if n == 0 : return 0
    l = cal_depth(L[n])
    r = cal_depth(R[n])

    return l + r + 1

for tc in range(T):
    E, N = map(int, input().split())

    L = [0] * (E+2)
    R = [0] * (E+2)

    input_data = list(map(int, input().split()))

    for e in range(0, 2 * E, 2):
        p, c = input_data[e], input_data[e+1]
        if not L[p]:
            L[p] = c
        else:
            R[p] = c

    print('#{} {}'.format(tc+1, cal_depth(N)))