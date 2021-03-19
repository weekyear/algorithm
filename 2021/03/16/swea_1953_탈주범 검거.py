import sys
sys.stdin = open('input_1953.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

turnel_info = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
]

for tc in range(int(input())):
    N, M, R, C, L = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[R][C] = 1

    Q = [(R, C, 1)]

    result = 1
    while Q:
        cur_y, cur_x, time = Q.pop(0)

        if time == L:
            break

        for d in range(4):
            new_y, new_x = cur_y + dy[d], cur_x + dx[d]

            if d % 2:
                rev_d = d - 1
            else:
                rev_d = d + 1

            if -1 < new_y < N and -1 < new_x < M and not visited[new_y][new_x]:
                if turnel_info[field[cur_y][cur_x]][d] == 1 and turnel_info[field[new_y][new_x]][rev_d] == 1:
                    visited[new_y][new_x] = 1
                    Q.append((new_y, new_x, time + 1))
                    result += 1

    print("#{} {}".format(tc + 1, result))
