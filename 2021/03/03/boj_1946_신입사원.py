import sys

sys.stdin = open('input_1946.txt', 'r')

for _ in range(int(input())):
    N = int(input())
    recruits = [list(map(int, input().split())) for _ in range(N)]

    recruits.sort()

    result = 0
    best_interview_rank = N + 1

    for i in range(N):
        if recruits[i][1] < best_interview_rank:
            result += 1
            best_interview_rank = recruits[i][1]

    print(result)
