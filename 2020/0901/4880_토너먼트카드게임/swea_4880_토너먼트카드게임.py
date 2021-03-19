import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def isRightWinner(right, left):
    if right == 1 and left == 3 or right == 2 and left == 1 or right == 3 and left == 2:
        return True
    else:
        return False

def getWinner(_list, start_idx):
    j = len(_list)

    if j > 2:
        k = (j - 1) // 2

        f_group = []
        for i in range(k+1):
            f_group.append(_list[i])
        f_win_info = getWinner(f_group, start_idx)

        s_group = []
        for i in range(k+1, j):
            s_group.append(_list[i])
        s_win_info = getWinner(s_group, start_idx+k+1)

        left = int(f_win_info[0])
        right = int(s_win_info[0])
        if isRightWinner(right, left):
            return s_win_info
        else:
            return f_win_info
    elif j > 1:
        right = int(_list[1])
        left = int(_list[0])

        if isRightWinner(right, left):
            return right, start_idx + 1
        else:
            return left, start_idx
    else:
        return _list[0], start_idx

for tc in range(T):
    N = int(input())
    num_list = input().split()

    result = getWinner(num_list, 0)

    print('#{} {}'.format(tc+1, result[1]+1))

