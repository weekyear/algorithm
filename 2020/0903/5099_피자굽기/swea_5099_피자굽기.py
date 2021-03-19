import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    lenQ, num_P = map(int, input().split())
    pizzas = list(map(int, input().split()))
    Q = []
    for i in range(lenQ):
        p_num = i + 1
        Q.append([pizzas.pop(0), p_num])

    n = 0
    remain_num = lenQ
    prev_num = 0

    while remain_num > 1:
        cur_pizza = Q[n]
        if Q[n]:
            if cur_pizza[0] > 1:
                cur_pizza[0] //= 2
                prev_num = n
            else:
                Q.pop(n)
                if len(pizzas) != 0:
                    p_num += 1
                    Q.insert(n, [pizzas.pop(0), p_num])
                else:
                    Q.insert(n, [])
                    remain_num -= 1

        n = (n+1)%lenQ


    print('#{} {}'.format(tc+1, Q[prev_num][1]))