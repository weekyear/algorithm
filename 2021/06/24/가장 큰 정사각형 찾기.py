def solution(board):
    len_y, len_x = len(board), len(board[0])
    visited = [[0 for _ in range(len_x)] for _ in range(len_y)]

    max_len = 0

    for y in range(len_y):
        visited[y][0] = board[y][0]
        if visited[y][0] > max_len:
            max_len = visited[y][0]

    for x in range(len_x):
        visited[0][x] = board[0][x]
        if visited[0][x] > max_len:
            max_len = visited[0][x]

    for y in range(1, len_y):
        for x in range(1, len_x):
            if board[y][x] == 1:
                visited[y][x] = min(visited[y - 1][x], visited[y][x - 1], visited[y - 1][x - 1]) + 1

                if visited[y][x] > max_len:
                    max_len = visited[y][x]
    return max_len ** 2