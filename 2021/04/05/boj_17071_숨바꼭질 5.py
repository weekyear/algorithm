import sys
sys.stdin = open('boj_17071.txt', 'r')
from collections import deque

N, K = map(int, input().split())
visited = [[0 for _ in range(500001)] for _ in range(2)]
k_pos = [K]

Q = deque()
Q.append((N, 0))
visited[0][N] = 1
result = 0

def getBro(n):
    return K + (n * (n + 1) // 2)

def checkResult(cur_N, cur_M, cur_bro):
    if not visited[cur_M % 2][cur_N]:
        visited[cur_M % 2][cur_N] = 1
        if cur_N == cur_bro:
            return M + 1
        else:
            Q.append((cur_N, M + 1))
            return -1
    else:
        return -1

if N == K:
    print(0)
else:
    while Q:
        N, M = Q.popleft()

        bro = getBro(M + 1)
        if bro > 500000:
            result = -1
            break

        if visited[(M + 1) % 2][bro]:
            result = M + 1
            break

        if N > 0:
            result = checkResult(N - 1, M + 1, bro)
            if result != -1:
                break

        if N < 500000:
            result = checkResult(N + 1, M + 1, bro)
            if result != -1:
                break

        if N < 250001:
            result = checkResult(N * 2, M + 1, bro)
            if result != -1:
                break

    print(result)