# def solution(a, edges):
#     all_sum = 0
#     for a_elem in a:
#         all_sum += a_elem
#
#     if all_sum != 0:
#         return -1
#
#     w_list = [[] for _ in range(len(a))]
#     for edge in edges:
#         w_list[edge[0]].append(edge[1])
#         w_list[edge[1]].append(edge[0])
#
#     # 중간에 w_list중 하나가 0이면 컷
#
#     Q = []
#     for a_idx in range(len(a)):
#         Q.append((a_idx, a[:], [0 for _ in range(a)]))
#
#
#     while Q:
#         cur_idx, cur_list, visited = Q.pop(0)
#
#         for w in w_list[cur_idx]:
#             if not visited[w]:
#
#
#
#     answer = -2
#     return answer