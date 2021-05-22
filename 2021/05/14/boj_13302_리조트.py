import sys
sys.stdin = open('boj_13302.txt', 'r')

N, M = map(int, input().split())

holiday_check = [0] * (N + 1)
if M > 0:
    holidays = list(map(int, input().split()))
    for m in range(M):
        holiday_check[holidays[m]] = 1

dp = [[0xffffff] * (N + 1) for _ in range(N + 1)]

def dfs(day, coupon):
    if day > N:
        return 0

    if dp[day][coupon] == 0xffffff:
        if holiday_check[day]:
            dp[day][coupon] = dfs(day + 1, coupon)
        else:
            prices = [dfs(day + 1, coupon) + 10000,
                      dfs(day + 3, coupon + 1) + 25000,
                      dfs(day + 5, coupon + 2) + 37000]
            if coupon > 2:
                prices.append(dfs(day + 1, coupon - 3))
            dp[day][coupon] = min(prices)

    return dp[day][coupon]

print(dfs(1, 0))