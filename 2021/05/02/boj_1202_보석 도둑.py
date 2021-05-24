import sys
sys.stdin = open('boj_1202.txt', 'r')
import sys, heapq
readlines = sys.stdin.readline

N, K = map(int, input().split())

jewelrys = []
bags = []

for n in range(N):
    heapq.heappush(jewelrys, list(map(int, readlines().split())))

for k in range(K):
    heapq.heappush(bags, int(readlines()))

result = 0
temp = []
while bags:
    cur_bag = heapq.heappop(bags)

    while jewelrys and cur_bag >= jewelrys[0][0]:
        cur_jewelry = heapq.heappop(jewelrys)
        heapq.heappush(temp, -cur_jewelry[1])

    if temp:
        result += -heapq.heappop(temp)

print(result)