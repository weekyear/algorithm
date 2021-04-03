import sys
sys.stdin = open('boj_10422.txt', 'r')

from itertools import combinations

for _ in range(int(input())):
    N = int(input())

    if N == 1:
        print(0)
        continue

    if not N % 2:
        result = 0
        for j in combinations([i for i in range(N - 2)], (N - 2) // 2):
            result += 1
        print(result)
    else:
        print(0)