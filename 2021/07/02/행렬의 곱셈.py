def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for a in range(len(arr1)):
        for d in range(len(arr2[0])):
            cur_ans = 0
            for b in range(len(arr1[0])):
                cur_ans += arr1[a][b] * arr2[b][d]
            answer[a].append(cur_ans)
    return answer