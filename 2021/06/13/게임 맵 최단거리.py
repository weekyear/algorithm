def solution(maps):
    from collections import deque
    dy_x = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    m = len(maps[0]) - 1
    n = len(maps) - 1
    Q = deque([(0, 0, 1)])
    visited.add((0, 0))

    while Q:
        cy, cx, step = Q.popleft()

        for dy, dx in dy_x:
            ny, nx = cy + dy, cx + dx
            # BFS의 경우 visited를 2차원으로 체크하고 넘겨주기가 힘들다
            # 따라서 set에다가 지나온 좌표를 채워넣은 다음 새로운 좌표를 검색할 때 set를 활용하는 것이 빠르다.
            # BFS는 해당 좌표에 도착했을 때 해당 방법이 가장 빠르게 도착하는 것을 보장하기 때문에
            # set에 이미 들어가 있는 좌표를 가면 해당 좌표를 가는 가장 빠른 방법이 아니기 때문에 갈 필요가 없다.
            if -1 < ny <= n and -1 < nx <= m and (ny, nx) not in visited and maps[ny][nx] == 1:
                visited.add((ny, nx))
                if ny == n and nx == m:
                    return step + 1
                Q.append((ny, nx, step + 1))

    return -1