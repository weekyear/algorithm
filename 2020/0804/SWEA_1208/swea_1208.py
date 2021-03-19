import sys
sys.stdin = open("input.txt", "r")

def find_min_max(_list):
    max_idx = 0
    min_idx = 0

    for i in range(len(blocks)):
        if blocks[i] > blocks[max_idx]:
            max_idx = i

        if blocks[i] < blocks[min_idx]:
            min_idx = i
    return max_idx, min_idx

for test_case in range(1, 11):
    d = int(input())
    blocks = list(map(int, input().split()))

    while d > 0:
        max_idx, min_idx = find_min_max(blocks)

        blocks[max_idx] -= 1
        blocks[min_idx] += 1
        d -= 1
    
    max_idx, min_idx = find_min_max(blocks)

    print('#{} {}'.format(test_case, blocks[max_idx]-blocks[min_idx]))