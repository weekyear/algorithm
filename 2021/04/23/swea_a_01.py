import sys
sys.stdin = open('input_1.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(int(input())):
    N = int(input())
    countries = [list(map(int, input().split())) for _ in range(N)]
    soldiers = [list(map(int, input().split())) for _ in range(N)]
    supplies = [list(map(int, input().split())) for _ in range(N)]

    remains = [0 for _ in range(4)]
    result = 0

    for y in range(N):
        for x in range(N):
            remains[countries[y][x]] += 1

    turn = 1
    isFinished = False
    while not isFinished:
        if remains[turn] > 0:
            # 공격
            attackers = {}
            beAttackers = []
            for y in range(N):
                for x in range(N):
                    if countries[y][x] != turn and countries[y][x] != 0:
                        num_soldiers_turn = 0
                        attack_pos = []
                        for d in range(4):
                            n_y, n_x = y + dy[d], x + dx[d]

                            if -1 < n_y < N and -1 < n_x < N and countries[n_y][n_x] == turn:
                                num_soldiers_turn += soldiers[n_y][n_x]
                                attack_pos.append((n_y, n_x))

                        if soldiers[y][x] * 5 < num_soldiers_turn:
                            attack_num = 0
                            for pos in attack_pos:
                                attackers[(pos[0], pos[1])] = attackers.get((pos[0], pos[1]), 0) + 1
                                attack_num += soldiers[pos[0]][pos[1]] // 4

                            beAttackers.append((y, x))
                            soldiers[y][x] = attack_num - soldiers[y][x]

            for a_pos, num in attackers.items():
                soldiers[a_pos[0]][a_pos[1]] -= (soldiers[a_pos[0]][a_pos[1]] // 4) * num

            for beAttack in beAttackers:
                c_y, c_x = beAttack[0], beAttack[1]
                remains[countries[c_y][c_x]] -= 1
                remains[turn] += 1
                countries[c_y][c_x] = turn

            # 지원
            suppliers = []
            for y in range(N):
                for x in range(N):
                    if countries[y][x] == turn:
                        isExistEnemy = False
                        myPos = []
                        for d in range(4):
                            n_y, n_x = y + dy[d], x + dx[d]
                            if -1 < n_y < N and -1 < n_x < N:
                                if countries[n_y][n_x] == turn:
                                    myPos.append((n_y, n_x))
                                elif countries[n_y][n_x] != 0:
                                    isExistEnemy = True
                        if isExistEnemy:
                            for pos in myPos:
                                if soldiers[pos[0]][pos[1]] * 5 < soldiers[y][x]:
                                    suppliers.append([(y, x), (pos[0], pos[1]), soldiers[y][x] // 5])
                        else:
                            for pos in myPos:
                                suppliers.append([(y, x), (pos[0], pos[1]), soldiers[y][x] // 5])

            for supply in suppliers:
                given, taken, num = supply[0], supply[1], supply[2]

                soldiers[given[0]][given[1]] -= num
                soldiers[taken[0]][taken[1]] += num


            # 보충
            for y in range(N):
                for x in range(N):
                    soldiers[y][x] += supplies[y][x]

            remain_num = 0
            for r in range(1, 4):
                if remains[r] != 0:
                    remain_num += 1

            if remain_num == 1:
                break

        # turn 교체
        if turn > 2:
            turn = 1
        else:
            turn += 1
    print('#{} {}'.format(tc + 1, sum(map(sum, soldiers))))