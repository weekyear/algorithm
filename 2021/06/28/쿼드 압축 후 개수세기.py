def solution(arr):
    len_a = len(arr)
    answer = [0, 0]

    def quad(start, end):
        cur_num = arr[start[0]][start[1]]
        is_united = True
        for y in range(start[0], end[0] + 1):
            for x in range(start[1], end[1] + 1):
                if arr[y][x] != cur_num:
                    is_united = False
                    break
            if not is_united:
                half = (end[0] - start[0] + 1) // 2
                quad(start, (start[0] + half - 1, start[1] + half - 1))
                quad((start[0] + half, start[1]), (start[0] + 2 * half - 1, start[1] + half - 1))
                quad((start[0], start[1] + half), (start[0] + half - 1, start[1] + 2 * half - 1))
                quad((start[0] + half, start[1] + half), (start[0] + 2 * half - 1, start[1] + 2 * half - 1))
                break
        else:
            answer[cur_num] += 1

    quad((0, 0), (len_a - 1, len_a - 1))
    return answer