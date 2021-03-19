import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    w_list = [[] for _ in range(V+1)]

    for i in range(E):
        v1, v2 = map(int, input().split())
        w_list[v1].append(v2)
        w_list[v2].append(v1)

    S, G = map(int, input().split())

    Q = [[S, 0]]
    visited = [0 for _ in range(V+1)]
    result = 0

    while Q:
        v_info = Q.pop(0)
        v = v_info[0]
        step = v_info[1]

        for w in w_list[v]:
            if w == G:
                result = step + 1
                break
            if visited[w] == 0:
                Q.append([w, step+1])
                visited[w] = 1

        if result:
            break

    print('#{} {}'.format(tc+1, result))