import sys
sys.stdin = open('input_2105.txt', 'r')

dx = [1, -1, -1, 1]
dy = [-1, -1, 1, 1]

for tc in range(int(input())):
    N = int(input())

    field = [list(map(int, input().split())) for _ in range(N)]
    desert = [0 for _ in range(101)]

    for d1 in range(1, N - 1):
        for d2 in range(1, N - d1):
            # print(f'{d1} x {d2}')
            for y in range(N):
                desert = [0 for _ in range(101)]
                for x in range(N):
                    max_x = x + d1
                    min_x = x - d2
                    max_y = y + d1 + d2
                    if max_x < N and -1 < min_x and max_y < N:
                        for d in range(4):
                            for dd1 in range(d1 + 1):
                                desert[]