def solution(p):
    def isRight(string):
        stack = 0
        for s in string:
            if s == '(':
                stack += 1
            elif s == ')':
                stack -= 1
            if stack < 0:
                return False
        if stack == 0:
            return True
        return False

    def divideUV(string):
        stack = 0
        for s in range(len(string)):
            if string[s] == '(':
                stack += 1
            elif string[s] == ')':
                stack -= 1
            if stack == 0:
                return s + 1

    def recur(string):
        if string == '':
            return ''
        idx = divideUV(string)
        u, v = string[:idx], string[idx:]
        if isRight(u):
            return u + recur(v)
        else:
            n_string = '('
            n_string += recur(v) + ')'
            new_u = ''
            for n in u[1:len(u) - 1]:
                if n == '(':
                    new_u += ')'
                else:
                    new_u += '('
            n_string += new_u
            return n_string

    return recur(p)

print(solution("()))((()"))