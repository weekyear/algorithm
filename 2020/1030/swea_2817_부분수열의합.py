import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    allSum = sum(nums)

    sums = []
    count = 0
    for num in nums:
        lenSums = len(sums)
        sums.append(num)
        if num == K:
            count += 1
        for s in range(lenSums):
            newSum = sums[s] + num
            if newSum < K:
                sums.append(newSum)
            elif newSum == K:
                count += 1

    print('#{} {}'.format(tc+1, count))