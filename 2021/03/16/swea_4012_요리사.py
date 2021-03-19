import sys
sys.stdin = open('input_4012.txt', 'r')

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for added in combination(array[i + 1:], r - 1):
                yield [array[i]] + added


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


for tc in range(int(input())):
    N = int(input())

    food_synergy = [list(map(int, input().split())) for _ in range(N)]

    foods = [i for i in range(N)]

    a_b_foods = [0 for _ in range(N)]

    half_N = N // 2

    cases = []
    num_case = 0
    num_half_case = factorial(N) // (factorial(N - half_N) * half_N * 2)
    for i in combination(foods, half_N):
        num_case += 1
        cases.append(i)
        if num_case == num_half_case:
            break

    min_result = 0xffffff
    for case in cases:
        a_case = case
        b_case = [i for i in range(N)]

        for c in case:
            b_case.remove(c)

        sum_a = 0
        for a in combination(a_case, 2):
            sum_a += food_synergy[a[0]][a[1]] + food_synergy[a[1]][a[0]]

        sum_b = 0
        for b in combination(b_case, 2):
            sum_b += food_synergy[b[0]][b[1]] + food_synergy[b[1]][b[0]]

        if min_result > abs(sum_a - sum_b):
            min_result = abs(sum_a - sum_b)

    print('#{} {}'.format(tc + 1, min_result))