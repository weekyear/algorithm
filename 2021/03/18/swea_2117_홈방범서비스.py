import sys
sys.stdin = open('input_2117.txt', 'r')

def operation_expense(k):
    return k * k + (k - 1) * (k - 1)

# 온갖 쇼를 다 벌였지만 실패하였다...반례도 모르겠다.
# for tc in range(int(input())):
#     N, M = map(int, input().split())
#     homes = [list(map(int, input().split())) for _ in range(N)]
#
#     result = 0
#     for n in range(N + 2, -1, -1):
#         cur_max_result = 0
#         for y in range(N):
#             for x in range(N):
#                 visited = [[0 for _ in range(N)] for _ in range(N)]
#                 cur_result = 0
#                 for n_y in range(-n+1, n):
#                     cur_y = y + n_y
#                     diff = abs(abs(n_y) - n)
#                     for n_x in range(-diff+1, diff):
#                         cur_x = x + n_x
#                         if -1 < cur_y < N and -1 < cur_x < N:
#                             visited[cur_y][cur_x] = 1
#                             if homes[cur_y][cur_x] == 1:
#                                 cur_result += 1
#                 if cur_result > cur_max_result:
#                     cur_max_result = cur_result
#         if cur_max_result * M - operation_expense(n) > 0:
#             result = cur_max_result
#             break
#
#     print('#{} {}'.format(tc + 1, result))

# 타협하고 코드를 10포인트 주고 샀다.
for tc in range(int(input())):
    N, M = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(N)]
    homes = []

    for y in range(N):
        for x in range(N):
            if field[y][x]:
                homes.append((y, x))

    max_profit = len(homes) * M

    for k in range(N + 2, 0, -1):
        cur_expense = operation_expense(k)
        if max_profit - cur_expense >= 0:
            num_max_home = 0
            for y in range(N):
                for x in range(N):
                    num_home = 0
                    for h_y, h_x in homes:
                        if abs(y - h_y) + abs(x - h_x) < k:
                            num_home += 1
                    if num_max_home < num_home and num_home * M >= cur_expense:
                        num_max_home = num_home
            if num_max_home:
                break

    print('#{} {}'.format(tc + 1, num_max_home))