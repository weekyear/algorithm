import sys
sys.stdin = open('input_02.txt', 'r')

def explore(k):
    global result
    global prev_explore
    global explore_max_k
    global explore_min_k
    cur_max_recur = 0
    for y in range(max_n - k + 1):
        for x in range(max_n - k + 1):
            recur = 0
            max_j_x, max_j_y = x + k, y + k
            for j in jongyangs:
                if x <= j[0][0] and j[0][1] <= max_j_x and y <= j[1][0] and j[1][1] <= max_j_y:
                    recur += 1

            else:
                if cur_max_recur < recur:
                    cur_max_recur = recur

    if cur_max_recur >= N - M:
        explore_max_k = k
        if result > k:
            result = k
    else:
        explore_min_k = k

    if prev_explore[0] != explore_min_k or prev_explore[1] != explore_max_k:
        prev_explore[0], prev_explore[1] = explore_min_k, explore_max_k
        explore((explore_min_k + explore_max_k) // 2)


for tc in range(int(input())):
    jongyangs = []
    N, M = map(int, input().split())

    max_n = 0

    for n in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        cur_max_n = max(x1, x2, y1, y2)
        if max_n < cur_max_n:
            max_n = cur_max_n

        jongyangs.append([[min(x1, x2), max(x1, x2)], [min(y1, y2), max(y1, y2)]])


    explore_min_k = 0
    explore_max_k = max_n

    result = 0xffffff
    prev_explore = [0, max_n]
    explore((explore_min_k + explore_max_k) // 2)

    print('#{} {}'.format(tc + 1, result))
