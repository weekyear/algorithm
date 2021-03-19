import sys


sys.stdin = open("sample_input.txt", "r")

def selectionSort(_list):
    for i in range(len(_list)-1):
        min_idx = i
        min_val = _list[i]
        for j in range(i, len(_list)):
            if min_val > _list[j]:
                min_val = _list[j]
                min_idx = j
        _list[i], _list[min_idx] = _list[min_idx], _list[i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    _list = list(map(int, input().split()))

    selectionSort(_list)
    new_list = []
    for i in range(len(_list) // 2):
        new_list.append(_list[len(_list)-1-i])
        new_list.append(_list[i])
    if len(_list) % 2 != 0:
        new_list.append(_list[len(_list) // 2 + 1])

    result = '#{} '.format(test_case)
    for i in range(10):
        result += str(new_list[i])
        if i != len(new_list)-1:
            result += ' '

    print(result)