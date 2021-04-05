import sys

sys.stdin = open('boj_16959.txt', 'r')
from sys import stdin
from collections import deque

readline = stdin.readline

N = int(input())
board = [list(map(int, readline().split())) for _ in range(N)]
board_idx = [0] * (N * N + 1)
visited = [[[[0 for _ in range(3)] for _ in range(N ** 2 + 1)] for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(N):
        board_idx[board[y][x]] = (y, x)


def knight(c_y, c_x):
    knight_rule = [(1, 2), (-1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]
    positions = []
    for r in range(8):
        n_y = c_y + knight_rule[r][0]
        n_x = c_x + knight_rule[r][1]
        if -1 < n_y < N and -1 < n_x < N:
            positions.append((n_y, n_x))

    return positions


def look(c_y, c_x):
    positions = []
    for p in range(N):
        if p == c_y:
            continue
        positions.append((p, c_x))

    for p in range(N):
        if p == c_x:
            continue
        positions.append((c_y, p))

    return positions


def findNextNumByLook(c_y, c_x, n_num):
    for p in range(N):
        if board[c_y][p] == n_num:
            return c_y, p

        if board[p][c_x] == n_num:
            return p, c_x

    return -1, -1


def findNextNumByBishop(c_y, c_x, n_num):
    d1 = c_y + c_x
    d2 = c_y - c_x
    for p in range(N):
        p_x = d1 - p
        p_y = d2 + p
        if -1 < p_x < N and board[p][p_x] == n_num:
            return p, p_x

        if -1 < p_y < N and board[p_y][p] == n_num:
            return p_y, p

    return -1, -1


def bishop(c_y, c_x):
    positions = []
    d1 = c_y + c_x
    d2 = c_y - c_x

    for p_y in range(N):
        if p_y == c_y:
            continue
        p_x = d1 - p_y
        if -1 < p_x < N:
            positions.append((p_y, p_x))

    for p_x in range(N):
        if p_x == c_x:
            continue
        p_y = d2 + p_x
        if -1 < p_y < N:
            positions.append((p_y, p_x))

    return positions


cur_chess = 0
Q = deque()
result = 0xffffff

for i in range(3):
    Q.append((board_idx[1][0], board_idx[1][1], 2, i, 0))
    visited[board_idx[1][0]][board_idx[1][1]][2][i] = 1

while Q:
    cur_y, cur_x, next_num, cur_type, exp = Q.popleft()

    if exp >= result:
        continue

    if next_num == N ** 2 + 1 and result > exp:
        result = exp
        continue

    if cur_type == 2:
        first_knight_positions = []
        for new_y, new_x in knight(cur_y, cur_x):
            if not visited[new_y][new_x][next_num][cur_type]:
                visited[new_y][new_x][next_num][cur_type] = 1
                first_knight_positions.append((new_y, new_x))
                if board[new_y][new_x] == next_num:
                    Q.append((new_y, new_x, next_num + 1, cur_type, exp + 1))
                    break
        else:
            for k_y, k_x in first_knight_positions:
                for new_y, new_x in knight(k_y, k_x):
                    if not visited[new_y][new_x][next_num][cur_type]:
                        visited[new_y][new_x][next_num][cur_type] = 1
                        if board[new_y][new_x] == next_num:
                            Q.append((new_y, new_x, next_num + 1, cur_type, exp + 2))
                            break
                if board[new_y][new_x] == next_num:
                    break
            else:
                if not visited[cur_y][cur_x][next_num][0]:
                    visited[cur_y][cur_x][next_num][0] = 1
                    Q.append((cur_y, cur_x, next_num, 0, exp + 1))
                if not visited[cur_y][cur_x][next_num][1]:
                    visited[cur_y][cur_x][next_num][1] = 1
                    Q.append((cur_y, cur_x, next_num, 1, exp + 1))

    else:
        new_y, new_x = findNextNumByLook(cur_y, cur_x, next_num) if cur_type == 0 else findNextNumByBishop(cur_y, cur_x, next_num)
        if new_y != -1:
            if not visited[new_y][new_x][next_num][cur_type]:
                visited[new_y][new_x][next_num][cur_type] = 1
                Q.append((new_y, new_x, next_num + 1, cur_type, exp + 1))
        else:
            new_y = board_idx[next_num][0]
            new_x = board_idx[next_num][1]
            if cur_type == 0 or (cur_type == 1 and (cur_y + cur_x) % 2 == (new_y + new_x) % 2):
                if not visited[new_y][new_x][next_num][cur_type]:
                    visited[new_y][new_x][next_num][cur_type] = 1
                    Q.append((new_y, new_x, next_num + 1, cur_type, exp + 2))

            for t in range(3):
                if not visited[cur_y][cur_x][next_num][t]:
                    visited[cur_y][cur_x][next_num][t] = 1
                    Q.append((cur_y, cur_x, next_num, t, exp + 1))

print(result)