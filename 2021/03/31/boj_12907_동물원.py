import sys
sys.stdin = open('boj_12907.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))

# 숫자는 최대 2개의 라인으로 0부터 차곡차곡 쌓여가야 한다.
# 특정 숫자가 끊기면 바로 0을 반환
# 특정 숫자가 3개가 쌓여가면 NG

visited = [0 for _ in range(N)]
result = 0
for num in nums:
    if num > N - 1:
        break
    visited[num] += 1
    if visited[num] > 2:
        break
else:
    max_idx = 0
    for v in range(N):
        if not result:
            if visited[v] != 2:
                result = 2 ** (v + visited[v])
                max_idx = v
                break

    for w in range(max_idx, N - 1):
        if visited[w + 1] > visited[w]:
            result = 0
            break

print(result)