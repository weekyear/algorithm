import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())

#     num_data = list(map(int, input().split()))

#     _min = 9999999999
#     _max = -9999999999
#     for i in range(N+1-M):
#         _sum = 0
#         for k in range(i, i+M):
#             _sum += num_data[k]

#         if _min > _sum:
#             _min = _sum
#         if _max < _sum:
#             _max = _sum

#     print('#{} {}'.format(test_case, _max-_min))

for t in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    cur = 0
    for i in range(M):
        cur += num[i]

    max_val = cur
    min_val = cur
    for i in range(M, N):
        cur += num[i] - num[i-M]
        if max_val < cur:
            max_val = cur
        elif min_val > cur:
            min_val = cur
    
    print('#{} {}'.format(t, max_val-min_val))