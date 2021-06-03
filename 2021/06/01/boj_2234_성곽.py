import sys
sys.stdin = open('boj_2234.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline

N, M = map(int, readline().split())

fields = [list(map(int, readline().split())) for _ in range(M)]
rooms = [[0 for _ in range(N)] for _ in range(M)]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

room_num = 0
areas = [0]

for y in range(M):
    for x in range(N):
        if not rooms[y][x]:
            room_num += 1
            area = 1
            Q = deque([(y, x)])
            rooms[y][x] = room_num

            while Q:
                c_y, c_x = Q.popleft()

                for d in range(4):
                    if not(fields[c_y][c_x] & 2 ** d):
                        n_y, n_x = c_y + dy[d], c_x + dx[d]
                        if -1 < n_y < M and -1 < n_x < N and not rooms[n_y][n_x]:
                            rooms[n_y][n_x] = room_num
                            Q.append((n_y, n_x))
                            area += 1
            areas.append(area)

print(room_num)
max_area = max(areas)
print(max_area)

for y in range(M):
    for x in range(N):
        for d in range(4):
            n_y, n_x = y + dy[d], x + dx[d]
            if -1 < n_y < M and -1 < n_x < N and rooms[y][x] != rooms[n_y][n_x]:
                if areas[rooms[y][x]] + areas[rooms[n_y][n_x]] > max_area:
                    max_area = areas[rooms[y][x]] + areas[rooms[n_y][n_x]]

print(max_area)
