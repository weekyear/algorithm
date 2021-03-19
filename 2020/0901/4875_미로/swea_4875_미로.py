import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def indexOfStartPoint(_str):
    str_length = len(_str)
    for idx in range(str_length):
        if _str[idx] == '2':
            return idx
    return -1

for tc in range(T):
    N = int(input())
    maze = []
    curPt = []
    saveStack = []
    isFinished = False
    visited = [[0 for _ in range(N)] for _ in range(N)]

    result = 0

    for n in range(N):
        maze.append(input())
        s_x = indexOfStartPoint(maze[n])
        if not curPt and s_x != -1:
            curPt.append(s_x)
            curPt.append(n)

    while not isFinished:
        if visited[curPt[1]][curPt[0]] == 0:
            visited[curPt[1]][curPt[0]] = 1

        num_route = 0
        for d in range(4):
            new_x = curPt[0] + dx[d]
            new_y = curPt[1] + dy[d]
            if -1 < new_x < N and -1 < new_y < N and not visited[new_y][new_x]:
                if maze[new_y][new_x] == '0':
                    num_route += 1
                    newPt = [new_x, new_y]
                elif maze[new_y][new_x] == '3':
                    isFinished = True
                    result = 1
                    break
        else:
            if num_route > 1:
                saveStack.append(curPt)

            if num_route > 0:
                curPt = [newPt[0], newPt[1]]
            else:
                if saveStack:
                    curPt = saveStack.pop()
                else:
                    isFinished = True


    print('#{} {}'.format(tc+1, result))

