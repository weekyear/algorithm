import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):
    str_1 = input()
    str_2 = input()

    set_str_1 = list(set(str_1))
    dict_str_1 = {}

    max_val = 0
    for i in range(len(str_2)):
        for j in range(len(set_str_1)):
            if str_2[i] == set_str_1[j]:
                dict_str_1[str_2[i]] = dict_str_1.get(str_2[i], 0) + 1
                if dict_str_1[str_2[i]] > max_val:
                    max_val = dict_str_1[str_2[i]]

    print('#{} {}'.format(test_case+1, max_val))