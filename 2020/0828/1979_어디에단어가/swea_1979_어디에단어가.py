import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())

    word_area = [[w for w in list(map(int, input().split()))] for _ in range(N)]

    result = 0
    # 가로 탐색
    char_count = 0
    for y in range(N):
        for x in range(N):
            # 0이 아니면 문자수 카운트 시작
            if word_area[y][x] != 0:
                char_count += 1
            # 탐색 중에 0만나면 문자수 카운트랑 지정된 문자수랑 같은지 비교하고 같으면 result에 추가
            else:
                if char_count == K:
                    result += 1
                # 문자수 카운트 초기화
                char_count = 0
        # 문자수 카운트 중에 가로 탐색이 끝나면 지정된 문자수 카운트랑 지정된 문자수랑 같은지 비교하고 같으면 result에 추가
        if char_count == K:
            result += 1
        char_count = 0

    # 세로 탐색 : 기본적으로 같음
    char_count = 0
    for x in range(N):
        for y in range(N):
            if word_area[y][x] != 0:
                char_count += 1
            else:
                if char_count == K:
                    result += 1
                char_count = 0

        if char_count == K:
            result += 1
        char_count = 0

    print('#{} {}'.format(test_case + 1, result))