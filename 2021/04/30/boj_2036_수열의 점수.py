import sys
sys.stdin = open('boj_2036.txt', 'r')

N = int(input())
plus_lst = []
minus_lst = []
for n in range(N):
    num = int(input())
    if num > 0:
        plus_lst.append(num)
    else:
        minus_lst.append(num)

plus_lst.sort(reverse=True)
minus_lst.sort()

result = 0
for p in range(0, len(plus_lst), 2):
    if p != len(plus_lst) - 1:
        if plus_lst[p] == 1 or plus_lst[p + 1] == 1:
            result += plus_lst[p] + plus_lst[p + 1]
        else:
            result += plus_lst[p] * plus_lst[p + 1]
    else:
        result += plus_lst[p]

for m in range(0, len(minus_lst), 2):
    if m != len(minus_lst) - 1:
        result += minus_lst[m] * minus_lst[m + 1]
    else:
        result += minus_lst[m]

print(result)