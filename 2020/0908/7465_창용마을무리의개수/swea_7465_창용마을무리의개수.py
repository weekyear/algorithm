import sys

sys.stdin = open('input.txt', 'r')

def dfs(k):
    visited[k] = 1
    for w in relations.get(k, []):
        if visited[w] == 0:
            dfs(w)

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)
    result = 0

    relations = {num : [] for num in range(1, N+1)}
    for _ in range(M):
        I, J = map(int, input().split())
        relations[I].append(J)
        relations[J].append(I)

    for n in range(1, N+1):
        if visited[n] == 0:
            dfs(n)
            result += 1



    # BFS
    # for human in relations:
    #     if visited[human] == 0:
    #         result += 1
    #         Q = [human]
    #         visited[human] = 1
    #
    #         while Q:
    #             v = Q.pop(0)
    #
    #             for w in relations.get(v, []):
    #                 if visited[w] == 0:
    #                     Q.append(w)
    #                     visited[w] = 1

    print('#{} {}'.format(tc + 1, result))
