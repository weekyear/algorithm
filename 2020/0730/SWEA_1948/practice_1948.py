import sys
sys.stdin = open("input.txt", "r")

def calculate_days():
    day = 0
    
    for k in range(date_list[0][0], date_list[1][0] + 1):
        if k == date_list[0][0]:
            day += dict_month[k] - date_list[0][1] + 1
        elif k == date_list[1][0]:
            day += date_list[1][1]
        else:
            day += dict_month[k]
    
    return day

dict_month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

T = int(input())

for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    date_list = []
    for i in range(0, 4, 2):
        date_list.append([data[i], data[i+1]])

    print('#{} {}'.format(test_case, calculate_days()))