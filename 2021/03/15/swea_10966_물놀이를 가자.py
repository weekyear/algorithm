import sys
sys.stdin = open('input_10966.txt', 'r')

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(int(input())):
    N, M = map(int, input().split())

    field = [input() for _ in range(N)]

    result = 0

    distances = [[-1 for _ in range(M)] for _ in range(N)]
    Q = deque()
    for y in range(N):
        for x in range(M):
            if field[y][x] == "W":
                distances[y][x] = 0
                Q.append((y, x))

    while Q:
        cur_y, cur_x = Q.popleft()
        distance = distances[cur_y][cur_x]

        for d in range(4):
            new_y = cur_y + dy[d]
            new_x = cur_x + dx[d]

            if -1 < new_y < N and -1 < new_x < M:
                if field[new_y][new_x] == 'L' and distances[new_y][new_x] == -1:
                    result += distance + 1
                    distances[new_y][new_x] = distance + 1
                    Q.append((new_y, new_x))

    # L을 기준으로 최소거리를 찾아가면 시간 초과가 뜸
    # for y in range(N):
    #     for x in range(M):
    #         min_time = 0
    #         if field[y][x] == "L":
    #             visited = [[0 for _ in range(M)] for _ in range(N)]
    #             visited[y][x] = 1
    #             isFindWater = False
    #             Q = [(y, x, 0)]
    #
    #             while Q:
    #                 cur_y, cur_x, time = Q.pop(0)
    #
    #                 for d in range(4):
    #                     new_y = cur_y + dy[d]
    #                     new_x = cur_x + dx[d]
    #
    #                     if -1 < new_y < N and -1 < new_x < M:
    #                         if field[new_y][new_x] == 'L':
    #                             Q.append((new_y, new_x, time + 1))
    #                         else:
    #                             isFindWater = True
    #                             min_time = time + 1
    #                             break
    #
    #                 if isFindWater:
    #                     break
    #         result += min_time

    print('#{} {}'.format(tc + 1, result))