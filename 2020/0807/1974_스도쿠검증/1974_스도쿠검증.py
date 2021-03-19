import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case = []
    isSuccess = True
    for i in range(9):
        case.append(list(map(int, input().split())))

    # 세로, 가로 동시에 찾기
    for y in range(9):
        if not isSuccess: break
        ver_check = 0
        hor_check = 0
        for x in range(9):
            if not hor_check & (1<<(case[x][y]-1)):
                hor_check += 1<<(case[x][y]-1)
            if not ver_check & (1 << (case[y][x] - 1)):
                ver_check += 1 << (case[y][x] - 1)
        for i in range(9):
            if not hor_check & (1<<i):
                isSuccess = False
                break
            if not ver_check & (1<<i):
                isSuccess = False
                break

    # 영역 찾기
    for x in range(0, 7, 3):
        if not isSuccess: break
        for y in range(0, 7, 3):
            if not isSuccess: break
            sqr_check = 0
            for i in range(3):
                for j in range(3):
                    if not sqr_check & (1 << (case[x+i][y+j] - 1)):
                        sqr_check +=  1<<(case[x+i][y+j]-1)
        for i in range(9):
            if not sqr_check & (1<<i):
                isSuccess = False
                break

    print('#{} {}'.format(test_case, int(isSuccess)))