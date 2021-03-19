import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(cur_list, cur_val, r):
    if r == N:
        global min_val
        cur_val += table[cur_list[N-1]][0]
        if cur_val < min_val:
            min_val = cur_val
    else:
        for p in p_list:
            if not visited[p]:
                cur_list[r] = p
                visited[p] = 1
                new_val = cur_val + table[cur_list[r-1]][cur_list[r]]
                if new_val < min_val:
                    dfs(cur_list, new_val, r + 1)
                visited[p] = 0

for tc in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    min_val = 0xffffff
    for n in range(N):
        temp_val = sum(table[n])
        for m in range(N):
            temp_val += table[m][0]
        min_val = temp_val

    visited = [0] * N
    p_list = list(range(1, N))
    dfs([0]*N, 0, 1)

    print('#{} {}'.format(tc+1, min_val))