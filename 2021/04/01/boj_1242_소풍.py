import sys
sys.stdin = open('boj_1242.txt', 'r')

N, K, M = map(int, input().split())
origin_N = N

while True:
    kN = K % N
    mN = M % N
    if kN == mN:
        break

    M -= kN

    if M < 0:
        M += N

    N -= 1

print(origin_N - N + 1)