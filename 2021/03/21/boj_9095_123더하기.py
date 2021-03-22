import sys
sys.stdin = open('input_9095.txt', 'r')

def dfs(cur_value):
    global result
    for add in range(1, 4):
        if cur_value + add == n:
            result += 1
        elif cur_value + add < n:
            dfs(cur_value + add)

for tc in range(int(input())):
    result = 0
    n = int(input())

    dfs(0)

    print(result)