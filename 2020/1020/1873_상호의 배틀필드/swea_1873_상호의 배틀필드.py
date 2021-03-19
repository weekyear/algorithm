import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def isPlayer(char):
    if char == '<' or char == '^' or char == 'v' or char == '>':
        return True
    return False

def shoot():
    if p_info[2] == '^':
        direc = [0, -1]
    elif p_info[2] == 'v':
        direc = [0, 1]
    elif p_info[2] == '<':
        direc = [-1, 0]
    elif p_info[2] == '>':
        direc = [1, 0]

    shoot_pos = [p_info[0], p_info[1]]

    while not (field[shoot_pos[1]][shoot_pos[0]] == '*' or field[shoot_pos[1]][shoot_pos[0]] == '#'):
        shoot_pos[0] += direc[0]
        shoot_pos[1] += direc[1]

        if not (-1 < shoot_pos[0] < W and -1 < shoot_pos[1] < H):
            return

    if field[shoot_pos[1]][shoot_pos[0]] == '*':
        field[shoot_pos[1]][shoot_pos[0]] = '.'


for tc in range(T):
    H, W = map(int, input().split())

    field = [list(input()) for _ in range(H)]

    N = int(input())
    command = input()

    p_info = [0, 0, '']

    # 전차 현재 위치 찾기
    for h in range(H):
        for f in range(len(field[h])):
            if isPlayer(field[h][f]):
                p_info = [f, h, field[h][f]]
                break

    # 명령 수행
    for n in range(N):
        if command[n] == 'S':
            shoot()
        else:
            if command[n] == 'U':
                new_pos = [p_info[0], p_info[1] - 1]
                new_player = '^'
            elif command[n] == 'D':
                new_pos = [p_info[0], p_info[1] + 1]
                new_player = 'v'
            elif command[n] == 'L':
                new_pos = [p_info[0] - 1, p_info[1]]
                new_player = '<'
            elif command[n] == 'R':
                new_pos = [p_info[0] + 1, p_info[1]]
                new_player = '>'
            if -1 < new_pos[0] < W and -1 < new_pos[1] < H and field[new_pos[1]][new_pos[0]] == '.':
                field[new_pos[1]][new_pos[0]] = new_player
                field[p_info[1]][p_info[0]] = '.'
                p_info = [new_pos[0], new_pos[1], new_player]
            else:
                field[p_info[1]][p_info[0]] = new_player
                p_info[2] = new_player

    print('#{}'.format(tc + 1), end=' ')
    for f in field:
        for char in f:
            print(char, end='')
        print()