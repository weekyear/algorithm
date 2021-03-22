import sys
sys.stdin = open('input_11047.txt', 'r')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

remain_price = K
result = 0
for n in range(N - 1, -1, -1):
    if coins[n] <= remain_price:
        num_coins = remain_price // coins[n]
        remain_price -= coins[n] * num_coins
        result += num_coins

        if remain_price == 0:
            break

print(result)

# DFS로 푸니 실패
# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]
#
# def dfs(remains, k, max_coin):
#     global result
#     if k >= result or max_coin == -1:
#         return
#
#     for n in range(max_coin, -1, -1):
#         if coins[n] < remains:
#             num_coins = remains // coins[n]
#             for m in range(num_coins, -1, -1):
#                 added_price = coins[n] * m
#                 if remains - added_price > 0:
#                     dfs(remains - added_price, k + m, n - 1)
#                 elif remains - added_price == 0:
#                     if result > k + m:
#                         result = k + m
#
# over_coin_idx = 0
# for n in range(N - 1, -1, -1):
#     if coins[n] < K:
#         over_coin_idx = n
#         break
#
# result = 0xffffff
# dfs(K, 0, over_coin_idx)
#
# print(result)

# BFS로 푸니 실패
# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]
#
# Q = []
# over_coin_idx = 0
# for n in range(N - 1, -1, -1):
#     if coins[n] <= K:
#         Q.append((coins[n], 1))
#     else:
#         over_coin_idx = n
#
# result = 0
# while Q:
#     price, k = Q.pop(0)
#
#     for n in range(over_coin_idx, -1, -1):
#         new_price = price + coins[n]
#         if new_price < K:
#             Q.append((new_price, k + 1))
#         elif new_price == K:
#             result = k + 1
#             break
#     if result:
#         break
#
# print(result)