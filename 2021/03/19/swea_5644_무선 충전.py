import sys

sys.stdin = open('input_5644.txt', 'r')

def setNewPosistionOfUser(cur_pos, move, m_idx):
    new_y = cur_pos[0] + m_case[move[m_idx]][0]
    new_x = cur_pos[1] + m_case[move[m_idx]][1]
    if 0 < new_y < 11 and 0 < new_x < 11:
        cur_pos[0], cur_pos[1] = new_y, new_x
    else:
        new_y, new_x = cur_pos[0], cur_pos[1]
    return new_y, new_x

def getMaxValueAndIndexOfList(lst):
    idx = -1
    max_value = 0
    for c in range(len(lst)):
        if lst[c] > max_value:
            max_value = lst[c]
            idx = c

    return max_value, idx

def calculate(a_pos, b_pos):
    new_a_y, new_a_x, new_b_y, new_b_x = a_pos[0], a_pos[1], b_pos[0], b_pos[1]
    cur_a_battery, cur_b_battery = [0 for _ in range(A)], [0 for _ in range(A)]

    for a in range(A):
        battery_x, battery_y, C, P = batteries[a][0], batteries[a][1], batteries[a][2], batteries[a][3]

        if abs(new_a_y - battery_y) + abs(new_a_x - battery_x) < C + 1:
            cur_a_battery[a] = P
        if abs(new_b_y - battery_y) + abs(new_b_x - battery_x) < C + 1:
            cur_b_battery[a] = P

    max_a, used_a_idx = getMaxValueAndIndexOfList(cur_a_battery)
    max_b, used_b_idx = getMaxValueAndIndexOfList(cur_b_battery)

    if used_a_idx != used_b_idx:
        return max_a + max_b
    else:
        cur_a_battery[used_a_idx], cur_b_battery[used_b_idx] = 0, 0
        return max_a + max(max(cur_a_battery), max(cur_b_battery))

for tc in range(int(input())):
    M, A = map(int, input().split())
    a_move, b_move = list(map(int, input().split())), list(map(int, input().split()))
    batteries = [list(map(int, input().split())) for _ in range(A)]
    m_case = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
    cur_a, cur_b = [1, 1], [10, 10]

    # 시간이 0일때 계산도 해야 됨
    sum_battery = calculate(cur_a, cur_b)
    for m in range(M):
        new_a_y, new_a_x = setNewPosistionOfUser(cur_a, a_move, m)
        new_b_y, new_b_x = setNewPosistionOfUser(cur_b, b_move, m)

        sum_battery += calculate([new_a_y, new_a_x], [new_b_y, new_b_x])

    print('#{} {}'.format(tc + 1, sum_battery))