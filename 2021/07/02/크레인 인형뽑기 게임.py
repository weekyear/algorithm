def solution(board, moves):
    answer = 0
    N, M = len(board), len(board[0])
    basket = []
    Q = [[] for _ in range(M)]
    for n in range(N - 1, -1, -1):
        for m in range(M):
            if board[n][m]:
                Q[m].append(board[n][m])

    for move in moves:
        if len(Q[move - 1]):
            doll = Q[move - 1].pop()
            len_b = len(basket)
            if len_b and basket[len_b - 1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)

    return answer