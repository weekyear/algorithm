def solution(relation):
    from itertools import combinations
    N, M = len(relation[0]), len(relation)
    keys, answer = [], 0
    for r in range(1, N + 1):
        for comb in combinations(range(N), r):
            isFinished = False
            for key in keys:
                len_key = len(key)
                for k in key:
                    if k in comb:
                        len_key -= 1
                    if len_key == 0:
                        isFinished = True
                        break
                if isFinished:
                    break

            if not isFinished:
                same_dict = {}
                for m in range(M):
                    cur_key = ''
                    for c in comb:
                        cur_key += relation[m][c]
                    if not same_dict.get(cur_key, False):
                        same_dict[cur_key] = True
                    else:
                        break
                else:
                    answer += 1
                    keys.append(comb)

    return answer