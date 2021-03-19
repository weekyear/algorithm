import sys
sys.stdin = open('input_5097.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())

    nums = list(map(int, input().split()))

    for m in range(M):
        nums.append(nums.pop(0))

    print('#{} {}'.format(tc + 1, nums[0]))