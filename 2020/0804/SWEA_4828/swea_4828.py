import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    _min = 999999999999
    _max = -999999999999

    for num in a:
        if _min > num:
            _min = num
        if _max < num:
            _max = num

    print('#{} {}'.format(test_case, _max - _min))