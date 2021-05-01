import sys
sys.stdin = open('boj_2012.txt', 'r')

N = int(input())
expects = [int(input()) for _ in range(N)]
expects.sort()

result = 0
for n in range(1, N + 1):
    result += abs(expects[n - 1] - n)

print(result)
