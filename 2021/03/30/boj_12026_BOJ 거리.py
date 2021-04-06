import sys
sys.stdin = open('boj_12026.txt', 'r')

N = int(input())
street = input()

boj_idxs = {'B': 0, 'O': 1, 'J': 2}
expenses = [[(0, 0)], [], []]
result = [0xfffffffff] * N

def calculate(lst_a, lst_b):
    added = (n, -1)
    for a in lst_a:
        cur_val = a[1] + (n - a[0]) ** 2
        if result[n] > cur_val:
            result[n] = cur_val
            added = (n, cur_val)

    if added[1] != -1:
        lst_b.append(added)
    else:
        result[n] = -1

for n in range(1, N):
    calculate(expenses[boj_idxs[street[n]] - 1], expenses[boj_idxs[street[n]]])

print(result[N - 1])