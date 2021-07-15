def solution(n, t, m, p):
    str_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F']
    lst = [0]

    def convert(num, q):
        lst = []

        while num > 0:
            num, mod = divmod(num, q)
            lst.append(mod)

        return reversed(lst)

    for i in range(1, t * m):
        lst.extend(convert(i, n))

    answer = ''
    j = p - 1
    while len(answer) < t:
        answer += str_lst[lst[j]]
        j += m

    return answer