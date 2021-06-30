def solution(N):
    answer = 0
    for n in range(1, N // 2 + 1):
        for m in range(n, N // 2 + 2):
            sum_num = sum(range(n, m + 1))
            if sum_num == N:
                answer += 1
            elif sum_num > N:
                break
    return answer + 1