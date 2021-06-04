import sys
sys.stdin = open('boj_14502.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline

N, M = map(int, readline().split())
fields = [list(map(int, readline().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

blanks = []
viruses = []
for y in range(N):
    for x in range(M):
        if not fields[y][x]:
            blanks.append((y, x))
        elif fields[y][x] == 2:
            viruses.append((y, x))


blank_num = len(blanks)
min_virus = 0xffffff

for a in range(blank_num - 2):
    for b in range(1, blank_num - 1):
        for c in range(2, blank_num):
            visited = [field[:] for field in fields]
            Q = deque()
            new_virus = 0

            visited[blanks[a][0]][blanks[a][1]], visited[blanks[b][0]][blanks[b][1]], visited[blanks[c][0]][blanks[c][1]] = 1, 1, 1

            for v_y, v_x in viruses:
                Q.append((v_y, v_x))

            while Q:
                c_y, c_x = Q.popleft()

                for d in range(4):
                    n_y, n_x = c_y + dy[d], c_x + dx[d]
                    if -1 < n_y < N and -1 < n_x < M and not visited[n_y][n_x]:
                        visited[n_y][n_x] = 2
                        new_virus += 1
                        if new_virus > min_virus:
                            Q.clear()
                            break
                        Q.append((n_y, n_x))

            if min_virus > new_virus:
                min_virus = new_virus

print(blank_num - min_virus - 3)
