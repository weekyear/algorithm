import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(_x, _y, _value, k):
    if k < 6:
        idx_info = _x * 100 + _y * 10 + k
        if idx_info not in memory.get(_value, []):
            memory[_value] = memory.get(_value, []) + [idx_info]
            for d in range(4):
                new_x = _x + dx[d]
                new_y = _y + dy[d]

                if -1 < new_x < 4 and -1 < new_y < 4:
                    dfs(new_x, new_y, _value * 10 + table[new_y][new_x], k + 1)
    else:
        result.add(_value)


for tc in range(T):
    table = [list(map(int, input().split())) for _ in range(4)]
    memory = {}
    result = set()

    for y in range(4):
        for x in range(4):
            value = table[y][x]
            dfs(x, y, value, 0)

    print('#{} {}'.format(tc+1, len(result)))