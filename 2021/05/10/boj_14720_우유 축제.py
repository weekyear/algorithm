import sys
sys.stdin = open('boj_14720.txt')

N = int(input())
stores = list(map(int, input().split()))

cur_milk = 0
result = 0
for n in range(N):
    if stores[n] == cur_milk:
        result += 1
        cur_milk = (cur_milk + 1) % 3

print(result)