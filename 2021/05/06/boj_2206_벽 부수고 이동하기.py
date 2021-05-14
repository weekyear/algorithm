import sys
sys.stdin = open('boj_2206.txt', 'r')

from collections import deque
import sys

readlines = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, readlines().split())
field = [readlines() for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

Q = deque([(0, 0, 0, visited, 1)])
result = 0

while Q:
    cur_y, cur_x, wall, cur_v, cur_r = Q.popleft()

    if cur_y == N - 1 and cur_x == M - 1:
        result = cur_r
        break

    for d in range(4):
        new_y, new_x = cur_y + dy[d], cur_x + dx[d]

        if -1 < new_y < N and -1 < new_x < M and not visited[wall][new_y][new_x]:
            if new_y == N - 1 and new_x == M - 1:
                result = cur_r + 1
                break

            if field[new_y][new_x] == '0':
                new_v = cur_v[:]
                new_v[wall][new_y][new_x] = 1
                Q.append((new_y, new_x, wall, new_v, cur_r + 1))
            elif wall == 0 and field[new_y][new_x] == '1':
                new_v = cur_v[:]
                new_v[wall + 1][new_y][new_x] = 1
                Q.append((new_y, new_x, wall + 1, new_v, cur_r + 1))
    if result:
        break

print(result if result != 0 else -1)