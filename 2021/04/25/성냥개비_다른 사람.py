import sys

sys.stdin = open('내꺼.txt', 'r')

max_dp = [0] * 101
max_dp[2] = 1
max_dp[3] = 7
num = [0, 0, 1, 7, 4, 2, 0, 8, 10]
for i in range(4, 101):
    max_dp[i] = max_dp[i - 2] * 10 + 1
min_dp = [0, 0, 1, 7, 4, 2, 6, 8, 10] + [0] * 92
for i in range(9, 101):
    min_dp[i] = min(min_dp[i - 2] * 10 + num[2], min_dp[i - 3] * 10 + num[3], min_dp[i - 4] * 10 + num[4], min_dp[i - 5] * 10 + num[5], min_dp[i - 6] * 10 + num[6], min_dp[i - 7] * 10 + num[7])
min_dp[6] = 6
i = 9

diff = []
for i in range(2, 101):
    other_min, other_max = min_dp[i], max_dp[i]
    my_min, my_max = map(int, input().split())
    if other_min != my_min or other_max != my_max:
        diff.append(i)
        print(i)