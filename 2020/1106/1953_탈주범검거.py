import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

turnel = {
    0: '0000',
    1: '1111',
    2: '1100',
    3: '0011',
    4: '1001',
    5: '0101',
    6: '0110',
    7: '1010',
}

opponent = [1, 0, 3, 2]

for tc in range(int(input())):
    N, M, R, C, L = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    Q = [(R, C, 1)]
    visited[R][C] = 1
    count = 1
    while Q:
        y, x, hour = Q.pop(0)

        for d in range(4):
            new_y = y + dy[d]
            new_x = x + dx[d]

            if -1 < new_x < M and -1 < new_y < N:
                if turnel[field[y][x]][d] == turnel[field[new_y][new_x]][opponent[d]] == '1':
                    if not visited[new_y][new_x]:
                        visited[new_y][new_x] = 1
                        if hour + 1 <= L:
                            Q.append((new_y, new_x, hour + 1))
                            count += 1

    print('#{} {}'.format(tc + 1, count))