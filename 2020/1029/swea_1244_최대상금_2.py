import sys
sys.stdin = open('input_1244.txt', 'r')

def convetListToNum():
    result = 0
    for i in range(lenNum):
        result += num_list[i] * 10 ** (lenNum - 1 - i)
    return result

def checkNext(n):
    global isMaxRemainNum
    if n == N:
        global max_num
        cur_result = convetListToNum()
        if cur_result > max_num:
            max_num = cur_result
    else:
        for l in range(lenNum):
            if isMaxRemainNum != -1:
                break
            for m in range(lenNum):
                if l != m:
                    num_list[l], num_list[m] = num_list[m], num_list[l]
                    cur_result = convetListToNum()
                    if cur_result == max_result:
                        isMaxRemainNum = n + 1
                    result_key = str(n) + str(cur_result)
                    if not visited.get(result_key):
                        visited[result_key] = 1
                        if isMaxRemainNum == -1:
                            checkNext(n + 1)
                        else:
                            break
                    num_list[l], num_list[m] = num_list[m], num_list[l]

T = int(input())

for tc in range(T):
    num_str, N = input().split()

    num_list = list(map(int, num_str))
    lenNum = len(num_str)

    isMaxRemainNum = -1

    N = int(N)

    visited = {}

    max_num = 0

    max_num_list = list(reversed(sorted(num_list)))
    max_result = 0
    for i in range(lenNum):
        max_result += max_num_list[i] * 10 ** (lenNum - 1 - i)

    checkNext(0)

    if isMaxRemainNum != -1:
        max_num = max_result
        if (N - isMaxRemainNum) % 2:
            final_result = 0
            for l in range(lenNum):
                if final_result == max_result:
                    break
                for m in range(lenNum):
                    if l != m:
                        max_num_list[l], max_num_list[m] = max_num_list[m], max_num_list[l]
                        cur_result = 0
                        for i in range(lenNum):
                            cur_result += max_num_list[i] * 10 ** (lenNum - 1 - i)
                        if cur_result > final_result:
                            final_result = cur_result
                        elif final_result == max_result:
                            break
                        max_num_list[l], max_num_list[m] = max_num_list[m], max_num_list[l]
            max_num = final_result

    print('#{} {}'.format(tc + 1, max_num))