import sys
sys.stdin = open('input_1743.txt', 'r')

N, M, K = map(int, input().split())
field = [[0 for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for k in range(K):
    r, c = map(int, input().split())
    field[r-1][c-1] = 1

max_size = 0

for n in range(N):
    for m in range(M):
        size = 1
        if field[n][m]:
            field[n][m] = 0
            Q = [(n, m)]

            while Q:
                y, x = Q.pop(0)

                for d in range(4):
                    n_y = y + dy[d]
                    n_x = x + dx[d]

                    if -1 < n_y < N and -1 < n_x < M and field[n_y][n_x]:
                        field[n_y][n_x] = 0
                        size += 1
                        Q.append((n_y, n_x))

            if size > max_size:
                max_size = size

print(max_size)