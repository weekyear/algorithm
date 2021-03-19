import sys
sys.stdin = open('input_1931.txt', 'r')

N = int(input())

schedules = []

for n in range(N):
    schedules.append(list(map(int, input().split())))

# 시작 시간과 종료 시간이 같은 회의가 앞에 배치될 수 도 있으므로 회의의 시작 시간이 2번째 조건으로 부여되어야 함
# 예시 : [11, 11] [8, 11]가 있을 경우 [11, 11]이 앞에 있다면
#       [8, 11]이 무시되고 [11, 11]만 등록된다.
schedules.sort(key=lambda x: (x[1], x[0]))
print(schedules)

final_time = 0
result = 0

for schedule in schedules:
    if schedule[0] >= final_time:
        result += 1
        final_time = schedule[1]

print(result)