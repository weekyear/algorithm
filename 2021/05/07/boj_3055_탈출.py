import sys
sys.stdin = open('boj_3055.txt', 'r')

import sys
from collections import deque
readlines = sys.stdin.readline

R, C = map(int, input().split())
field = [input() for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

waters = []
water_fields = [[-1] * C for _ in range(R)]
me, goal = 0, 0

for r in range(R):
    for c in range(C):
        if field[r][c] == 'D':
            goal = (r, c)
        elif field[r][c] == 'S':
            water_fields[r][c] = 0
            me = (r, c)
        elif field[r][c] == '*':
            water_fields[r][c] = 1
            waters.append((r, c))

Q = deque([(me, 0)])
result = 0
max_r = 0

while Q:
    cur_me, cur_r = Q.popleft()

    if cur_r >= max_r:
        max_r = cur_r + 1
        new_water = []
        for water in waters:
            for d in range(4):
                n_w_y, n_w_x = water[0] + dy[d], water[1] + dx[d]

                if -1 < n_w_y < R and -1 < n_w_x < C and field[n_w_y][n_w_x] != 'X' and field[n_w_y][n_w_x] != 'D' and water_fields[n_w_y][n_w_x] == -1:
                    water_fields[n_w_y][n_w_x] = max_r + 1
                    new_water.append((n_w_y, n_w_x))

        waters = new_water

    for d in range(4):
        new_y, new_x = cur_me[0] + dy[d], cur_me[1] + dx[d]

        if -1 < new_y < R and -1 < new_x < C and field[new_y][new_x] != 'X' and water_fields[new_y][new_x] <= cur_r + 1 and water_fields[new_y][new_x] == -1:
            if field[new_y][new_x] == 'D':
                result = cur_r + 1
                break
            else:
                water_fields[new_y][new_x] = water_fields[cur_me[0]][cur_me[1]] + 1
                Q.append([(new_y, new_x), cur_r + 1])

    if result:
        break

print(result if result else 'KAKTUS')