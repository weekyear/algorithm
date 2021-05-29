import sys
sys.stdin = open('boj_9205.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline
t = int(input())

def can_go(a_x, a_y, b_x, b_y):
    if abs(a_y - b_y) + abs(a_x - b_x) <= 1000:
        return True
    else:
        return False

for _ in range(t):
    n = int(input())

    stores = [list(map(int, readline().split())) for _ in range(n + 2)]
    visited = [0] * (n + 2)
    cur = 0
    Q = deque([(stores[0][0], stores[0][1], 0)])
    visited[0] = 1
    isFinished = False

    while Q:
        x, y, idx = Q.popleft()

        for i in range(n + 2):
            if i != idx and not visited[i] and can_go(x, y, stores[i][0], stores[i][1]):
                visited[i] = 1
                if i == n + 1:
                    isFinished = True
                Q.append((stores[i][0], stores[i][1], i))

        if isFinished:
            break

    print("happy" if isFinished else "sad")