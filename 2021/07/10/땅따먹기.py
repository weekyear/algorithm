def solution(land):
    for l in range(len(land) - 1):
        for i in range(4):
            land[l + 1][i] = max([land[l][j] if j != i else 0 for j in range(4)]) + land[l + 1][i]

    return max(land[len(land) - 1])