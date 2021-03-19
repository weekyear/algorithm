import sys

sys.stdin = open('boj_12851.txt', 'r')

N, K = map(int, input().split())

Q = [(N, 0)]
visited = {N: [0, 1]}
result = 0
num_m = 0


def insertToQAndCheckCatch(info, num_case):
    global result, Q, num_m, visited
    new_x, time = info
    if not -1 < new_x < 100001:
        return

    if not visited.get(new_x, False):
        # 해당 시간대에 몇 개가 겹치는지 확인하기 위해
        visited[new_x] = [time, num_case]
        Q.append(info)
        if new_x == K:
            result = time
    elif visited[new_x][0] == time:
        visited[new_x][1] += num_case


while Q:
    cur_x, time = Q.pop(0)

    if result and result <= time:
        break

    for a in [-1, 1, cur_x]:
        insertToQAndCheckCatch((cur_x + a, time + 1), visited.get(cur_x)[1])

print(result)
print(visited[K][1])
