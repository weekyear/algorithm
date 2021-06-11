def countingSort(nums):
    max_num = max(nums)
    # 1. counting 배열을 생성하고 값을 증가시켜준다.
    counts = [0] * (max_num + 1)
    for num in nums:
        counts[num] += 1

    # 2. counting 배열을 누적합으로 바꿔준다.
    for c in range(1, len(counts)):
        counts[c] += counts[c - 1]

    # 3. counting 배열의 뒤에서 부터 앞으로 순회하면서 새로운 배열에 값을 쌓아간다.
    results = [0] * len(nums)
    for n in range(len(nums) - 1, -1, -1):
        results[counts[nums[n]] - 1] = nums[n]
        counts[nums[n]] -= 1

    return results

print(countingSort([5, 5, 3, 4, 19, 1, 0, 4, 1, 3, 0, 2, 4, 2, 3, 0]))