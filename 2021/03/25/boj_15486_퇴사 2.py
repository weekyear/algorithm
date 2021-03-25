import sys
sys.stdin = open('boj_15486.txt', 'r')

N = int(input())
consults = [list(map(int, sys.stdin.readline().split())) for _ in range(N + 1)]
cache = [0 for consult in consults]

for c in range(N):
    T, P = consults[c]

    if c + T < N + 1:
        cache[c + T] = max(cache[c + T], cache[c] + P)

    cache[c + 1] = max(cache[c + 1], cache[c])

print(cache[N])