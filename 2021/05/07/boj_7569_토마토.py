import sys
sys.stdin = open('boj_7569.txt', 'r')

from collections import deque
import sys

readlines = sys.stdin.readline

dh = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, readlines().split())

field = [[list(map(int, readlines().split())) for _ in range(N)] for _ in range(H)]

remains = 0
Q = deque([])
for h in range(H):
    for y in range(N):
        for x in range(M):
            if field[h][y][x] == 0:
                remains += 1
            elif field[h][y][x] == 1:
                Q.append((h, y, x, 0))

result = 0
if remains:
    while Q:
        cur_h, cur_y, cur_x, cur_r = Q.popleft()

        for d in range(6):
            new_h, new_y, new_x = cur_h + dh[d], cur_y + dy[d], cur_x + dx[d]

            if -1 < new_h < H and -1 < new_y < N and -1 < new_x < M and not field[new_h][new_y][new_x]:
                remains -= 1
                if remains == 0:
                    result = cur_r + 1

                field[new_h][new_y][new_x] = 1
                Q.append((new_h, new_y, new_x, cur_r + 1))

        if result:
            break
    print(result if result != 0 else -1)
else:
    print(0)