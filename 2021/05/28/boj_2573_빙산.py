import sys

sys.stdin = open('boj_2573.txt', 'r')

import sys

sys.setrecursionlimit(20000)
readline = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())

fields = [list(map(int, readline().split())) for _ in range(N)]
ices = []

# 빙산에 대한 정보를 ices 리스트에 넣어둔다.
for n in range(N):
    for m in range(M):
        if fields[n][m]:
            ices.append((n, m))

isFinished = False
year = 0

# 빙산이 몇 개 연결되어 있는지 계산해주는 함수
def get_connected_num(c_y, c_x, visited):
    cur_added = 0
    visited[c_y][c_x] = 1
    for c_d in range(4):
        n_y, n_x = c_y + dy[c_d], c_x + dx[c_d]

        if -1 < n_y < N and -1 < n_x < M and not visited[n_y][n_x] and fields[n_y][n_x]:
            cur_added += get_connected_num(n_y, n_x, visited)
    return cur_added + 1


while ices:
    year += 1
    # 이번 턴에 빙산이 다 녹는 위치를 담아두는 리스트
    zero_ices = []
    new_ices = []

    # 빙산 목록에서 하나씩 빼서 빙산을 녹이는 과정
    while ices:
        cur_y, cur_x = ices.pop()

        for d in range(4):
            new_y, new_x = cur_y + dy[d], cur_x + dx[d]
            if -1 < new_y < N and -1 < new_x < M and not fields[new_y][new_x]:
                fields[cur_y][cur_x] -= 1
                if fields[cur_y][cur_x] == 0:
                    # 이번 턴에 얼음이 다 녹은 위치는 다른 빙산들에 영향을 주면 안 되기 때문에 0이 아닌 -1을 표시해준다.
                    fields[cur_y][cur_x] = -1
                    zero_ices.append((cur_y, cur_x))
                    break
        else:
            new_ices.append((cur_y, cur_x))

    # 남은 빙산이 없다면 종료
    if len(new_ices) == 0:
        year = 0
        break

    # 이번 턴에 다 녹은 빙산의 위치 값을 0으로 바꿔줌
    for z_y, z_x in zero_ices:
        fields[z_y][z_x] = 0

    # 지금 빙산들이 다 연결되어 있는지 계산
    cur_num = get_connected_num(new_ices[0][0], new_ices[0][1], [[0 for _ in range(M)] for _ in range(N)])
    # 현재 남아 있는 빙산의 수와 임의의 위치에서 DFS를 순회한 결과가 다르다면 끝
    if cur_num != len(new_ices):
        break

    ices = new_ices

print(year)