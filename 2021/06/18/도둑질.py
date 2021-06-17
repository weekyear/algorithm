def solution(money):
    dp1 = [0 for _ in range(len(money))]
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for m in range(2, len(money) - 1):
        dp1[m] = max(dp1[m - 2] + money[m], dp1[m - 1])

    dp2 = [0 for _ in range(len(money))]
    dp2[0] = 0
    dp2[1] = money[1]
    for m in range(2, len(money)):
        dp2[m] = max(dp2[m - 2] + money[m], dp2[m - 1])

    return max(max(dp1), max(dp2))