import sys
sys.stdin = open('boj_16973.txt', 'r')

from collections import deque
readline = sys.stdin.readline

N, M = map(int, readline().split())
field = [list(map(int, readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
walls = []

for n in range(N):
    for m in range(M):
        if field[n][m] == 1:
            walls.append((n, m))

H, W, Sr, Sc, Fr, Fc = map(int, readline().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

def existsWalls(r, c):
    for wall in walls:
        w_r, w_c = wall
        if c <= w_c < c + W and r <= w_r < r + H:
            return True
    return False

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = -1

Q = deque()
Q.append((Sr, Sc, 0))
visited[Sr][Sc] = 1

while Q:
    r, c, e = Q.popleft()

    for d in range(4):
        n_r, n_c = r + dy[d], c + dx[d]

        if -1 < n_r < N - H + 1 and -1 < n_c < M - W + 1 and not visited[n_r][n_c] and not existsWalls(n_r, n_c):
            visited[n_r][n_c] = 1
            if n_r == Fr and n_c == Fc:
                result = e + 1
                break

            Q.append((n_r, n_c, e + 1))
    if result != -1:
        break

print(result)
