import sys
sys.stdin = open('boj_2644.txt', 'r')

N = int(input())
a, b = map(int, input().split())
P = int(input())

linked = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(P):
    c, d = map(int, input().split())
    linked[c].append(d)
    linked[d].append(c)

Q = [(a, 0)]

result = 0
while Q:
    cur_p, cur_r = Q.pop(0)

    for w in linked[cur_p]:
        if not visited[w]:
            visited[w] = 1
            Q.append((w, cur_r + 1))

        if w == b:
            result = cur_r + 1
            break

    if result:
        break

print(result if result != 0 else -1)