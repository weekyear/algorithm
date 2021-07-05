def solution(nums):
    visited = [0] * 200001
    kind_num = 0

    for num in nums:
        if not visited[num]:
            visited[num] = 1
            kind_num += 1

    answer = min(len(nums) // 2, kind_num)
    return answer

# 더 좋은 방법
def solution_2(nums):
    return min(len(nums) // 2, len(set(nums)))