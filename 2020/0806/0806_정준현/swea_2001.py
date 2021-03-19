import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    if test_case == 2:
        pass
    N, M = map(int, input().split())
    area = []
    for i in range(N):
        area.append(list(map(int, input().split())))

    _max = 0
    for x in range(N-M+1):
        cur = 0
        for i in range(M):
            for j in range(M):
                cur += area[x+i][j]
        else:
            if _max < cur:
                _max = cur

        for y in range(N-M):
            for i in range(M):
                cur += area[x+i][y+M] - area[x+i][y]
            if _max < cur:
                _max = cur
    print('#{} {}'.format(test_case, _max))

    # 4중 반복문 => 좋지않아..
    # T = int(input())
    # # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    # for test_case in range(1, T + 1):
    #     N, M = map(int, input().split())
    #     area = []
    #     for i in range(N):
    #         area.append(list(map(int, input().split())))
    #
    #     _max = 0
    #     for x in range(N - M + 1):
    #         for y in range(N - M + 1):
    #             temp = 0
    #             for i in range(M):
    #                 for j in range(M):
    #                     temp += area[x + i][y + j]
    #             if _max < temp:
    #                 _max = temp
    #     print('#{} {}'.format(test_case, _max))