import sys
sys.stdin = open('boj_2503.txt', 'r')

from itertools import permutations

N = int(input())
pitchings = [list(map(int, input().split())) for _ in range(N)]
result = 0
kinds_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = list(permutations(kinds_of_num, 3))

for n in range(len(nums)):
    num = nums[n]
    isRight = False
    for pitching in pitchings:
        pitch, num_strikes, num_balls = pitching

        if num[0] == 1 and num[1] == 3 and num[2] == 4:
            a = 1

        real_strike = 0
        real_ball = 0
        first_num = pitch // 100
        second_num = (pitch - first_num * 100) // 10
        third_num = pitch - second_num * 10 - first_num * 100

        for k in range(3):
            if real_strike > num_strikes or real_ball > num_balls:
                break

            if num[k] == first_num:
                if k == 0:
                    real_strike += 1
                else:
                    real_ball += 1
                continue

            if num[k] == second_num:
                if k == 1:
                    real_strike += 1
                else:
                    real_ball += 1
                continue

            if num[k] == third_num:
                if k == 2:
                    real_strike += 1
                else:
                    real_ball += 1

        if real_strike == num_strikes and real_ball == num_balls:
            isRight = True
        else:
            isRight = False
            break

    if isRight:
        result += 1
print(result)