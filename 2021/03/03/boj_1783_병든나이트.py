import sys
sys.stdin = open('input_1783.txt', 'r')

import math

N, M = map(int, input().split())

# 높이가 3 이상
if N > 2:
    if M > 5:
        print(M - 2)
    elif M == 5:
        print(4)
    else:
        print(M)
# 높이가 3 미만
elif N > 1:
    if M >= 7:
        print(4)
    else:
        print(math.ceil(M / 2))
else:
    print(1)