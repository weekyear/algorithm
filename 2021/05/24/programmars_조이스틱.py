def solution(name):
    from collections import deque
    answer = 0xffffff

    len_n = len(name)
    Q = deque([(0, name[0] + 'A' * (len_n - 1), min(ord(name[0]) - 65, 91 - ord(name[0])))])

    while Q:
        c, cur_name, expense = Q.popleft()

        if cur_name == name and answer > expense:
            answer = expense
            break

        prev_c = c - 1 if c != 0 else len_n - 1
        cur_ex = 0
        cur_list = list(cur_name)
        if cur_name[prev_c] != name[prev_c]:
            cur_ex = min(ord(name[prev_c]) - 65, 91 - ord(name[prev_c]))
            cur_list[prev_c] = name[prev_c]
        Q.append((prev_c, ''.join(cur_list), expense + cur_ex + 1))

        post_c = c + 1
        if post_c < len_n:
            cur_ex = 0
            cur_list = list(cur_name)
            if cur_name[post_c] != name[post_c]:
                cur_ex = min(ord(name[post_c]) - 65, 91 - ord(name[post_c]))
                cur_list[post_c] = name[post_c]

            Q.append((post_c, ''.join(cur_list), expense + cur_ex + 1))

    return answer

print(solution("BBBBAAAABA"))