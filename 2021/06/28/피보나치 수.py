def solution(N):
    dp = [0, 1]
    for n in range(2, N + 1):
        dp.append(dp[n - 1] + dp[n - 2])

    return dp[N] % 1234567