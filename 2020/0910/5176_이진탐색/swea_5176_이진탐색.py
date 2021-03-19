import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def inorder(v):
    global c
    if v <= N:
        inorder(2*v)
        bst[v] = c
        c += 1
        inorder(2*v+1)

for tc in range(T):
    N = int(input())
    bst = [0] * (N + 1)

    c = 1
    inorder(1)

    print('#{} {} {}'.format(tc+1, bst[1], bst[N // 2]))