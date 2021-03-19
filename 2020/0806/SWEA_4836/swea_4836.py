import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    _list = [[0 for _ in range(10)] for _ in range(10)]
    purple_count = 0

    for n in range(N):
        data = list(map(int, input().split()))
        r1, c1, r2, c2, color = data[0], data[1], data[2], data[3], data[4]
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if _list[x][y] == 0:
                    _list[x][y] = color
                elif _list[x][y] != color:
                    purple_count += 1
    print('#{} {}'.format(test_case, purple_count))