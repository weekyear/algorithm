import sys
sys.stdin = open('input_13458.txt', 'r')

import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = len(A)
c = 0
for a in A:
    if a - B > 0:
        remain = a - B
        c += math.ceil(remain / C)

result += c
print(result)