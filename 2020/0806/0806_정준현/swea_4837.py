import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    data = list(map(int, input().split()))
    N, K = data[0], data[1]
    n = 12

    for i in range(1<<n):
        my_comb = []
        for j in range(n):
            if i & (1<<j):
                my_comb.append(j+1)

        if len(my_comb) == N:
            _sum = 0
            for k in range(len(my_comb)):
                _sum += my_comb[k]
            if _sum == K:
                result += 1

    print('#{} {}'.format(test_case, result))