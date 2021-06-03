import sys

sys.stdin = open('boj_11559.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline

fields = [list(readline()[:6]) for _ in range(12)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0

while True:
    visited = [[0 for _ in range(6)] for _ in range(12)]
    isPuyo = False
    for y in range(11, -1, -1):
        for x in range(6):
            if fields[y][x] != '.' and not visited[y][x]:
                cur_type = fields[y][x]
                Q = deque([(y, x)])
                visited[y][x] = 1
                stack = 1
                delete_list = [(y, x)]
                while Q:
                    c_y, c_x = Q.popleft()

                    for d in range(4):
                        n_y, n_x = c_y + dy[d], c_x + dx[d]
                        if -1 < n_y < 12 and -1 < n_x < 6:
                            if not visited[n_y][n_x] and fields[n_y][n_x] == cur_type:
                                delete_list.append((n_y, n_x))
                                visited[n_y][n_x] = 1
                                stack += 1
                                Q.append((n_y, n_x))

                if stack > 3:
                    for d_y, d_x in delete_list:
                        fields[d_y][d_x] = '.'
                    if not isPuyo:
                        result += 1
                        isPuyo = True
    if not isPuyo:
        break

    for x in range(6):
        for y in range(11, -1, -1):
            if fields[y][x] != '.':
                dot_stack = 0
                for c_y in range(y + 1, 12):
                    if fields[c_y][x] == '.':
                        dot_stack += 1
                    else:
                        break
                if dot_stack > 0:
                    fields[y + dot_stack][x] = fields[y][x]
                    fields[y][x] = '.'

print(result)