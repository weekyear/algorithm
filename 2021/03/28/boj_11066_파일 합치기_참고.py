import sys
sys.stdin = open('boj_11066.txt', 'r')

n = int(input())

while n > 0:
    n -= 1
    K = int(input())
    file_list = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    sum = [0] * (K + 1)  # 첫번째부터 K번짹 까지의 파일크기합 한번 합칠때 추가비용
    for i in range(1, K + 1):  # i번째 파일까지의 합
        sum[i] = sum[i - 1] + file_list[i - 1]

    for x in range(1, K + 1):  # x만큼 더한 구간의 구하기
        for i in range(K - x):  # 시작위치 i에서 i+x까지 구간 잡아주기
            j = i + x
            dp[i][j] = 999999999999
            for k in range(i, j):  # 시작위치에서 x만큼 더한 위치의 구간을 k를 기준으로 나누어서 계산하여 최솟값을 구한다..
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum[j + 1] - sum[i])

    print(dp[0][K - 1])