import sys
sys.stdin = open('input_4880.txt', 'r')

def GawiBawiBo(a, b):
    winner = []
    if a[1] == b[1]:
        winner = min([a, b], key=lambda x: x[0])
    elif a[1] == 1 and b[1] == 3 or a[1] == 3 and b[1] == 1:
        winner = min([a, b], key=lambda x: x[1])
    else:
        winner = max([a, b], key=lambda x: x[1])
    return winner

def dfs(start, end):
    if (end - start) == 1:
        return GawiBawiBo([start, people[start]], [end, people[end]])
    elif start == end:
        return [start, people[start]]

    return GawiBawiBo(dfs(start, int((start + end)/2)), dfs(int((start + end)/2) + 1, end))

for tc in range(int(input())):
    N = int(input())

    people = list(map(int, input().split()))

    winner = dfs(0, len(people) - 1)

    print('#{} {}'.format(tc + 1, winner[0] + 1))