import sys
sys.stdin = open('boj_9019.txt', 'r')

from collections import deque

def get_D(number):
    return number * 2 % 10000

def get_S(number):
    return number - 1 if number != 0 else 9999

def get_L(number):
    if number > 999:
        return (number % 1000) * 10 + number // 1000
    else:
        return number * 10

def get_R(number):
    return (number % 10) * 1000 + number // 10

N = int(input())

for n in range(N):
    A, B = map(int, input().split())

    Q = deque([(A, "")])
    visited = [0] * 10000

    result = ''

    while Q:
        cur_str, cmds = Q.popleft()
        # cmds = visited[cur_str]
        if cur_str == B:
            print(cmds)
            break

        if visited[cur_str] != 0: continue
        visited[cur_str] = 1

        for fun, cmd in [(get_D, 'D'), (get_S, 'S'), (get_L, 'L'), (get_R, 'R')]:
            Q.append((fun(cur_str), cmds + cmd))
