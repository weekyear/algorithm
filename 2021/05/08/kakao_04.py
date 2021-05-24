def solution(n, start, end, roads, traps):
    import sys
    sys.setrecursionlimit(20000)
    answer = []
    reverses = [0 for _ in range(n+1)]
    field = [[0] * (n + 1) for _ in range(n+1)]
    for road in roads:
        field[road[0]][road[1]] = road[2], False
        field[road[1]][road[0]] = road[2], True

    for t in traps:
        reverses[t] = 1

    visited = {}
    visited[(tuple(reverses), start)] = 1

    def dfs(cur_p, cur_r):
        if cur_p == end:
            answer.append(cur_r)

        for w in range(len(field[cur_p])):
            if field[cur_p][w] == 0:
                continue
            val, is_rev = field[cur_p][w]
            is_reverse = False
            if reverses[cur_p] == -1:
                is_reverse = not is_reverse
            if reverses[w] == -1:
                is_reverse = not is_reverse

            if is_reverse == is_rev:
                if reverses[w] != 0:
                    reverses[w] *= -1
                if not visited.get((tuple(reverses), w), False):
                    visited[(tuple(reverses), w)] = 1
                    dfs(w, cur_r + val)
                if reverses[w] != 0:
                    reverses[w] *= -1

    dfs(start, 0)
    return min(answer)

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))