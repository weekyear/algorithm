import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

operator_dict = {
    0: '+',
    1: '-',
    2: '*',
    3: '/',
}

def calculate(o, s_num, e_num):
    if o == 0:
        return s_num + e_num
    elif o == 1:
        return s_num - e_num
    elif o == 2:
        return s_num * e_num
    else:
        return int(s_num / e_num)

def dfs(k, cur_val):
    if k == N - 1:
        global max_num
        global min_num
        if cur_val > max_num:
            max_num = cur_val
        if cur_val < min_num:
            min_num = cur_val
    else:
        for o in range(4):
            if operators[o] > 0:
                operators[o] -= 1
                new_val = calculate(o, cur_val, numbers[k+1])
                dfs(k + 1, new_val)
                operators[o] += 1

for tc in range(T):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_num = -0xffffff
    min_num = 0xffffff

    result_list = [numbers[0]]
    dfs(0, numbers[0])

    print('#{} {}'.format(tc+1, max_num - min_num))