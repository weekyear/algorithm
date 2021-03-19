import sys

sys.stdin = open("input.txt", "r")

for test_case in range(10):
    length = 100
    T = int(input())
    str_list = [input() for _ in range(length)]

    # 끝났는지 체크~
    isFinished = False

    max_lenPattern = 0

    # 글자수 100개 부터 패턴 검색
    for lenPattern in range(length, 0, -1):

        # 가로 검색
        for i in range(length):
            for j in range(length+1-lenPattern):
                for k in range(lenPattern // 2):
                    if str_list[i][j+k] != str_list[i][j+lenPattern-k-1]:
                        break
                else:
                    isFinished = True
                    max_lenPattern = lenPattern
                    break

        # 세로 검색
        # 검색하는 부분에 공통된 반복문이 있어서 아래 이중반복문 아래의 코드를 위에 넣어도 무방하나
        # 한 번에 가로 세로를 다 검증하다보니 50ms 정도 계산 속도가 느려져서 세로 검색을 따로 뽑아냄
        for i in range(length):
            for j in range(length + 1 - lenPattern):
                for k in range(lenPattern // 2):
                    if str_list[j+k][i] != str_list[j+lenPattern-k-1][i]:
                        break
                else:
                    isFinished = True
                    max_lenPattern = lenPattern
                    break

            if isFinished: break
        if isFinished: break

    print('#{} {}'.format(test_case+1, max_lenPattern))