import sys

sys.stdin = open('boj_16959.txt', 'r')
from sys import stdin
from collections import deque

readline = stdin.readline

N = int(input())
board = [list(map(int, readline().split())) for _ in range(N)]

visited = [[[[0 for _ in range(3)] for _ in range(N ** 2 + 1)] for _ in range(N)] for _ in range(N)]
expenses = [0xfffff] * (N ** 2 + 1)
expenses[1] = 0
Q = deque()
result = 0


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


for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            for i in range(3):
                Q.append((y, x, 2, i, 0))
                visited[y][x][2][i] = 1
            break
    if len(Q):
        break

while Q:
    cur_y, cur_x, next_num, c_type, exp = Q.popleft()

    new_positions = look(cur_y, cur_x) if c_type == 0 else bishop(cur_y, cur_x) if c_type == 1 else knight(cur_y, cur_x)
    for new_k_y, new_k_x in new_positions:
        if not visited[new_k_y][new_k_x][next_num][c_type]:
            visited[new_k_y][new_k_x][next_num][c_type] = 1
            if board[new_k_y][new_k_x] == next_num:
                if next_num == N ** 2:
                    result = exp + 1
                    break
                if exp + 1 - expenses[next_num - 1] < 4:
                    Q.append((new_k_y, new_k_x, next_num + 1, c_type, exp + 1))
            else:
                Q.append((new_k_y, new_k_x, next_num, c_type, exp + 1))

    if result:
        break

    for t in range(3):
        if not visited[cur_y][cur_x][next_num][t]:
            visited[cur_y][cur_x][next_num][t] = 1
            Q.append((cur_y, cur_x, next_num, t, exp + 1))

print(result)
