import sys
sys.stdin = open('input_4008.txt', 'r')

def dfs(result, k):
    global max_result
    global min_result
    global operator_nums
    if k == N - 1:
        if max_result < result:
            max_result = result

        if min_result > result:
            min_result = result
        return

    for i in range(4):
        if operator_nums[i] > 0:
            operator_nums[i] -= 1
            if i == 0:
                dfs(result + nums[k + 1], k + 1)
            elif i == 1:
                dfs(result - nums[k + 1], k + 1)
            elif i == 2:
                dfs(result * nums[k + 1], k + 1)
            else:
                dfs(int(result / nums[k + 1]), k + 1)

            operator_nums[i] += 1

for tc in range(int(input())):
    N = int(input())

    operator_nums = list(map(int, input().split()))

    nums = list(map(int, input().split()))

    max_result = -0xffffff
    min_result = 0xffffff

    dfs(nums[0], 0)

    print('#{} {}'.format(tc + 1, max_result - min_result))