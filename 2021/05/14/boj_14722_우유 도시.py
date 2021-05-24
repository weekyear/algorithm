import sys

sys.stdin = open('boj_14722.txt', 'r')

import sys
readlines = sys.stdin.readline

N = int(readlines())

field = [list(map(int, readlines().split())) for _ in range(N)]
dp = [[[0, 0] for _ in range(N)] for _ in range(N)]

if field[0][0] == 0:
    dp[0][0][0], dp[0][0][1] = 1, 1
else:
    dp[0][0][0], dp[0][0][1] = 0, 0

for y in range(N):
    for x in range(N):
        up_val = dp[y - 1][x] if y > -1 else (-1, -1)
        left_val = dp[y][x - 1] if x > -1 else (-1, -1)
        up_new_val = up_val[:]
        left_new_val = left_val[:]
        if field[y][x] == up_val[1]:
            up_new_val = (up_val[0] + 1, (up_val[1] + 1) % 3)

        if field[y][x] == left_new_val[1]:
            left_new_val = (left_val[0] + 1, (left_val[1] + 1) % 3)

        dp[y][x] = max(up_new_val, left_new_val, key=lambda x: x[0])

print(dp[N - 1][N - 1][0])