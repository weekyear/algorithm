import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for m in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for n in range(N, 0, -1):
        if n > L:
            tree[n // 2] += tree[n]
        else:
            break

    print('#{} {}'.format(tc+1, tree[L]))