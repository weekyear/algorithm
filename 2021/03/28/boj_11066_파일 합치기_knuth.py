import sys
sys.stdin = open('boj_11066.txt', 'r')
from sys import stdin

readline = stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, readline().split()))

    dp = [[0] * N for _ in range(N)]

    sums = [0] * (N + 1)
    for n in range(1, N + 1):
        sums[n] = sums[n - 1] + nums[n - 1]

    knuth = [[0] * N for _ in range(N)]
    for k in range(N):
        knuth[k][k] = k

    for gap in range(1, N + 1):
        for i in range(N - gap):
            j = i + gap
            dp[i][j] = 0xffffffffff
            for k in range(knuth[i][j-1], knuth[i + 1][j] + 1):
                if k >= N - 1:
                    break

                cur_val = dp[i][k] + dp[k + 1][j] + sums[j + 1] - sums[i]
                if dp[i][j] > cur_val:
                    dp[i][j] = cur_val
                    knuth[i][j] = k


    print(dp[0][N - 1])