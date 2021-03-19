import sys
sys.stdin = open('input_5105.txt', 'r')

from collections import deque

for tc in range(int(input())):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    S = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for n in range(N):
        for m in range(N):
            if maze[n][m] == '2':
                S = (n, m, 0)
                break
        if S:
            break

    Q = deque()
    Q.append(S)

    result = 0

    while Q:
        y, x, step = Q.popleft()

        for d in range(4):
            n_y = y + dy[d]
            n_x = x + dx[d]

            if -1 < n_x < N and -1 < n_y < N and maze[n_y][n_x] != '1':
                if maze[n_y][n_x] == '3':
                    result = step
                    break
                if not visited[n_y][n_x]:
                    visited[n_y][n_x] = 1
                    Q.append((n_y, n_x, step + 1))

        if result:
            break

    print('#{} {}'.format(tc + 1, result))