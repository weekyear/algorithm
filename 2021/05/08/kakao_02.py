places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = []
for place in places:
    is_close = False
    for y in range(5):
        for x in range(5):
            if place[y][x] == 'P':
                for d in range(4):
                    for p in range(1, 3):
                        n_y, n_x = y + p * dy[d], x + p * dx[d]
                        if -1 < n_y < 5 and -1 < n_x < 5:
                            if place[n_y][n_x] == 'X':
                                break
                            elif p == 1 and place[n_y][n_x] == 'O':
                                if d < 2:
                                    n_n_x_1, n_n_x_2 = n_x + 1, n_x - 1
                                    if -1 < n_n_x_1 < 5 and place[n_y][n_n_x_1] == 'P':
                                        is_close = True
                                        break
                                    if -1 < n_n_x_2 < 5 and place[n_y][n_n_x_2] == 'P':
                                        is_close = True
                                        break
                                else:
                                    n_n_y_1, n_n_y_2 = n_y + 1, n_y - 1
                                    if -1 < n_n_y_1 < 5 and place[n_n_y_1][n_x] == 'P':
                                        is_close = True
                                        break
                                    if -1 < n_n_y_2 < 5 and place[n_n_y_2][n_x] == 'P':
                                        is_close = True
                                        break
                            elif place[n_y][n_x] == 'P':
                                is_close = True
                                break
                    if is_close:
                        break
            if is_close:
                break
        if is_close:
            break

    if is_close:
        answer.append(0)
    else:
        answer.append(1)
print(answer)