import sys
sys.stdin = open('boj_16973.txt', 'r')

from collections import deque
readline = sys.stdin.readline

# 정보 받기
N, M = map(int, readline().split())
field = [list(map(int, readline().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, readline().split())
# 좌표 정보 동기화
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

visited = [[0] * M for _ in range(N)]
# 벽에 가로막히는 부분은 미리 방문처리 하기
for n in range(N):
    for m in range(M):
        if field[n][m] == 1:
            for w in range(W):
                for h in range(H):
                    if -1 < n - h < N and -1 < m - w < M:
                        visited[n - h][m - w] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = -1

Q = deque([(Sr, Sc, 0)])
visited[Sr][Sc] = 1

while Q:
    r, c, e = Q.popleft()

    for d in range(4):
        n_r, n_c = r + dy[d], c + dx[d]

        if -1 < n_r < N - H + 1 and -1 < n_c < M - W + 1 and not visited[n_r][n_c]:
            visited[n_r][n_c] = 1
            # 도착하면 result에 값 갱신
            if n_r == Fr and n_c == Fc:
                result = e + 1
                break

            Q.append((n_r, n_c, e + 1))
    # BFS로 돌았기 때문에 결과값이 갱신되면 그 결과가 최소 비용이다.
    if result != -1:
        break

print(result)
