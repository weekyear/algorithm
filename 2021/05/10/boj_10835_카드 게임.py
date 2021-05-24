import sys
sys.stdin = open('boj_10835.txt', 'r')

N = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]
left = list(map(int, input().split()))
right = list(map(int, input().split()))

for r in range(N - 1, -1, -1):
    for l in range(N - 1, -1, -1):
        if left[l] > right[r]:
            dp[l][r] = dp[l][r+1] + right[r]
        else:
            dp[l][r] = max(dp[l+1][r+1], dp[l+1][r])

print(dp[0][0])