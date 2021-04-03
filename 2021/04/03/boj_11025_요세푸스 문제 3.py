import sys
sys.stdin = open('boj_11025.txt', 'r')

# f(n) = ((f(n-1) + k - 1) % n) + 1

N, K = map(int, input().split())

# dp = [0 for _ in range(N + 1)]
# dp[1] = 1
#
# for n in range(2, N + 1):
#     dp[n] = ((dp[n - 1] + K - 1) % n) + 1
#
# print(dp[N])

P = 0
for n in range(1, N + 1):
    P = (P + K) % n

print(P + 1)