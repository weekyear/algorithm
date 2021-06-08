def solution(lottos, win_nums):
    win_visited = [0 for _ in range(46)]
    zero_num = 0
    win_num = 0
    for win in win_nums:
        win_visited[win] = 1

    for lotto in lottos:
        if lotto != 0:
            if win_visited[lotto]:
                win_num += 1
        else:
            zero_num += 1

    max_win, min_win = zero_num + win_num, win_num

    answer = [7 - max_win if max_win > 1 else 6, 7 - min_win if min_win > 1 else 6]
    return answer