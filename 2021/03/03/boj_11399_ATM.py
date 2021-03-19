import sys
sys.stdin = open('input_11399.txt', 'r')

N = int(input())
P = list(map(int, input().split()))

P.sort()

result = 0
cur_sum = 0

for p in P:
    result += cur_sum + p
    cur_sum += p

print(result)