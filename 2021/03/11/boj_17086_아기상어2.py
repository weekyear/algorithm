import sys
sys.stdin = open('input_17086.txt', 'r')


N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]
dx = [0, 0, -1, 1, 1, 1, -1, -1]

result = 0
Q = []
# 상어를 중심으로 1씩 더해가면서 채워준다.
for y in range(N):
    for x in range(M):
        if field[y][x]:
            Q.append((y, x, 0))

while Q:
    cur_y, cur_x, k = Q.pop(0)

    for d in range(8):
        n_y = cur_y + dy[d]
        n_x = cur_x + dx[d]

        if -1 < n_y < N and -1 < n_x < M and not field[n_y][n_x]:
            field[n_y][n_x] = k + 1
            Q.append((n_y, n_x, k + 1))
            if result < k + 1:
                result = k + 1

print(result)

# 모든 위치를 중심으로 BFS로 푸니깐 82% 째에서 계속 시간초과가 뜸
# for y in range(N):
#     for x in range(M):
#         visited = [[0 for _ in range(M)] for _ in range(N)]
#         visited[y][x] = 1
#         result = 0
#         if not field[y][x]:
#             Q = deque([(y, x, 0)])
#
#             while Q:
#                 cur_y, cur_x, k = Q.popleft()
#                 for d in range(8):
#                     n_y = cur_y + dy[d]
#                     n_x = cur_x + dx[d]
#
#                     if -1 < n_y < N and -1 < n_x < M and not visited[n_y][n_x]:
#                         if not field[n_y][n_x]:
#                             visited[n_y][n_x] = 1
#                             Q.append((n_y, n_x, k + 1))
#                         else:
#                             result = k + 1
#                             if max_result < result:
#                                 max_result = result
#                             break
#                 if result:
#                     break
# print(max_result)