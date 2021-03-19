import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    E_list = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for e in range(E):
        x, y = map(int, input().split())
        E_list[x][y] = 1

    S, G = map(int, input().split())

    isFind = 0

    visited = []
    stack = []

    stack.append(S)

    while stack:
        node = stack[len(stack)-1]

        if node not in visited:
            visited.append(node)

        for w in range(1, len(E_list[node])):
            if E_list[node][w] == 1 and w not in visited:
                if w == G:
                    isFind = 1
                    break
                node = w
                stack.append(w)
                break
        else:
            node = stack.pop()

        if isFind: break
    print('#{} {}'.format(tc+1, isFind))