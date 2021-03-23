import sys
sys.stdin = open('boj_9095.txt', 'r')

def dp(n):
    if n < 1:
        return 0

    if cache[n]: return cache[n]

    if n < 4:
        cache[n] = dp(n - 3) + dp(n - 2) + dp(n - 1) + 1
        return cache[n]

    cache[n] = dp(n - 3) + dp(n - 2) + dp(n - 1)
    return cache[n]

for _ in range(int(input())):
    N = int(input())
    cache = [0 for _ in range(N + 1)]

    print(dp(N))


