import sys
sys.stdin = open('input_2178.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

Q = [(0, 0, 1)]
result = 0

while Q:
    y, x, k = Q.pop(0)

    if not visited[y][x]:
        visited[y][x] = 1
        for d in range(4):
            n_y = y + dy[d]
            n_x = x + dx[d]
            if -1 < n_y < N and -1 < n_x < M:
                if not visited[n_y][n_x] and maze[n_y][n_x] == '1':
                    if n_y != N - 1 or n_x != M - 1:
                        Q.append((n_y, n_x, k + 1))
                    else:
                        result = k + 1
                        break
        if result:
            print(result)
            break