import sys
sys.stdin = open('boj_15486.txt', 'r')

N = int(input())
input = sys.stdin.readline
cache = [0] * (N + 1)

max_res = 0
for c in range(N + 1):
    if c < N:
        T, P = map(int, input().split())

    if max_res < cache[c]:
        max_res = cache[c]

    if c + T > N:
        continue

    if cache[c + T] < max_res + P:
        cache[c + T] = max_res + P

print(max_res)