import sys
sys.stdin = open('boj_1389.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline

N, M = map(int, readline().split())

friends = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, readline().split())
    friends[a].append(b)
    friends[b].append(a)

kebins = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    visited[n] = 1

    Q = deque([(n, 1)])

    while Q:
        cur_f, depth = Q.popleft()
        for w in friends[cur_f]:
            if not visited[w]:
                visited[w] = 1
                kebins[n][w] = depth
                Q.append((w, depth + 1))

min_idx = -1
min_val = 0xfffffff
for i in range(1, len(kebins)):
    cur_val = sum(kebins[i])
    if cur_val < min_val:
        min_idx = i
        min_val = cur_val

print(min_idx)