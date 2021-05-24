import sys
sys.stdin = open('boj_6603.txt', 'r')

import sys
readline = sys.stdin.readline

def dfs(lst, c, N):
    if len(lst) == 6:
        infos[N].append(lst[:])
        return

    for i in range(c, N - 4 + len(lst)):
        lst.append(i)
        dfs(lst, i + 1, N)
        lst.pop()

infos = [[] for _ in range(14)]
visited = []

for n in range(7, 14):
    dfs([], 1, n)

info = list(map(int, input().split()))
while info[0] != 0:
    for idxs in infos[info[0]]:
        for idx in idxs:
            print(info[idx], end=' ')
        print()
    info = list(map(int, input().split()))
    print()