import sys
sys.stdin = open('input_1952.txt', 'r')

def dfs(n, temp):
    global total
    if n > 11:
        if temp < total:
            total = temp
        return

    dfs(n + 1, temp + expenses[n])

    dfs(n + 3, temp + three_month)

for tc in range(int(input())):
    day, month, three_month, year = map(int, input().split())

    schedules = list(map(int, input().split()))
    expenses = [0 for _ in range(12)]

    for s in range(12):
        if schedules[s] * day < month:
            expenses[s] = schedules[s] * day
        else:
            expenses[s] = month

    total = 0xffffff
    dfs(0, 0)

    if total > year:
        print('#{} {}'.format(tc + 1, year))
    else:
        print('#{} {}'.format(tc + 1, total))