import sys

sys.stdin = open('input.txt', 'r')

def inorder(v):
    if v != 0:
        inorder(L[v])
        print(W[v], end='')
        inorder(R[v])

for tc in range(10):
    N = int(input())
    G = {}
    W = [0] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)
    for n in range(1, N + 1):
        n_data = input().split()
        G[n] = n_data
        for i in range(1, len(n_data)):
            if i < 2:
                W[n] = n_data[i]
            else:
                c = int(n_data[i])
                P[c] = n
                if L[n] == 0:
                    L[n] = c
                else:
                    R[n] = c
    print('#{}'.format(tc+1), end=' ')
    inorder(1)
    print()