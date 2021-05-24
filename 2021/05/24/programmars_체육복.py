def solution(n, costs):
    def check_connection(start, end):
        visited = [0 for _ in range(n)]

        visited[start] = 1
        Q = [start]
        while Q:
            cur = Q.pop(0)
            for w in check[cur]:
                if w == end:
                    return True
                if not visited[w]:
                    visited[w] = 1
                    Q.append(w)
        return False

    check = [[] for _ in range(n)]
    costs.sort(key=lambda c: c[2])
    answer = 0
    for cost in costs:
        if not check_connection(cost[0], cost[1]):
            check[cost[0]].append(cost[1])
            check[cost[1]].append(cost[0])
            answer += cost[2]

    return answer


print(solution(5, [[0,1,1],[0,3,2],[1,2,5],[2,3,1],[1,3,8],[1, 4, 9]]))