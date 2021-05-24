import sys

sys.stdin = open('boj_2468.txt', 'r')

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
height_info = {}

max_h = 0
for y in range(N):
    for x in range(N):
        cur_v = field[y][x]
        if cur_v > max_h:
            max_h = cur_v
        if height_info.get(cur_v, False):
            height_info[cur_v].append((y, x))
        else:
            height_info[cur_v] = height_info.get(cur_v, [(y, x)])

max_safe = 1
visited = [item[:] for item in field]
for rain in range(1, max_h):
    if height_info.get(rain, False):
        for y, x in height_info.get(rain, []):
            visited[y][x] = 0

    cur_visited = [item[:] for item in visited]
    cur_safe = 0
    for y in range(N):
        for x in range(N):
            if cur_visited[y][x]:
                cur_safe += 1
                cur_visited[y][x] = 0

                Q = deque([(y, x)])

                while Q:
                    cur_y, cur_x = Q.popleft()
                    for d in range(4):
                        new_y, new_x = cur_y + dy[d], cur_x + dx[d]

                        if -1 < new_y < N and -1 < new_x < N and cur_visited[new_y][new_x]:
                            Q.append((new_y, new_x))
                            cur_visited[new_y][new_x] = 0

    if cur_safe > max_safe:
        max_safe = cur_safe

print(max_safe)