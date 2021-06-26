def solution(N, roads, K):
    import heapq
    fields = [[0xffffff for _ in range(N + 1)] for _ in range(N + 1)]

    for a, b, w in roads:
        if fields[a][b] > w:
            fields[a][b], fields[b][a] = w, w

    distances = [0xffffff] * (N + 1)
    distances[1] = 0
    Q = [(0, 1)]

    while Q:
        cur_dist, cur_pos = heapq.heappop(Q)

        if distances[cur_pos] < cur_dist:
            continue

        for r in range(1, N + 1):
            new_dist = cur_dist + fields[cur_pos][r]
            if new_dist < distances[r]:
                distances[r] = new_dist
                heapq.heappush(Q, (new_dist, r))

    answer = 0
    for d in distances:
        if d <= K:
            answer += 1

    return answer