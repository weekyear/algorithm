import sys

sys.stdin = open('input_2875.txt', 'r')

N, M, K = map(int, input().split())

canMakeTeam = True
result = 0

while canMakeTeam:
    if N > 1 and M > 0 and N + M - 3 >= K:
        N -= 2
        M -= 1
        result += 1
    else:
        canMakeTeam = False

print(result)