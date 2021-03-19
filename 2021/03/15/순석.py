import sys
sys.stdin = open('input_10966.txt', 'r')

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pool = []
    arr =[[0] * M for _ in range(N)]
    ans = 0
    water = deque()
    for i in range(N):
        pool.append(input())
        for j in range(M):
            if pool[i][j] == 'W':
                arr[i][j] = -1
                water.append((i, j, 0))

    dist = 0
    while water:
        x, y, dist = water.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M or pool[tx][ty] == 'W':
                continue

            if arr[tx][ty] == 0:
                arr[tx][ty] = dist + 1
                ans += arr[tx][ty]
                water.append((tx, ty, dist + 1))

    print('#{} {}'.format(t, ans))