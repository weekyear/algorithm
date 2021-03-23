import sys
sys.stdin = open('boj_2579.txt', 'r')

N = int(input())
stairs = [int(input()) for _ in range(N)]

cache = [[] for _ in range(N + 1)]

cache[0].append(0)
cache[1].append(stairs[0])

for i in range(2, N + 1):
    cache[i].append(max(cache[i - 2]) + stairs[i - 1])
    cache[i].append(cache[i - 1][0] + stairs[i - 1])

print(max(cache[N]))