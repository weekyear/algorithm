import sys
sys.stdin = open('input.txt', 'r')


from copy import deepcopy

def checkVisit(x, y, _list):
    for d in range(8):
        new_x = x
        new_y = y
        while -1 < new_x < N and -1 < new_y < N:
            _list[new_y][new_x] = 1
            new_x += dx[d]
            new_y += dy[d]
    return _list

def dfs(y, cur_board):
    if y == N:
        global count
        count += 1
    else:
        for x in range(N):
            if cur_board[y][x] == 0:
                new_board = deepcopy(cur_board)
                checkVisit(x, y, new_board)
                dfs(y+1, new_board)

T = int(input())

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

for tc in range(T):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    count = 0

    dfs(0, board)

    print('#{} {}'.format(tc+1, count))