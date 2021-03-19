import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):
    str_1 = input()
    str_2 = input()

    flag = 0

    for i in range(len(str_2) - len(str_1)+1):
        for j in range(len(str_1)):
            if str_1[j] != str_2[i+j]:
                break
        else:
            flag = 1
            break

    print('#{} {}'.format(test_case+1, flag))