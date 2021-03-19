import sys

sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    V, E = map(int, input().split())

    w_list = [[] for _ in range(V + 1)]

    for e in range(E):
        a, b = map(int, input().split())
        w_list[a].append(b)

    S, G = map(int, input().split())

    stack = [S]
    visited = [0 for _ in range(V + 1)]
    visited[S] = 1
    isFinish = 0

    while stack:
        cur = stack[len(stack) - 1]

        for w in w_list[cur]:
            if w == G:
                isFinish = 1
                break;
            if not visited[w]:
                stack.append(w)
                visited[w] = 1
                break
        else:
            stack.pop()

        if isFinish:
            break

    print('#{} {}'.format(tc + 1, isFinish))