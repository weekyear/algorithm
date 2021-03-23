import sys
sys.stdin = open('boj_11726.txt', 'r')

N = int(input())
cache = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[N] % 10007)