import sys
sys.stdin = open('boj_11722.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
cache = [1 for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i):
        if numbers[i] < numbers[j] and cache[j] + 1 > cache[i]:
            cache[i] = cache[j] + 1
    if result < cache[i]:
        result = cache[i]

print(result)