import sys
sys.stdin = open('input_1969.txt', 'r')

N, M = map(int, input().split())

dnas = [input() for _ in range(N)]

info_dna = []

for i in range(M):
    nums_of_dna = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    for j in range(N):
        nums_of_dna[dnas[j][i]] += 1

    max_num = max(nums_of_dna.keys(), key=nums_of_dna.get)
    info_dna.append(max_num)

res_num = 0
result = ''.join(info_dna)
for k in range(N):
    if dnas[k] != result:
        for m in range(M):
            if dnas[k][m] != info_dna[m]:
                res_num += 1

print(result)
print(res_num)