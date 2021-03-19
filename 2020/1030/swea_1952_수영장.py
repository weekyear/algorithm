import sys
sys.stdin = open('input.txt', 'r')

def get_three_cases(idx, elem):
    if idx > 9:
        threeCases.append(list(elem))
        return
    for t in range(idx, 10):
        if threeMonthPrices[t]:
            elem.append(t)
            get_three_cases(t + 3, elem)
            elem.pop()
            if threeMonthPrices[t + 1]:
                elem.append(t+1)
                get_three_cases(t + 4, elem)
                elem.pop()
            if threeMonthPrices[t + 2]:
                elem.append(t+2)
                get_three_cases(t + 5, elem)
                elem.pop()
            break
    else:
        threeCases.append(list(elem))

T = int(input())

for tc in range(T):
    D, M, T, Y = map(int, input().split())
    pool_days = list(map(int, input().split()))

    prices = [0 for _ in range(12)]

    for i in range(12):
        if pool_days[i]:
            if pool_days[i] * D > M:
                prices[i] = M
            else:
                prices[i] = pool_days[i] * D

    threeMonthPrices = [0 for _ in range(12)]
    for i in range(10):
        if prices[i] + prices[i+1] + prices[i+2] > T:
            threeMonthPrices[i] = T

    threeCases = []
    get_three_cases(0, [])

    min_result = 0xffffff
    for case in threeCases:
        result = 0
        visited = [1 if i in case else 0 for i in range(12)]

        result += T * len(case)
        m = 0
        while m < 12:
            if not visited[m]:
                result += prices[m]
                m += 1
            else:
                m += 3

        if result < min_result:
            min_result = result

    if min_result > Y:
        min_result = Y

    print('#{} {}'.format(tc + 1, min_result))

