from itertools import combinations
from collections import defaultdict
import bisect


def solution(info, query):
    answer = []

    dict = defaultdict(list)

    for i in info:
        key = i.split()
        score = int(key.pop())
        dict[''.join(key)].append(score)

        for j in range(4):
            candi = list(combinations(key, j))
            for c in candi:
                dict[''.join(c)].append(score)

    for i in dict:
        dict[i].sort()

    for q in query:
        q = q.replace('and', '').replace('-', '')
        key = q.split()
        score = int(key.pop())
        key = ''.join(key)

        answer.append(len(dict[key])-bisect.bisect_left(dict[key], score))

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))