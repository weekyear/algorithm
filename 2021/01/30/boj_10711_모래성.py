import sys

sys.stdin = open('input_10711.txt', 'r')

from collections import deque

H, W = map(int, input().split())

sand_castle = [[int(i) if i.isnumeric() else i for i in input()] for _ in range(H)]

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

Q = deque()

cur_wave_num = 0

wave_list = [[9 for _ in range(W)] for _ in range(H)]

for h in range(1, H - 1):
    for w in range(1, W - 1):
        if sand_castle[h][w] != '.':
            cur_num = sand_castle[h][w]
            num_blank = 0
            for d in range(8):
                n_y = h + dy[d]
                n_x = w + dx[d]
                if -1 < n_x < W and -1 < n_y < H:
                    if sand_castle[n_y][n_x] == '.':
                        num_blank += 1
                    if num_blank >= cur_num:
                        Q.append([h, w, 1])
                        wave_list[h][w] = 9
                        break
            else:
                wave_list[h][w] = num_blank

while Q:
    c_h, c_w, cur_wave = Q.popleft()
    if cur_wave > cur_wave_num:
        cur_wave_num = cur_wave

    for d in range(8):
        n_y = c_h + dy[d]
        n_x = c_w + dx[d]
        if wave_list[n_y][n_x] != 9:
            wave_list[n_y][n_x] += 1

            if wave_list[n_y][n_x] >= sand_castle[n_y][n_x]:
                Q.append([n_y, n_x, cur_wave + 1])
                wave_list[n_y][n_x] = 9

print(cur_wave_num)


# blank_list = [[1 for _ in range(W)] for _ in range(H)]
#
# dy = [-1, 1, 0, 0, -1, -1, 1, 1]
# dx = [0, 0, -1, 1, -1, 1, -1, 1]
#
# Q = deque()
#
# for h in range(H):
#     for w in range(W):
#         if sand_castle[h][w] == '.':
#             blank_list[h][w] = 0
#         else:
#             Q.append([h, w, 0])
#
# cur_wave_num = 0
#
# delete_list = []
# while Q:
#     c_h, c_w, cur_wave = Q.popleft()
#     if cur_wave_num < cur_wave:
#         if not delete_list:
#             break
#         else:
#             cur_wave_num = cur_wave
#             for d_pos in delete_list:
#                 blank_list[d_pos[0]][d_pos[1]] = 0
#             delete_list.clear()
#
#     cur_num = int(sand_castle[c_h][c_w])
#     num_blank = 0
#     for d in range(8):
#         n_y = c_h + dy[d]
#         n_x = c_w + dx[d]
#         if blank_list[n_y][n_x] == 0:
#             num_blank += 1
#         if num_blank >= cur_num:
#             delete_list.append([c_h, c_w])
#             break
#
#         if 7 - d + num_blank < cur_num:
#             Q.append([c_h, c_w, cur_wave + 1])
#             break
#     else:
#         if num_blank < sand_castle[c_h][c_w]:
#             Q.append([c_h, c_w, cur_wave + 1])
#         else:
#             delete_list.append([c_h, c_w])



# while delete_list:
#     for elem in delete_list:
#         blank_list[elem[0]][elem[1]] = 0
#     delete_list.clear()
#     cur_wave_num += 1
#     for h in range(1, H - 1):
#         for w in range(1, W -1):
#             cur_num = 0
#             if blank_list[h][w] == 0:
#                 continue
#
#             cur_num = int(sand_castle[h][w])
#             num_blank = 0
#             for d in range(8):
#                 n_y = h + dy[d]
#                 n_x = w + dx[d]
#                 if blank_list[n_y][n_x] == 0:
#                     num_blank += 1
#                 if num_blank == cur_num:
#                     delete_list.append([h, w])
#                     break
#     if not delete_list:
#         cur_wave_num -= 1
