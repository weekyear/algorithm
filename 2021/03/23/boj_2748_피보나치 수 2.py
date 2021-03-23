import sys
sys.stdin = open('boj_2748.txt', 'r')

N = int(input())
# N = 10
cache = [0 for _ in range(N + 1)]
cache[1] = 1

def fibonachi(n):
    if n < 2:
        return cache[n]

    if cache[n]:
        return cache[n]

    cache[n] = fibonachi(n - 1) + fibonachi(n - 2)
    return cache[n]

print(fibonachi(N))