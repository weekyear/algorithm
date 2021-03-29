import sys
sys.stdin = open('boj_16922.txt', 'r')

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
            continue

        for next in combinations(array, r - 1):
            yield [array[i]] + next

from itertools import combinations_with_replacement

romas = [1, 5, 10, 50]
N = int(input())
result = 0
visited = [0] * 50 * (N + 1)

for i in combinations_with_replacement(romas, N):
    sum_comb = sum(i)
    if not visited[sum_comb]:
        visited[sum_comb] = 1
        result += 1

print(result)