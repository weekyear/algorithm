import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(s, e):
    if e - s < 2:
        return

    mid = (s + e) >> 1
    merge_sort(s, mid)
    merge_sort(mid, e)

    if nums[mid - 1] > nums[e - 1]:
        global count
        count += 1

    i, j, k = s, mid, s
    while i < mid and j < e:
        if nums[i] < nums[j]:
            tmp[k] = nums[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = nums[j]
            j, k = j + 1, k + 1

    while i < mid:
        tmp[k] = nums[i]
        i, k = i + 1, k + 1

    while j < e:
        tmp[k] = nums[j]
        j, k = j + 1, k + 1

    for t in range(s, e):
        nums[t] = tmp[t]

T = int(input())

for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    tmp = [0 for _ in range(N)]
    count = 0

    merge_sort(0, N)
    print('#{} {} {}'.format(tc + 1, nums[N >> 1], count))
    print(nums)