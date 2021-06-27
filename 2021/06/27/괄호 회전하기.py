def solution(s):
    len_s = len(s)
    answer = 0
    for x in range(len_s):
        close_dict = {']': '[', ')': '(', '}': '{'}
        Q = []
        for y in range(x, len_s + x):
            y %= len_s
            if s[y] == '[' or s[y] == '(' or s[y] == '{':
                Q.append(s[y])
            elif not len(Q) or Q.pop() != close_dict[s[y]]:
                break
        else:
            if not len(Q):
                answer += 1
    return answer