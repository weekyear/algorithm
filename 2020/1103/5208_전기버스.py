import sys
sys.stdin = open('input.txt', 'r')

def dfs(cur_b, cur_p, cnt):
    global min_cnt
    if cur_b == 0 or cnt >= min_cnt: return
    if cur_p + cur_b >= N or cur_p == N:
        if min_cnt > cnt:
            min_cnt = cnt
    else:
        cur_b -= 1
        new_b = bus_stop[cur_p]

        dfs(new_b, cur_p + 1, cnt + 1)
        dfs(cur_b, cur_p + 1, cnt)

for tc in range(int(input())):
    bus_infos = list(map(int, input().split()))
    N, bus_stop = bus_infos[0], bus_infos[1:]

    min_cnt = 0xffffff

    dfs(bus_stop[0], 1, 0)

    print('#{} {}'.format(tc + 1, min_cnt))