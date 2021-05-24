import sys
sys.stdin = open('boj_5585.txt', 'r')

N = int(input())

coins = [500, 100, 50, 10, 5, 1]
result = 0
remains = 1000 - N
for coin in coins:
    result += remains // coin
    remains %= coin

print(result)