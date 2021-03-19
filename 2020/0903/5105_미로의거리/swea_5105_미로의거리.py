import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(T):
    N = int(input())
    maze = []
    isFindStart = False
    cur_pt = []
    for y in range(N):
        row = input()
        maze.append(row)
        # 시작점 찾기
        if not isFindStart:
            for x in range(len(row)):
                if row[x] == '2':
                    isFindStart = True
                    cur_pt = [x, y]

    Q = [[cur_pt, 0]]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[cur_pt[1]][cur_pt[0]] = 1

    isFinished = False
    result = 0
    while Q:
        v_info = Q.pop(0)
        v = v_info[0]
        step = v_info[1]

        for d in range(4):
            n_x = v[0] + dx[d]
            n_y = v[1] + dy[d]

            if -1 < n_x < N and -1 < n_y < N and not visited[n_y][n_x]:
                if maze[n_y][n_x] == '0':
                    Q.append([[n_x, n_y], step+1])
                    visited[n_y][n_x] = 1
                elif maze[n_y][n_x] == '3':
                    isFinished = True
                    result = step

    print('#{} {}'.format(tc+1, result))