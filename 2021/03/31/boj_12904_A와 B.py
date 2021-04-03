import sys
sys.stdin = open('boj_12904.txt', 'r')

from collections import deque

S = input()
T = input()

Q = deque([T])
result = 0
lenS = len(S)

while Q:
    word = Q.popleft()
    n_word1 = ''
    n_word2 = ''

    if word[len(word) - 1] == 'A':
        n_word1 = word[:len(word) - 1]
        Q.append(n_word1)

    if word[len(word) - 1] == 'B':
        n_word2 = word[len(word)-2::-1]
        Q.append(n_word2)

    if n_word1 == S or n_word2 == S:
        result = 1
        break
    elif len(word) - 1 == lenS:
        break

print(result)

# 처음에 S에서부터 T로 BFS로 풀어봤는데 시간초과가 뜸
# visited = {T: 1}

# while Q:
#     word = Q.popleft()
#
#     n_word1 = word + 'A'
#     n_word2 = ''.join(reversed(word)) + 'B'
#
#     if n_word1 == T or n_word2 == T:
#         result = 1
#         break
#
#     if len(n_word1) < lenT and not visited.get(n_word1, False):
#         visited[n_word1] = True
#         Q.append(n_word1)
#
#     if len(n_word2) < lenT and not visited.get(n_word2, False):
#         visited[n_word2] = True
#         Q.append(n_word2)
