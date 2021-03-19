import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for x in range(N):
        cur_type = 0
        for y in range(N):
            m_type = table[y][x]

            if cur_type == 0 and m_type == 1:
                cur_type = 1
            elif cur_type == 1 and m_type == 2:
                result += 1
                cur_type = 0

    print('#{} {}'.format(tc, result))