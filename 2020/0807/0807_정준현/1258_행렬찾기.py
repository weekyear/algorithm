import sys
sys.stdin = open("input.txt", "r")

def get_width(x, y, map_list):
    cur_x = x
    width = 0
    while map_list[y][cur_x] != 0:
        width += 1
        cur_x += 1
    return width

def get_height(x, y, map_list):
    cur_y = y
    height = 0
    while map_list[cur_y][x] != 0:
        height += 1
        cur_y += 1
    return height

def sort_my_list(my_list):
    for i in range(len(my_list)-1):
        min_idx = i
        min_val = my_list[i]
        for j in range(i+1, len(my_list)):
            if min_val[2] > my_list[j][2] or (min_val[2] == my_list[j][2] and min_val[0] > my_list[j][0]):
                min_val = my_list[j]
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]

    square_count = 0
    w_h_list = []

    for y in range(N):
        for x in range(N):
            if map_list[y][x] != 0:
                width = get_width(x, y, map_list)
                height = get_height(x, y, map_list)
                w_h_list.append([height, width, width*height])
                square_count += 1
                for i in range(width):
                    for j in range(height):
                        map_list[y+j][x+i] = 0

    result = '#{} {} '.format(test_case, square_count)
    sort_my_list(w_h_list)
    for w, h, m in w_h_list:
        result += str(w) + ' ' + str(h) + ' '
    print(result)
