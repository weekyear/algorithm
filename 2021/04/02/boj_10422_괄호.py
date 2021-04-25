import sys
sys.stdin = open('boj_10422.txt', 'r')

dp = [0 for _ in range(5001)]
dp[0] = 1

for i in range(2, 5001, 2):
    for k in range(2, i + 1, 2):
        dp[i] += dp[k - 2] * dp[i - k]
    dp[i] %= 1000000007

for _ in range(int(input())):
    print(dp[int(input())])