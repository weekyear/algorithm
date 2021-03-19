import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    schedule = []
    for _ in range(N):
        schedule.append(list(map(int, input().split())))

    for n in range(1, N):
        val = schedule[n][1]
        idx = n
        for i in range(n - 1, -1, -1):
            if schedule[i][1] > val:
                schedule[idx], schedule[i] = schedule[i], schedule[idx]
                idx -= 1

    real_schedule = []
    r = -1
    for time in schedule:
        if not real_schedule or time[0] >= real_schedule[r][1]:
            real_schedule.append(time)
            r += 1

    print('#{} {}'.format(tc+1, len(real_schedule)))