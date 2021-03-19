import sys
sys.stdin = open('input_4796.txt', 'r')

case_num = 0
while True:
    L, P, V = map(int, input().split())

    if L == P == V == 0:
        break

    case_num += 1
    result = V // P * L + min(V % P, L)

    print("Case {}: {}".format(case_num, result))