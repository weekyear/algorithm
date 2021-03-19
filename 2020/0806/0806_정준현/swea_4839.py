import sys


sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def get_count_binary(right, P):
    count = 0
    left = 1
    while left <= right:
        center = (left+right) // 2
        count += 1
        if P == center:
            break
        elif P < center:
            right = center
        else:
            left = center
    return count

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    count_a = get_count_binary(P, Pa)
    count_b = get_count_binary(P, Pb)

    winner = 0
    if count_b < count_a:
        winner = 'B'
    elif count_b > count_a:
        winner = 'A'

    print('#{} {}'.format(test_case, winner))