def solution(n, words):
    visited = {}

    answer = [0, 0]
    last_word = words[0][0]

    for w in range(len(words)):
        if not visited.get(words[w], False) and last_word == words[w][0] and len(words[w]) > 1:
            visited[words[w]] = 1
            last_word = words[w][len(words[w]) - 1]
        else:
            answer = [w % n + 1, w // n + 1]
            break

    return answer