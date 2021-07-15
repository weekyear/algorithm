def solution(msg):
    dictionary = {}
    answer = []
    for i in range(65, 91):
        dictionary[chr(i)] = i - 64

    cur_key = 27
    n, m = -1, 0

    while n < len(msg) - 1:
        n += 1
        w = msg[n]
        while n < len(msg) and dictionary.get(w):
            if n + 1 > len(msg) - 1:
                answer.append(dictionary.get(w))
                break

            if not dictionary.get(w + msg[n + 1], False):
                answer.append(dictionary.get(w))
                dictionary[w + msg[n + 1]] = cur_key
                cur_key += 1
                break
            else:
                n += 1
                w += msg[n]

    return answer

print(solution("KAKAO"))