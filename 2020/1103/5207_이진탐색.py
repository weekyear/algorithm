import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))
    m_list = list(map(int, input().split()))

    count = 0

    for m in m_list:
        low = 0
        high = N - 1
        flag = 0
        while low <= high:
            mid = (low + high) // 2

            if n_list[mid] == m:
                count += 1
                break
            elif n_list[mid] > m:
                high = mid - 1
                if flag == 1: break
                flag = 1
            else:
                low = mid + 1
                if flag == 2: break
                flag = 2

    print('#{} {}'.format(tc+1, count))