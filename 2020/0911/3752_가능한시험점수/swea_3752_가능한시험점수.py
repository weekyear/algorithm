import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

# 새로운 방식
for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    all_sum = 0
    for i in range(len(num_list)):
        all_sum += num_list[i]

    result = [0]
    visited = [1] + [0] * all_sum
    for i in num_list:
        for j in range(len(result)):
            n_val = i + result[j]
            if not visited[n_val]:
                visited[n_val] = 1
                result.append(n_val)

    print('#{} {}'.format(tc+1, len(result)))

    # result = {}
    # count = 0
    #
    # # 같은 높이에서 같은 숫자를 제거해주면 됨
    # # BFS로 같은 높이의 값을 제거
    #
    # Q = [0]
    #
    # for n in range(N):
    #     pop_list = []
    #     while Q:
    #         pop_list.append(Q.pop())
    #     check_dict = {}
    #     for q in range(len(pop_list)):
    #         q_val = pop_list[q]
    #         if check_dict.get(q_val, -1) == -1:
    #             Q.append(q_val)
    #             check_dict[q_val] = 1
    #
    #         q_val += num_list[n]
    #         if check_dict.get(q_val, -1) == -1:
    #             Q.append(q_val)
    #             check_dict[q_val] = 1

    # print('#{} {}'.format(tc+1, len(Q)))

# 도대체 이해가 되지 않는 코드
# for t in range(int(input())):
#     input()
#     a = 1
#     for i in map(int, input().split()):
#         a |= a << i
#     print(f'#{t+1}',bin(a).count('1'))