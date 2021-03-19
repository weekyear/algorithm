import sys
sys.stdin = open('input_1303.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())

field = [input() for _ in range(M)]

power_w = 0
power_b = 0
visited = [[0 for _ in range(N)] for _ in range(M)]

def dfs(y, x, score, type):
    visited[y][x] = 1
    for d in range(4):
        new_y = y + dy[d]
        new_x = x + dx[d]
        if -1 < new_y < M and -1 < new_x < N and not visited[new_y][new_x]:
            if type == field[new_y][new_x]:
                score = dfs(new_y, new_x, score + 1, type)
    else:
        return score


for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            if field[y][x] == 'W':
                power_w += dfs(y, x, 1, field[y][x]) ** 2
            else:
                power_b += dfs(y, x, 1, field[y][x]) ** 2

print(power_w, power_b)