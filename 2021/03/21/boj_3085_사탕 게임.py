import sys
sys.stdin = open('input_3085.txt', 'r')

def check_same_candy(cur_y, cur_x):
    col_stack = 0
    c_y = cur_y - 1
    while -1 < c_y and board[c_y][cur_x] == board[cur_y][cur_x]:
        col_stack += 1
        c_y -= 1

    c_y = cur_y + 1
    while c_y < N and board[c_y][cur_x] == board[cur_y][cur_x]:
        col_stack += 1
        c_y += 1

    row_stack = 0
    c_x = cur_x - 1
    while -1 < c_x and board[cur_y][c_x] == board[cur_y][cur_x]:
        row_stack += 1
        c_x -= 1

    c_x = cur_x + 1
    while c_x < N and board[cur_y][c_x] == board[cur_y][cur_x]:
        row_stack += 1
        c_x += 1

    if row_stack == 0 and col_stack == 0:
        return 0
    return max(row_stack + 1, col_stack + 1)

N = int(input())
board = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0

for y in range(N):
    for x in range(N):
        for d in range(4):
            new_y = y + dy[d]
            new_x = x + dx[d]
            if -1 < new_y < N and -1 < new_x < N:
                board[new_y][new_x], board[y][x] = board[y][x], board[new_y][new_x]
                cur_result = check_same_candy(y, x)
                board[new_y][new_x], board[y][x] = board[y][x], board[new_y][new_x]

                if result < cur_result:
                    result = cur_result
print(result)