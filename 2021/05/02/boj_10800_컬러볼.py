import sys
sys.stdin = open('boj_10800.txt')

readlines = sys.stdin.readline
N = int(input())
result = [0] * N

inputs = []
accumulates = {}
for n in range(N):
    C, S = map(int, readlines().split())
    inputs.append([n, C, S])

    if not accumulates.get(C, False):
        accumulates[C] = 0

inputs.sort(key=lambda x: x[2])

cur_val = 0
total_sum = 0
saved = []
for i in range(N):
    cur_n, cur_c, cur_s = inputs[i]

    saved.append((cur_n, cur_c, cur_s))
    result[cur_n] = total_sum - accumulates[cur_c]
    if (i < N - 1 and cur_s < inputs[i + 1][2]) or i == N - 1:
        for save in saved:
            total_sum += save[2]
            accumulates[save[1]] += save[2]
        saved.clear()

for r in result:
    print(r)