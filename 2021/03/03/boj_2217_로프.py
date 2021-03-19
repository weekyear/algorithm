import sys
sys.stdin = open('input_2217.txt', 'r')

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)

result = 0

for r in range(N):
    cur_w = ropes[r] * (r + 1)
    if result < cur_w:
        result = cur_w

print(result)