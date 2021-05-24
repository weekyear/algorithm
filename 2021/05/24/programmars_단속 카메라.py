def solution(routes):
    routes.sort(key=lambda x: x[1])
    leng = len(routes)
    checked = [0] * leng
    answer = 0

    for i in range(leng):
        if not checked[i]:
            camera = routes[i][1]
            answer += 1
        else:
            continue

        for j in range(i + 1, leng):
            if routes[j][0] <= camera <= routes[j][1]:
                checked[j] = 1

    return answer


# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.2MB)
# 테스트 3 〉	통과 (0.11ms, 10.2MB)
# 테스트 4 〉	통과 (0.11ms, 10.1MB)
# 테스트 5 〉	통과 (0.09ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (6.86ms, 10.5MB)
# 테스트 2 〉	통과 (3.41ms, 10.3MB)
# 테스트 3 〉	통과 (17.24ms, 10.4MB)
# 테스트 4 〉	통과 (0.35ms, 10.1MB)
# 테스트 5 〉	통과 (21.68ms, 10.6MB)