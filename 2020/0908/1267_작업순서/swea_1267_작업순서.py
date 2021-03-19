import sys

sys.stdin = open('input.txt', 'r')

def dfs(s):
    if visited[s] == 0:
        print('{}'.format(s), end=' ')
        visited[s] = 1
        for w in graph.get(s, []):
            if visited[w] == 0 and input_check[w] == 1:
                dfs(w)
            if input_check[w] > 0:
                input_check[w] -= 1

for tc in range(10):
    V, E = map(int, input().split())
    graph = {}
    data = list(map(int, input().split()))
    visited = [0 for _ in range(V+1)]

    input_check = [0 for _ in range(V+1)]
    for i in range(E):
        _in, _out = data[2 * i], data[2 * i + 1]
        graph[_in] = graph.get(_in, []) + [_out]
        input_check[_out] += 1

    inputs = []
    for c in range(1, V+1):
        if input_check[c] == 0:
            inputs.append(c)

    print('#{}'.format(tc+1), end=' ')
    for inp in inputs:
        dfs(inp)

    print()

    # print('#{} {} {}'.format(tc + 1, s_num, max_k))
