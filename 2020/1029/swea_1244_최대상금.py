import sys
sys.stdin = open('input_1244.txt', 'r')

def convetListToNum():
    result = 0
    for i in range(lenNum):
        result += num_list[i] * 10 ** (lenNum - 1 - i)
    return result

def checkNext(n):
    if n == N:
        global max_num
        cur_result = convetListToNum()
        if cur_result > max_num:
            max_num = cur_result
    else:
        for l in range(lenNum):
            for m in range(lenNum):
                if l != m:
                    num_list[l], num_list[m] = num_list[m], num_list[l]
                    cur_result = convetListToNum()
                    cur_result = str(n) + str(cur_result)
                    if not visited.get(cur_result):
                        visited[cur_result] = 1
                        checkNext(n + 1)
                    num_list[l], num_list[m] = num_list[m], num_list[l]

T = int(input())

for tc in range(T):
    num_str, N = input().split()

    num_list = list(map(int, num_str))
    lenNum = len(num_str)
    N = int(N)

    visited = {}

    max_num = 0

    checkNext(0)

    print('#{} {}'.format(tc + 1, max_num))