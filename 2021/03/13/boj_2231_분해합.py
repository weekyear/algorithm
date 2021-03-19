import sys
sys.stdin = open('input_2231.txt', 'r')

N = int(input())

result = 0
for num in range(1, N):
    result = num
    temp = num
    while num:
        temp += num % 10
        num //= 10

    if temp == N:
        break

if result < N - 1:
    print(result)
else:
    print(0)