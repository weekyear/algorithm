import sys
sys.stdin = open('input_16953.txt', 'r')

A, B = map(int, input().split())

# 162 => 2
cur_val = B
result = 1
while cur_val != A:
    if cur_val % 10 == 1:
        cur_val //= 10
        result += 1
    elif not cur_val % 2:
        cur_val //= 2
        result += 1
    else:
        print(-1)
        break

    if cur_val < A:
        print(-1)
        break
else:
    print(result)

# 2 => 162 : 시간 초과가 뜨는데??...
# Q = [(A, 0)]
# k = 0
#
# cur_min = A
# while Q:
#     cur_val, k = Q.pop(0)
#
#     n_val_1 = cur_val * 2
#     n_val_2 = cur_val * 10 + 1
#     if n_val_1 == B or n_val_2 == B:
#         print(k + 2)
#         break
#     else:
#         Q.append((n_val_1, k + 1))
#         Q.append((n_val_2, k + 1))
#
#         if cur_min == cur_val:
#             cur_min = min(Q, key=lambda x: x[0])[0]
#             if cur_min > B:
#                 print(-1)
#                 break