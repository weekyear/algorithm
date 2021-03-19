import sys
sys.stdin = open('input.txt', 'r')

def dfs(k, cur_val):
    if k >= N:
        global min_result
        if cur_val < min_result:
            min_result = cur_val
    else:
        for x in range(N):
            if not visited[x]:
                visited[x] = 1
                new_val = cur_val + factories[k][x]
                if new_val < min_result:
                    dfs(k + 1, new_val)
                visited[x] = 0

for tc in range(int(input())):
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]

    visited = [0 for _ in range(N)]
    min_result = 0
    for n in range(N):
        min_val = 0xffffff
        for m in range(N):
            if not visited[m] and min_val > factories[n][m]:
                visited[m] = 1
                min_val = factories[n][m]
        min_result += min_val

    visited = [0 for _ in range(N)]
    dfs(0, 0)

    print('#{} {}'.format(tc + 1, min_result))