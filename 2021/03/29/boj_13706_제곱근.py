import sys
sys.stdin = open('boj_13706.txt', 'r')

N = int(input())
result = 1
s, e = 2, N - 1
isFinished = False

while not isFinished:
    mid = (s + e) // 2
    mid_sqrt = (mid ** 2)

    if mid_sqrt == N:
        isFinished = True
    elif mid_sqrt < N:
        s = mid + 1
    else:
        e = mid - 1

print(mid)