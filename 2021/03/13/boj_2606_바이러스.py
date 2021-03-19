import sys
sys.stdin = open('input_2606.txt', 'r')

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N + 1)]
Q = [1]
visited[1] = 1
result = 0

while Q:
    com = Q.pop(0)

    for w in graph[com]:
        if not visited[w]:
            visited[w] = 1
            result += 1
            Q.append(w)

print(result)
