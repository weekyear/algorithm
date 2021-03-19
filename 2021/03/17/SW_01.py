import sys
sys.stdin = open('input_01.txt', 'r')

def deepcopy(lst):
    new_lst = []
    for y in range(len(lst)):
        x_lst = []
        for x in range(len(lst)):
            x_lst.append(lst[y][x])
        new_lst.append(x_lst)
    return new_lst

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(result, k, visit, num_connect):
    global min_result
    global max_connect
    if result > min_result:
        return

    if k == len(cores):
        if max_connect < num_connect:
            max_connect = num_connect
            min_result = result
        elif max_connect == num_connect and min_result > result:
            min_result = result
        return

    canGo = False
    for d in range(4):
        cur_visit = deepcopy(visit)
        new_y = cores[k][0]
        new_x = cores[k][1]
        added_result = 0

        while new_y != 0 and new_y != N - 1 and new_x != 0 and new_x != N - 1:
            new_y += dy[d]
            new_x += dx[d]

            if not cur_visit[new_y][new_x]:
                cur_visit[new_y][new_x] = 1
                added_result += 1
            else:
                break
        else:
            canGo = True
            dfs(result + added_result, k + 1, cur_visit, num_connect + 1)
    else:
        if not canGo:
            dfs(result, k + 1, visit, num_connect)

for tc in range(int(input())):
    N = int(input())

    exinos = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    min_result = 0xffffff
    max_connect = 0
    cores = []

    for y in range(N):
        for x in range(N):
            if exinos[y][x] == 1:
                visited[y][x] = 1
                if not(y == 0 or x == 0 or y == N - 1 or x == N - 1):
                    cores.append([y, x])

    dfs(0, 0, visited, 0)

    print('#{} {}'.format(tc + 1, min_result))