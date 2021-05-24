import sys
sys.stdin = open('boj_1459.txt', 'r')

X, Y, W, S = map(int, input().split())

result = 0

if S < W:
    if X % 2 != Y % 2:
        result = S * (max(X, Y) - 1) + W
    else:
        result = S * max(X, Y)
elif S < W * 2:
    result = S * min(X, Y)
    result += W * abs(X - Y)
else:
    result = W * (X + Y)

print(result)