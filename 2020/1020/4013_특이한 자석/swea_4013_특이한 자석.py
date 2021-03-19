import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def get_wheel_idx(w_num):
    if w_num < 0:
        w_num += 4
    elif w_num > 3:
        w_num -= 4
    return w_num

def get_left_index(w_num):
    if wheel_indexes[w_num] - 2 > -1:
        return wheel_indexes[w_num] - 2
    else:
        return wheel_indexes[w_num] + 6

def get_right_index(w_num):
    if wheel_indexes[w_num] + 2 < 7:
        return wheel_indexes[w_num] + 2
    else:
        return wheel_indexes[w_num] - 6

def rotate(r_info):
    w_num, r_direc = r_info[0], r_info[1]
    visited[w_num] = 1
    l_w_idx = get_wheel_idx(w_num - 1)
    r_w_idx = get_wheel_idx(w_num + 1)

    cur_wheel_left_mag = wheels[w_num][get_left_index(w_num)]
    left_wheel_right_mag = wheels[l_w_idx][get_right_index(l_w_idx)]

    if w_num != 0 and not visited[l_w_idx] and cur_wheel_left_mag != left_wheel_right_mag:
        rotate([l_w_idx, r_direc * -1])

    cur_wheel_right_mag = wheels[w_num][get_right_index(w_num)]
    right_wheel_left_mag = wheels[r_w_idx][get_left_index(r_w_idx)]
    if w_num != 3 and not visited[r_w_idx] and cur_wheel_right_mag != right_wheel_left_mag:
        rotate([r_w_idx, r_direc * -1])

    if wheel_indexes[w_num] - r_direc < 0:
        wheel_indexes[w_num] = wheel_indexes[w_num] - r_direc + 8
    elif wheel_indexes[w_num] - r_direc > 7:
        wheel_indexes[w_num] = wheel_indexes[w_num] - r_direc - 8
    else:
        wheel_indexes[w_num] -= r_direc

for tc in range(T):
    K = int(input())
    wheels = []
    for w in range(4):
        wheels.append(list(map(int, input().split())))

    rotates = []
    for k in range(K):
        wheel_num, rotate_direction = map(int, input().split())
        rotates.append([wheel_num - 1, rotate_direction])

    wheel_indexes = [0, 0, 0, 0]

    visited = [0, 0, 0, 0]
    for r in rotates:
        visited = [0, 0, 0, 0]
        rotate(r)

    score = 0
    for w in range(len(wheel_indexes)):
        if wheels[w][wheel_indexes[w]] == 1:
            score += 1 << w

    print('#{} {}'.format(tc+1, score))