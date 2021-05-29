import sys
sys.stdin = open('boj_14503.txt', 'r')

import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
y, x, cur_d = map(int, readline().split())
fields = [list(map(int, readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 0

isFinished = False
while not isFinished:
    if not visited[y][x]:
        visited[y][x] = 1
        result += 1

    for d in range(1, 5):
        n_d = (cur_d - d + 4) % 4
        n_y, n_x = y + dy[n_d], x + dx[n_d]

        if -1 < n_y < N and -1 < n_x < M and not visited[n_y][n_x] and not fields[n_y][n_x]:
            y, x = n_y, n_x
            cur_d = n_d
            break
    else:
        n_y, n_x = y - dy[cur_d], x - dx[cur_d]
        if not fields[n_y][n_x]:
            y, x = n_y, n_x
        else:
            isFinished = True

print(result)
