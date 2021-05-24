def solution(routes):
    routes.sort(key=lambda x: x[1])
    leng = len(routes)
    for r in range(leng):
        routes[r] = (routes[r][0] + 30000, routes[r][1] + 30000)

    answer = 0
    camera = -1

    for i in range(leng):
        if camera < routes[i][0]:
            camera = routes[i][1]
            answer += 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.1MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (0.98ms, 10.4MB)
# 테스트 2 〉	통과 (0.41ms, 10.3MB)
# 테스트 3 〉	통과 (1.54ms, 10.7MB)
# 테스트 4 〉	통과 (0.11ms, 10.2MB)
# 테스트 5 〉	통과 (1.96ms, 10.8MB)