import sys

sys.stdin = open('boj_1543.txt', 'r')

N, M = input(), input()

if len(M) > len(N):
    print(0)
else:
    n = 0
    result = 0
    while n < len(N):
        for m in range(len(M)):
            if n + m >= len(N) or M[m] != N[m + n]:
                n += 1
                break
        else:
            n += len(M)
            result += 1

    print(result)