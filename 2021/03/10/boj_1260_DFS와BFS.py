import sys
sys.stdin = open('input_1260.txt', 'r')

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for m in range(M):
    m1, m2 = map(int, input().split())
    graph[m1].append(m2)
    graph[m2].append(m1)

for g in graph:
    g.sort()

visited = [0 for _ in range(N + 1)]

# dfs
def dfs(cur_pt):
    visited[cur_pt] = 1
    print(cur_pt, end=' ')

    for m in graph[cur_pt]:
        if not visited[m]:
            dfs(m)

dfs(V)

print()

# bfs
Q = []
Q.append(V)

while Q:
    cur_pt = Q.pop(0)

    if visited[cur_pt]:
        print(cur_pt, end=' ')
        visited[cur_pt] = 0
        for w in graph[cur_pt]:
            if visited[w]:
                Q.append(w)