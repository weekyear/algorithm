def solution(infos, queries):
    def binary_search(lst, find):
        if not lst:
            return 0
        start, end = 0, len(lst) - 1
        prev = -1
        while True:
            mid = (start + end) // 2
            if lst[mid] == find:
                while mid > -1 and lst[mid] == find:
                    mid -= 1
                return len(lst) - mid - 1
            if mid == prev:
                return len(lst) - mid - 1
            prev = mid
            if lst[mid] < find:
                start = mid + 1
            else:
                end = mid - 1

    idxs = {
        'cpp': 0,
        'java': 1,
        'python': 2,
        'backend': 0,
        'frontend': 1,
        'junior': 0,
        'senior': 1,
        'chicken': 0,
        'pizza': 1
    }
    data = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    for info in infos:
        lang, job, career, food, score = info.split()
        data[idxs[lang]][idxs[job]][idxs[career]][idxs[food]].append(int(score))

    for l in range(3):
        for j in range(2):
            for c in range(2):
                for f in range(2):
                    data[l][j][c][f].sort()

    answer = []
    for query in queries:
        c_ans = 0
        lang, job, career, food_and_score = query.split(' and ')
        food, score = food_and_score.split()
        for l in range(3):
            if lang == '-' or idxs.get(lang, -1) == l:
                for j in range(2):
                    if job == '-' or idxs.get(job, -1) == j:
                        for c in range(2):
                            if career == '-' or idxs.get(career, -1) == c:
                                for f in range(2):
                                    if food == '-' or idxs.get(food, -1) == f:
                                        c_ans += binary_search(data[l][j][c][f], int(score))
        answer.append(c_ans)

    return answer