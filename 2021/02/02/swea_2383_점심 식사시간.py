import sys
sys.stdin = open('input_2383.txt', 'r')

for tc in range(int(input())):
    # 데이터 받아오는 곳
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]
    peoples = []
    stairs = []
    p_num = 0


    for y in range(N):
        for x in range(N):
            if rooms[y][x] == 1:
                # 사람들 위치 정보 받아오고
                peoples.append([y, x])
            elif rooms[y][x] != 0:
                # 계단에다가는 위치랑, 내려가는 데 걸리는 시간
                stairs.append([y, x, rooms[y][x]])

    # 최종 답
    result = 0xffffff

    # 부분집합
    # 2가지 출구로 가는 경우의 수를 가정
    for i in range(2 << len(peoples)):
        # 계단 대기열
        stair1 = []
        stair2 = []
        for j in range(len(peoples)):
            # 사람들이 현재 경우의 수에서 어떤 출구를 선택하는지 확인
            # True인 경우에는 1번 출구로 가는데
            if i & (1 << j):
                # s1 : 현재 사람위치에서 출구까지 도착하는 데 걸리는 거리
                s1 = abs(peoples[j][0] - stairs[0][0]) + abs(peoples[j][1] - stairs[0][1])
                # s2 : 현재 사람 출발위치에서 출구를 나가는데 까지 걸리는 거리
                s2 = s1 + stairs[0][2]
                stair1.append([s1, s2])
            else:
                s1 = abs(peoples[j][0] - stairs[1][0]) + abs(peoples[j][1] - stairs[1][1])
                s2 = s1 + stairs[1][2]
                stair2.append([s1, s2])

        # 온 순서대로 정렬
        stair1.sort(key=lambda s: s[0])
        stair2.sort(key=lambda s: s[0])

        # 3명이 초과하는 경우에는 대기해야 함
        if len(stair1) > 3:
            # 4번째부터는 출발 위치에서 나가는데 까지 걸리는 시간에서 대기 시간을 추가해야 함.
            for k in range(len(stair1) - 3):
                # 실제 대기할 수도 있는데
                # 3명이 다 내려가고 나서야 도착할 수 있잖아
                stair1[k+3][1] = max(stair1[k][1] + stairs[0][2], stair1[k+3][1])

        if len(stair2) > 3:
            for k in range(len(stair2) - 3):
                stair2[k+3][1] = max(stair2[k][1] + stairs[1][2], stair2[k+3][1])

        max_result = 0
        if stair1 and stair2:
            max_result = max(stair1[len(stair1) - 1][1], stair2[len(stair2) - 1][1])
        elif stair1:
            max_result = stair1[len(stair1) - 1][1]
        else:
            max_result = stair2[len(stair2) - 1][1]

        if result > max_result:
            result = max_result

    print('#{} {}'.format(tc + 1, result + 1))