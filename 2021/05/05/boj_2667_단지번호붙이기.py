import sys

sys.stdin = open('boj_2667.txt', 'r')

import sys

sys.setrecursionlimit(10000)
readlines = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())

field = [list(readlines()) for _ in range(N)]

def dfs(cur_y, cur_x):
    global res
    for d in range(4):
        new_y, new_x = cur_y + dy[d], cur_x + dx[d]
        if -1 < new_y < N and -1 < new_x < N and field[new_y][new_x] == '1':
            field[new_y][new_x] = '0'
            res += 1
            dfs(new_y, new_x)


num = 0
res = 0
results = []
for y in range(N):
    for x in range(N):
        if field[y][x] == '1':
            num += 1
            res = 1
            field[y][x] = '0'
            dfs(y, x)
            results.append(res)

print(num)
results.sort()
for r in results:
    print(r)
