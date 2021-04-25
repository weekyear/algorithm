min_dp = [0] * 101
num = [0, 0, 1, 7, 4, 2, 0, 8, 10]
min_dp[2], min_dp[3], min_dp[4], min_dp[5], min_dp[6], min_dp[7], min_dp[8] = 1, 7, 4, 2, 6, 8, 10

# for i in range(9, 101):
#     min_dp[i] = min_dp[i - 2] * 10 + min_dp[2]
#     for j in range(3, 8):
#         min_dp[i] = min(min_dp[i], min_dp[i - j] * 10 + num[j])
for i in range(9, 101):
    min_dp[i] = min(min_dp[i - 2] * 10 + num[2], min_dp[i - 3] * 10 + num[3], min_dp[i - 4] * 10 + num[4], min_dp[i - 5] * 10 + num[5], min_dp[i - 6] * 10 + num[6], min_dp[i - 7] * 10 + num[7])

max_dp = [0] * 101
max_dp[2] = 1
max_dp[3] = 7
for i in range(4, 101):
    max_dp[i] = max_dp[i - 2] * 10 + 1

def solution(N):
    print('{} {}'.format(min_dp[N], max_dp[N]))

for i in range(2, 101):
    solution(i)