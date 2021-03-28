import sys
sys.stdin = open('boj_1520.txt')

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    if y == 0 and x == 0:
        return 1

    result = 0
    for d in range(4):
        new_y = y + dy[d]
        new_x = x + dx[d]

        if -1 < new_y < M and -1 < new_x < N and field[new_y][new_x] > field[y][x]:
            if cache[new_y][new_x] == -1:
                result += dfs(new_y, new_x)
            else:
                result += cache[new_y][new_x]

    cache[y][x] = result
    return result

input = stdin.readline

M, N = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(M)]
cache = [[-1] * N for _ in range(M)]

print(dfs(M - 1, N - 1))