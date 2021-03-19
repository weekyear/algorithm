import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

sys.setrecursionlimit(10000)


def dfs(x, y, k):
    global max_k

    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]

        if -1 < new_x < N and -1 < new_y < N:
            new_val = rooms[new_y][new_x]
            if new_val == rooms[y][x] + 1:
                if not memory.get(new_val, False):
                    result = dfs(new_x, new_y, k + 1)
                    if memory.get(new_val, 0) < result:
                        memory[new_val] = result
                    return result
                else:
                    return k + memory.get(new_val, False) - 1
    else:
        return k


for tc in range(T):
    N = int(input())
    max_k = 0
    s_num = -1
    rooms = [list(map(int, input().split())) for _ in range(N)]
    memory = {}

    for j in range(N):
        for i in range(N):
            temp_k = dfs(i, j, 1)
            if temp_k > max_k:
                max_k = temp_k
                s_num = rooms[j][i]
            elif temp_k == max_k and s_num > rooms[j][i]:
                s_num = rooms[j][i]

    print('#{} {} {}'.format(tc + 1, s_num, max_k))
