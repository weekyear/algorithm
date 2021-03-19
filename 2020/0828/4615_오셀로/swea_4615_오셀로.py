import sys

sys.stdin = open("input.txt", "r")

T = int(input())

dx_list = [1, -1, 0, 0, 1, 1, -1, -1]
dy_list = [0, 0, 1, -1, -1, 1, -1, 1]

for test_case in range(T):
    N, M = map(int, input().split())

    othello = [[0 for _ in range(N+1)] for _ in range(N+1)]

    othello[N//2][N//2] = othello[N//2+1][N//2+1] = 2
    othello[N//2][N//2+1] = othello[N//2+1][N//2] = 1

    num_w = 2
    num_b = 2

    for m in range(M):
        x, y, s = map(int, input().split())
        othello[y][x] = s
        if s == 1:
            num_b += 1
        elif s == 2:
            num_w += 1

        stack = []
        direc_idx = 0

        for direc_idx in range(len(dx_list)):
            stack.clear()

            cur_x = x + dx_list[direc_idx]
            cur_y = y + dy_list[direc_idx]

            while 0 < cur_x < N+1 and 0 < cur_y < N+1:
                if othello[cur_y][cur_x] == 0:
                    break
                elif othello[cur_y][cur_x] != s:
                    stack.append([cur_x, cur_y])
                    cur_x += dx_list[direc_idx]
                    cur_y += dy_list[direc_idx]
                else:
                    for xy in stack:
                        othello[xy[1]][xy[0]] = s
                        if s == 1:
                            num_b += 1
                            num_w -= 1
                        elif s == 2:
                            num_b -= 1
                            num_w += 1
                    break

    print('#{} {} {}'.format(test_case + 1, num_b, num_w))