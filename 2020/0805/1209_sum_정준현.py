import sys

sys.stdin = open('input.txt', 'r')

for test_case in range(10):
    _ = input()

    data = [list(map(int, input().split())) for _ in range(100)]

    _max = 0
    for i in range(100):
        col_max = 0
        row_max = 0
        for j in range(100):
            row_max += data[i][j]
            col_max += data[j][i]
        if col_max > _max:
            _max = col_max
        if row_max > _max:
            _max = row_max

    dig_max = 0
    rev_dig_max = 0
    for i in range(100):
        dig_max += data[99-i][99-i]
        rev_dig_max += data[99-i][99-i]

    if dig_max > _max:
        _max = dig_max
    if rev_dig_max > _max:
        _max = rev_dig_max

    print(_max)