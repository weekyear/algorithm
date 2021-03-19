import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    test_case = int(input())
    radder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if radder[99][i] == 2:
            x_idx = i
            break

    depth = 98
    while depth > 0:
        x_left = 0
        x_right = 0

        if x_idx-1 > -1:
            x_left = radder[depth][x_idx-1]
        if x_idx+1 < 100:
            x_right = radder[depth][x_idx+1]

        if x_left:
            x_idx -= 1
            while radder[depth - 1][x_idx] != 1:
                x_idx -= 1
        elif x_right:
            x_idx += 1
            while radder[depth - 1][x_idx] != 1:
                x_idx += 1

        depth -= 1

    print('#{} {}'.format(test_case, x_idx))

