import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    l, s_pt = map(int, input().split())
    n_list = list(map(int, input().split()))

    N = len(n_list)
    w_dict = {}

    for n in range(0, N, 2):
        f = n_list[n]
        t = n_list[n + 1]
        w_dict[f] = w_dict.get(f, []) + [t]

    max_num = 0
    Q = []
    Q.append([s_pt, 0])
    visited = [0] * 101
    visited[s_pt] = 1

    result = []
    cur_step = 0

    while Q:
        v_info = Q.pop(0)
        v = v_info[0]

        for w in w_dict.get(v, []):
            if visited[w] == 0:
                if cur_step == v_info[1]:
                    cur_step = v_info[1] + 1
                    result.clear()
                Q.append([w, cur_step])
                result.append(w)
                visited[w] = 1

    r = len(result)
    for i in range(r):
        if result[i] > max_num:
            max_num = result[i]

    print('#{} {}'.format(tc, max_num))