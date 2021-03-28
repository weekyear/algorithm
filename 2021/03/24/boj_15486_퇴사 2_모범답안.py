import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    dp = [0]*(N+1)

    mx = 0
    for i in range(N):
        t, p = map(int, input().split())
        mx = max(mx, dp[i])

        if i+t > N:
            continue

        if dp[i+t] < p+mx:
            dp[i+t] = p + mx
        # dp[i+t] = max(mx+p, dp[i+t])

    print(max(dp))