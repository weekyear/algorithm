import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def perm(k, dist):
    if k == N:
        global min_dist
        dist += abs(home[0] - cust[idxs[N]][0]) + abs(home[1] - cust[idxs[N]][1])
        if dist < min_dist:
            min_dist = dist
            print(min_dist, idxs)
    else:
        for i in range(1, N + 1):
            if not cust_visited[i]:
                cust_visited[i] = 1
                idxs[k + 1] = i
                new_dist = dist + abs(cust[idxs[k]][0] - cust[i][0]) + abs(cust[idxs[k]][1] - cust[i][1])
                if new_dist < min_dist:
                    perm(k + 1, new_dist)
                cust_visited[i] = 0


for tc in range(T):
    N = int(input())
    pos = list(map(int, input().split()))

    comp = [pos[0], pos[1]]
    home = [pos[2], pos[3]]

    min_dist = 0xffffff

    cust = [comp]
    for p in range(2, N + 2):
        cust.append([pos[2 * p], pos[2 * p + 1]])

    idxs = [0 for _ in range(N + 1)]
    cust_visited = [0 for _ in range(N + 1)]
    cust_visited[0] = 1

    perm(0, 0)
    print('#{} {}'.format(tc + 1, min_dist))