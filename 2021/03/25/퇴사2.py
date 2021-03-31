import sys
sys.stdin = open('boj_15486.txt', 'r')

N = int(input())
consults = [list(map(int, sys.stdin.readline().split())) for _ in range(N + 1)]
cache = [0 for consult in consults]

max_res = 0
for c in range(N + 1):
    if c < N:
        T, P = consults[c]

    if c + T < N:
        cache[c + T] = max(cache[c + T], cache[c] + P, max_res + P)

    if max_res < cache[c]:
        max_res = cache[c]

print(max_res)