def checkString(cur_str):
    a_stack = 0
    b_stack = 0
    c_stack = 0

    for s in cur_str:
        if s == '(':
            a_stack += 1
        elif s == '[':
            b_stack += 1
        elif s == '{':
            c_stack += 1
        elif s == ')':
            a_stack -= 1
        elif s == ']':
            b_stack -= 1
        elif s == '}':
            c_stack -= 1

        if a_stack < 0 or b_stack < 0 or c_stack < 0:
            return False

    if a_stack == b_stack == c_stack == 0:
        return True

    return False

def solution(string):
    answer = 0
    for s in range(len(string)):
        if checkString(string[s:len(string)] + string[:s]):
            answer += 1
    return answer

samples=["[](){}", "}]()[{", "[)(]", "}}}"]

for sample in samples:
    print(solution(sample))