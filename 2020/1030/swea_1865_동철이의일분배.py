import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def solve(k, result):
    global max_val
    if k == N:
        max_val = max(max_val, result)
    else:
        for i in range(k, N):
            next_val = result * num_list[k][order[i]]
            if max_val < next_val:
                order[k], order[i] = order[i], order[k]
                solve(k + 1, next_val)
                order[k], order[i] = order[i], order[k]

for tc in range(T):
    N = int(input())
    num_list = []
    max_val = 1
    for _ in range(N):
        nums = list(map(lambda x: int(x)/100, input().split()))
        num_list.append(nums)

    # 탐욕 알고리즘으로 최적해 선정
    check_list = [0] * N
    for i in range(N):
        max_elem = 0
        idx = -1
        for j in range(N):
            if check_list[j] == 0 and num_list[i][j] > max_elem:
                max_elem = num_list[i][j]
                idx = j

        max_val *= max_elem
        check_list[idx] = 1

    order = [x for x in range(N)]
    solve(0, 1.0)

    print('#{} {}'.format(tc + 1, format(max_val*100, '.6f')))