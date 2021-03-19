import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    _input = input()

    _max = 0
    num_list = [0] * 10

    for char in _input:
        num = int(char)
        num_list[num] += 1

    freq_num = 0
    for i in range(len(num_list)):
        if num_list[i] >= freq_num and i > _max:
            freq_num = num_list[i]
            _max = i

    print('#{} {} {}'.format(test_case, _max, freq_num))