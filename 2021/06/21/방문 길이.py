def solution(dirs):
    answer = 0
    visited = [[[0 for _ in range(4)] for _ in range(11)] for _ in range(11)]
    idxs = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    pos = (5, 5)

    for d in dirs:
        c_y, c_x = pos
        n_y, n_x = c_y + dy[idxs[d]], c_x + dx[idxs[d]]
        if -1 < n_y < 11 and -1 < n_x < 11:
            coun_dir_idx = idxs[d] - 1 if idxs[d] % 2 else idxs[d] + 1
            if not visited[c_y][c_x][idxs[d]] and not visited[n_y][n_x][coun_dir_idx]:
                visited[c_y][c_x][idxs[d]] = 1
                visited[n_y][n_x][coun_dir_idx] = 1
                answer += 1
            pos = (n_y, n_x)

    return answer