import sys
sys.stdin = open('input_2.txt', 'r')

def cal_regist_y(y, x):
    cur_r = 1
    while field[y + cur_r][x]:
        cur_r += 1

        if y + cur_r > N - 1:
            break

    return cur_r - 1

def cal_regist_x(y, x):
    cur_r = 1
    while field[y][x + cur_r]:
        cur_r += 1

        if x + cur_r > N - 1:
            break

    return cur_r - 1

for tc in range(10):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    for s in range(N):
        cur_pos = 0
        cur_m = 1
        cur_f = 1
        if field[0][s] == 1:
            while cur_pos < N - 1:
                if field[cur_pos + 1][s]:
                    next_regist = cal_regist_y(cur_pos, s)
                    for n in range(cur_pos + 1):
                        if n < cur_pos - cur_m + 1:
                            field[n][s] = 0
                        else:
                            field[n][s] = 1
                    if cur_f > next_regist:
                        cur_f += next_regist
                        cur_pos += next_regist
                        cur_m += next_regist
                    else:
                        break
                else:
                    cur_f *= 1.9
                    cur_pos += 1
            else:
                for n in range(cur_pos + 1):
                    if n < cur_pos - cur_m + 1:
                        field[n][s] = 0
                    else:
                        field[n][s] = 1


    for s in range(N):
        cur_pos_x = 0
        cur_m_x = 1
        cur_f_x = 1
        if field[s][0] == 1:
            while cur_pos_x < N - 1:
                if field[s][cur_pos_x + 1]:
                    next_regist = cal_regist_x(s, cur_pos_x)
                    for n in range(cur_pos_x + 1):
                        if n < cur_pos_x - cur_m_x + 1:
                            field[s][n] = 0
                        else:
                            field[s][n] = 1
                    if cur_f_x > next_regist:
                        cur_f_x += next_regist
                        cur_pos_x += next_regist
                        cur_m_x += next_regist
                    else:
                        break
                else:
                    cur_f_x *= 1.9
                    cur_pos_x += 1
            else:
                for n in range(cur_pos_x + 1):
                    if n < cur_pos_x - cur_m_x + 1:
                        field[s][n] = 0
                    else:
                        field[s][n] = 1
    result2 = 0
    for y in range(N):
        result2 += field[y][N - 1]
    print('#{} {} {}'.format(tc + 1, sum(field[N - 1]), result2))