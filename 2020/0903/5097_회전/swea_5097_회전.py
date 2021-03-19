import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Q = input().split()

    p = M % N

    for _ in range(p):
        Q.append(Q.pop(0))

    print('#{} {}'.format(tc+1, Q[0]))