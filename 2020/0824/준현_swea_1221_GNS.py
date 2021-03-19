import sys

sys.stdin = open("input.txt", "r")

T = int(input())

str_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
str_dict = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}

def getIntNum(str_num):
    int_num = str_dict[str_num]
    return int_num

for test_case in range(1, T + 1):
    len_nums = int(list(input().split())[1])
    num_list = list(input().split())

    check_list = [0 for _ in range(10)]

    for i in range(len_nums):
        check_list[getIntNum(num_list[i])] += 1

    print('#{}'.format(test_case))
    for k in range(10):
        print((str_list[k] + ' ')*check_list[k], end='')
    print()