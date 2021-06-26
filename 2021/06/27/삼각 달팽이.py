def solution(n):
    answer = []
    fields = [[0 for _ in range(n)] for _ in range(n)]
    ver, num = 0, 1
    y, x, M = -1, 0, n
    while n > 0:
        for i in range(n):
            if ver == 0:
                y += 1
            elif ver == 1:
                x += 1
            else:
                y -= 1
                x -= 1
            fields[y][x] = num
            num += 1

        ver = (ver + 1) % 3
        n -= 1

    for m in range(M):
        for l in range(m + 1):
            answer.append(fields[m][l])
    return answer