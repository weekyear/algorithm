import sys

sys.stdin = open('boj_12886.txt', 'r')

import sys
from collections import deque

readline = sys.stdin.readline

stones = list(map(int, readline().split()))

all_sum = sum(stones)
visited = {(stones[0], stones[1], stones[2]): 1}


def exchange(stone1, stone2):
    if stone1 < stone2:
        return stone1 + stone1, stone2 - stone1
    else:
        return stone1 - stone2, stone2 + stone2


Q = deque([(stones[0], stones[1], stones[2])])
isFinished = 0

if stones[0] == stones[1] == stones[2]:
    isFinished = 1

while Q and not isFinished:
    A, B, C = Q.popleft()
    lst = [(A, B), (B, C), (C, A)]

    for l in range(3):
        s1, s2 = lst[l]
        if s1 != s2:
            res1, res2 = exchange(s1, s2)

            newList = []

            if l == 0:
                newList = [res1, res2, C]
            elif l == 1:
                newList = [A, res1, res2]
            else:
                newList = [res2, B, res1]

            if not visited.get((newList[0], newList[1], newList[2]), False):
                visited[(newList[0], newList[1], newList[2])] = 1
                if newList[0] == newList[1] == newList[2]:
                    isFinished = 1
                    break
                else:
                    Q.append((newList[0], newList[1], newList[2]))

print(isFinished)
