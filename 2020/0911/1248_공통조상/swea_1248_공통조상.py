import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def cal_depth(n):
    if n == 0 : return 0
    l = cal_depth(L[n])
    r = cal_depth(R[n])

    return l + r + 1

for tc in range(T):
    V, E, a, b = map(int, input().split())

    L = [0] * (V+1)
    R = [0] * (V+1)
    P = [0] * (V+1)

    lca = 0
    lca_tree = 0

    input_data = list(map(int, input().split()))

    for e in range(0, 2 * E, 2):
        p, c = input_data[e], input_data[e+1]
        P[c] = p
        if not L[p]:
            L[p] = c
        else:
            R[p] = c

    ances_check = [0] * (V+1)
    n = a

    while n != 1:
        ances_check[P[n]] = 1
        n = P[n]

    m = b
    while not ances_check[P[m]]:
        m = P[m]

    lca = P[m]

    print('#{} {} {}'.format(tc+1, lca, cal_depth(lca)))