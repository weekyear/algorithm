def solution(n):
    answer = ''
    nums = ['4', '1', '2']
    while n:
        mod = n % 3
        answer = nums[mod] + answer
        if mod:
            n = n // 3
        else:
            n = n // 3 - 1
    return answer