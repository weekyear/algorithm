import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappush, heappop

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(int(input())):
    N = int(input())
    field = [input() for _ in range(N)]
    D = [[0xffffff for _ in range(N)] for _ in range(N)]
    heap = []
    heappush(heap, [0, 0, 0])

    while heap:
        w, y, x = heappop(heap)
        for d in range(4):
            n_y = y + dy[d]
            n_x = x + dx[d]

            if 0 <= n_y < N and 0 <= n_x < N:
                n_v = w + int(field[n_y][n_x])
                if n_v < D[n_y][n_x] and n_v < D[N - 1][N - 1]:
                    D[n_y][n_x] = n_v
                    heappush(heap, [n_v, n_y, n_x])

    print('#{} {}'.format(tc + 1, D[N-1][N-1]))