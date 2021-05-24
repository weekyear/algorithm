import sys
sys.stdin = open('boj_2141.txt', 'r')

N = int(input())
villeges = []

all_sum = 0
for _ in range(N):
    a, x = map(int, input().split())
    all_sum += x
    villeges.append((a, x))

villeges.sort(key=lambda x: x[0])

if all_sum % 2:
    half_people = all_sum // 2 + 1
else:
    half_people = all_sum // 2

cnt = 0
result = 0
for v in villeges:
    cnt += v[1]
    if cnt >= half_people:
        result = v[0]
        break

print(result)