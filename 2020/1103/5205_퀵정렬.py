import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def partition(l, r):
    x = nums[r]
    i = l - 1

    for j in range(l, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

def quick_sort(l, r):
    if l > r: return

    p = partition(l, r)

    quick_sort(l, p - 1)
    quick_sort(p + 1, r)

for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(0, N - 1)
    print('#{} {}'.format(tc + 1, nums[N // 2]))