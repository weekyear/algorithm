import sys
sys.stdin = open('boj_1911.txt', 'r')

import math

N, L = map(int, input().split())
waters = [list(map(int, input().split())) for _ in range(N)]
waters.sort(key=lambda w: w[0])

cur = 0
result = 0

for S, E in waters:
    S = max(S, cur + 1)
    if E < S:
        continue
    board = math.ceil((E - S) / L)
    cur = S + board * L - 1
    result += board

print(result)
