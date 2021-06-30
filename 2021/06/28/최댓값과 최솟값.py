def solution(s):
    nums = list(map(int, s.split()))
    return ' '.join([str(min(nums)), str(max(nums))])