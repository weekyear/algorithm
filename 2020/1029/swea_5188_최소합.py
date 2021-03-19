import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dx = [0, 1]
dy = [1, 0]

def dfs(x, y, cur_val):
    if x == N - 1 and y == N - 1:
        global min_val
        if min_val > cur_val:
            min_val = cur_val
    else:
        for d in range(2):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if -1 < new_x < N and -1 < new_y < N:
                temp_val = cur_val + table[new_x][new_y]
                if temp_val < min_val:
                    dfs(new_x, new_y, temp_val)


for tc in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    min_val = 0xffffff

    dfs(0, 0, table[0][0])

    print('#{} {}'.format(tc+1, min_val))