import sys

sys.stdin = open('boj_16948.txt', 'r')

import sys
from collections import deque

readline = sys.stdin.readline

N = int(readline())
r1, c1, r2, c2 = map(int, readline().split())
visited = [[0 for _ in range(N)] for _ in range(N)]

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

Q = deque([(r1, c1, 0)])
visited[r1][c1] = 1
isFinished = False

while Q:
    cur_r, cur_c, cur_res = Q.popleft()

    for d in range(6):
        new_r, new_c = cur_r + dr[d], cur_c + dc[d]
        if -1 < new_r < N and -1 < new_c < N and not visited[new_r][new_c]:
            visited[new_r][new_c] = 1
            if new_r == r2 and new_c == c2:
                cur_res += 1
                isFinished = True
                break
            Q.append((new_r, new_c, cur_res + 1))
    if isFinished:
        break
else:
    cur_res = -1

print(cur_res)
