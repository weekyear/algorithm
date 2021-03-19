import sys

sys.stdin = open('input_1949.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def getMaxHeightPositions():
    max_h = 0
    max_h_list = []

    for y in range(N):
        for x in range(N):
            if mountain[y][x] > max_h:
                max_h_list.clear()
                max_h = mountain[y][x]
                max_h_list.append((y, x))
            elif mountain[y][x] == max_h:
                max_h_list.append((y, x))

    return max_h, max_h_list

def dfs(cur_info, cur_l):
    global chance
    global max_l
    if cur_l > max_l:
        max_l = cur_l
    cur_y = cur_info[0]
    cur_x = cur_info[1]
    cur_h = cur_info[2]
    for d in range(4):
        n_y = cur_y + dy[d]
        n_x = cur_x + dx[d]
        if -1 < n_y < N and -1 < n_x < N and not visited[n_y][n_x]:
            new_h = mountain[n_y][n_x]
            if new_h < cur_h:
                visited[n_y][n_x] = 1
                dfs((n_y, n_x, mountain[n_y][n_x]), cur_l + 1)
                visited[n_y][n_x] = 0
            elif chance and new_h - K < cur_h:
                mountain[n_y][n_x] = cur_h - 1
                chance = 0
                visited[n_y][n_x] = 1
                dfs((n_y, n_x, mountain[n_y][n_x]), cur_l + 1)
                mountain[n_y][n_x] = new_h
                chance = 1
                visited[n_y][n_x] = 0

for tc in range(int(input())):
    N, K = map(int, input().split())
    global chance

    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    max_h, max_h_list = getMaxHeightPositions()

    max_l = 0

    for h_pos in max_h_list:
        chance = 1
        h_y = h_pos[0]
        h_x = h_pos[1]

        visited[h_y][h_x] = 1
        dfs((h_y, h_x, max_h), 1)
        visited[h_y][h_x] = 0

    print('#{} {}'.format(tc + 1, max_l))
