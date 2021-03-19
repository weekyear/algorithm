import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]

    flag = 0
    result = ''

    for i in range(N):
        for j in range(N-M+1):
            for k in range(M // 2):
                if str_list[i][j+k] != str_list[i][M-1+j-k]:
                    break
            else:
                flag = 1
                for m in range(M):
                    result += str_list[i][j+m]
                break

            for k in range(M // 2):
                if str_list[j+k][i] != str_list[M-1+j-k][i]:
                    break
            else:
                flag = 1
                for m in range(M):
                    result += str_list[j+m][i]
                break
        if flag: break

    print('#{} {}'.format(test_case+1, result))