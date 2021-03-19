import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


for tc in range(T):
    N = int(input())
    inputs = list(map(int, input().split()))
    bst = [0]

    for n in range(N):
        c = inputs[n]
        bst.append(c)
        cur_node = (n+1)
        p_node = cur_node // 2
        while p_node > 0 and bst[p_node] > c:
            bst[p_node], bst[cur_node] = bst[cur_node], bst[p_node]
            cur_node = p_node
            p_node //= 2

    final_node = N
    p_sum = 0
    while final_node > 0:
        final_node //= 2
        p_sum += bst[final_node]

    print('#{} {}'.format(tc+1, p_sum))