import sys
sys.stdin = open('input_2382.txt', 'r')

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

for tc in range(int(input())):
    N, M, K = map(int, input().split())

    bacterias = []

    field = [[[] for _ in range(N)] for _ in range(N)]

    for k in range(K):
        bacteria = list(map(int, input().split()))
        bacterias.append(bacteria)
        field[bacteria[0]][bacteria[1]].append([bacteria[2], bacteria[3]])

    for m in range(M):
        for bacteria in bacterias:
            bacteria[0] += dy[bacteria[3]]
            bacteria[1] += dx[bacteria[3]]

            if not bacteria[0] or not bacteria[1] or bacteria[0] == N - 1 or bacteria[1] == N - 1:
                bacteria[2] //= 2
                if bacteria[3] % 2:
                    bacteria[3] += 1
                else:
                    bacteria[3] -= 1

        bacterias.sort(key=lambda bac: (bac[0], bac[1]))

        combines = [bacterias.pop(0)]
        new_bacterias = []
        while bacterias:
            cur_bacteria = bacterias.pop(0)
            if combines[0][0] == cur_bacteria[0] and combines[0][1] == cur_bacteria[1]:
                combines.append(cur_bacteria)
            else:
                if len(combines) > 1:
                    combines.sort(key=lambda c: -c[2])

                    for e in range(1, len(combines)):
                        combines[0][2] += combines[e][2]

                new_bacterias.append(combines[0])
                combines.clear()

        bacterias = new_bacterias

    result = 0
    for bac in bacterias:
        result += bac[2]

    print('#{} {}'.format(tc + 1, result))

