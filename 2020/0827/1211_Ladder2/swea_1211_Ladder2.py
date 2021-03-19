import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    test_case = int(input())
    radder = [list(map(int, input().split())) for _ in range(100)]\

    min_idx = -1
    min_val = 999999
    for i in range(100):
        if radder[0][i] == 1:
            count = 0
            depth = 0
            x_idx = i
            while depth < 99:
                x_left = 0
                x_right = 0

                if x_idx-1 > -1:
                    x_left = radder[depth][x_idx-1]
                if x_idx+1 < 100:
                    x_right = radder[depth][x_idx+1]

                if x_left:
                    x_idx -= 1
                    while radder[depth + 1][x_idx] != 1:
                        x_idx -= 1
                        count += 1
                elif x_right:
                    x_idx += 1
                    while radder[depth + 1][x_idx] != 1:
                        x_idx += 1
                        count += 1

                if count >= min_val:
                    break
                depth += 1
            else:
                if min_val > count:
                    min_val = count
                    min_idx = i

    print('#{} {}'.format(test_case, min_idx))

