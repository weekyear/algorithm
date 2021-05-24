import sys

sys.stdin = open('boj_11724.txt', 'r')

import sys
sys.setrecursionlimit(10000)

readlines = sys.stdin.readline

N, M = map(int, readlines().split())
linked = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)


def dfs(i):
    for w in linked[i]:
        if not visited[w]:
            visited[w] = 1
            dfs(w)


for _ in range(M):
    a, b = map(int, readlines().split())
    linked[a].append(b)
    linked[b].append(a)

result = 0
for n in range(1, N + 1):
    if not visited[n]:
        result += 1
        dfs(n)

print(result)
