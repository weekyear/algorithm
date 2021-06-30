def solution(M, N, input_board):
    answer = 0
    is_finished = False
    board = [list(row) for row in input_board]
    while not is_finished:
        is_finished = True
        del_lst = []
        for y in range(M):
            for x in range(N):
                cur_type = board[y][x]
                nyx = [(y + 1, x), (y, x + 1), (y + 1, x + 1)]
                if cur_type == '':
                    continue

                is_deleted = True
                for item in nyx:
                    n_y, n_x = item
                    if -1 < n_y < M and -1 < n_x < N:
                        if board[n_y][n_x] != cur_type:
                            is_deleted = False
                    else:
                        is_deleted = False

                if is_deleted:
                    is_finished = False
                    del_lst.append((y, x))

                    for item in nyx:
                        n_y, n_x = item
                        del_lst.append((n_y, n_x))
        else:
            if del_lst:
                for item in del_lst:
                    del_y, del_x = item
                    board[del_y][del_x] = ''

                answer = 0
                for n in range(N):
                    new_lst = []
                    for m in range(M - 1, -1, -1):
                        if board[m][n] != '':
                            new_lst.append(board[m][n])
                            board[m][n] = ''

                    for l in range(len(new_lst)):
                        board[M - 1 - l][n] = new_lst[l]
                    answer += M - len(new_lst)
    return answer