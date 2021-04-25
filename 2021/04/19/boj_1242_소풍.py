import sys
sys.stdin = open("input.txt","r")

N, K, M = map(int,input().split()) #M번 학생이 언제 퇴장하는가?

# 원형큐로 풀려고하다가 안됨..
front = 0 # 시작 인덱스
M -= 1  # 동호의 인덱스

# 돌아가는 총 경우의 수가 된다. i의 값이
for i in range(1, N + 1):
    # 제거할 인덱스를 구한다. 시작점 + 탈출할 인덱스를 전체 N으로 나눠서 계산
    removed = (front + K - 1) % N
    # 제거인덱스가 M과 동일하면 출력하고 나간다.
    if removed == M:
        print(i)
        break
        #동호의 위치가 더 크면 1을 줄여서 다시계산 제거점을 위치로 동호의 위치를 다시 계산하기 위함.
    if removed < M:
        M -= 1
        # 동호의 위치(인덱스)가 더 작으면 뒤에값이 빠지므로 그대로 패스
    else:
        pass
    # 시작점 빼준 인덱스에 할당하고 전체 길이를 하나 줄인다.
    front = removed
    N -= 1