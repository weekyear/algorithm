def solution(rows, columns, queries):
    field = [[(c + 1) + r * columns for c in range(columns)] for r in range(rows)]
    answer = []

    for query in queries:
        y1, x1, y2, x2 = map(lambda x: x - 1, query)
        min_val = 0xffffff
        idx_list = []
        val_list = []
        for a in range(x1, x2 + 1):
            idx_list.append((y1, a))
            val_list.append(field[y1][a])
            if min_val > field[y1][a]:
                min_val = field[y1][a]
        for b in range(y1 + 1, y2 + 1):
            idx_list.append((b, x2))
            val_list.append(field[b][x2])
            if min_val > field[b][x2]:
                min_val = field[b][x2]
        for c in range(x2 - 1, x1 - 1, -1):
            idx_list.append((y2, c))
            val_list.append(field[y2][c])
            if min_val > field[y2][c]:
                min_val = field[y2][c]
        for d in range(y2 - 1, y1, -1):
            idx_list.append((d, x1))
            val_list.append(field[d][x1])
            if min_val > field[d][x1]:
                min_val = field[d][x1]

        for i in range(len(idx_list)):
            c_y, c_x = idx_list[i]
            field[c_y][c_x] = val_list[i - 1]

        answer.append(min_val)

    return answer