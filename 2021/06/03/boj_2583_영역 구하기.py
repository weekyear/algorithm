import sys
sys.stdin = open('boj_2583.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline

M, N, K = map(int, readline().split())

fields = [[0 for _ in range(N)] for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(K):
    l_x, l_y, r_x, r_y = map(int, readline().split())
    for y in range(l_y, r_y):
        for x in range(l_x, r_x):
            fields[y][x] = 1

results = []
for y in range(M):
    for x in range(N):
        result = 1
        if not fields[y][x]:
            Q = deque([(y, x)])
            fields[y][x] = 1

            while Q:
                c_y, c_x = Q.popleft()

                for d in range(4):
                    n_y, n_x = c_y + dy[d], c_x + dx[d]

                    if -1 < n_y < M and -1 < n_x < N and not fields[n_y][n_x]:
                        fields[n_y][n_x] = 1
                        Q.append((n_y, n_x))
                        result += 1
            results.append(result)

results.sort()
print(len(results))
for res in results:
    print(res, end=' ')