import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, _sum):
    global min_num
    if _sum > min_num:
        return
    if idx >= N:
        if _sum >= B:
            min_num = _sum
        return
    visited[idx] = True
    dfs(idx + 1, _sum + h_list[idx])
    visited[idx] = False
    dfs(idx + 1, _sum)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    h_list = list(map(int, input().split()))

    min_num = 99999
    # 탐욕 알고리즘
    temp = 0
    for i in range(N):
        temp += h_list[i]
        if temp > B:
            min_num = temp
            break

    visited = [False for _ in range(N)]
    dfs(0, 0)
    print('#{} {}'.format(tc+1, min_num-B))