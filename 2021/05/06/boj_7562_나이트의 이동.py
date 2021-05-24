import sys
sys.stdin = open('boj_7562.txt', 'r')

from collections import deque

T = int(input())
dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [2, 1, -1, -2, -2, -1, 1, 2]

for tc in range(T):
    N = int(input())
    s_y, s_x = map(int, input().split())
    e_y, e_x = map(int, input().split())

    visited = [[0] * N for _ in range(N)]
    visited[s_y][s_x] = 1

    Q = deque([(s_y, s_x, 0)])
    result = 0

    if s_y != e_y or s_x != e_x:
        while Q:
            cur_y, cur_x, cur_r = Q.popleft()

            for d in range(8):
                new_y, new_x = cur_y + dy[d], cur_x + dx[d]
                if -1 < new_y < N and -1 < new_x < N and not visited[new_y][new_x]:
                    if new_y == e_y and new_x == e_x:
                        result = cur_r + 1
                        break
                    else:
                        visited[new_y][new_x] = 1
                        Q.append((new_y, new_x, cur_r + 1))
            if result:
                break

    print(result)