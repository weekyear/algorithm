import sys
sys.stdin = open('boj_10451.txt', 'r')

from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.insert(0, -1)
    visited = [0] * (N + 1)

    result = 0

    for n in range(1, N + 1):
        if not visited[n]:
            Q = deque([n])

            while Q:
                cur_n = Q.popleft()

                if not visited[lst[cur_n]]:
                    visited[lst[cur_n]] = 1
                    if lst[cur_n] == n:
                        result += 1
                    else:
                        Q.append(lst[cur_n])

    print(result)