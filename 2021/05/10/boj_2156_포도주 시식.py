import sys
sys.stdin = open('boj_2156.txt', 'r')

N = int(input())
wines = [int(input()) for _ in range(N)]
dp = [0] * N

dp[0] = wines[0]
max_res = dp[0]

if N > 1:
    dp[1] = wines[0] + wines[1]
    max_res = dp[1] if dp[1] > max_res else max_res
else:
    if N > 2:
        dp[2] = max(wines[2] + wines[0], wines[2] + wines[1])
        max_res = dp[2] if dp[2] > max_res else max_res
    else:
        for i in range(3, N):
            dp[i] = wines[i] + max(dp[i - 2], wines[i - 1] + dp[i - 3], wines[i - 1] + dp[i - 4])
            max_res = max(dp[N - 1], dp[N - 2], dp[N - 3])

print(max_res)