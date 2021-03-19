import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def insertionSort(my_list):
    for i in range(1, len(my_list)):
        val = my_list[i]
        idx = i
        while idx > 0 and my_list[idx - 1] < val:
            my_list[idx] = my_list[idx - 1]
            idx -= 1
        my_list[idx] = val

for tc in range(T):
    N, M = map(int, input().split())

    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    insertionSort(containers)
    insertionSort(trucks)

    m_idx = 0
    result = 0
    for n in range(N):
        if m_idx == M:
            break
        if containers[n] <= trucks[m_idx]:
            result += containers[n]
            m_idx += 1

    print('#{} {}'.format(tc+1, result))