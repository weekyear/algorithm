import sys
sys.stdin = open('input.txt', 'r')

def push_operator(_operator):
    global oper_stack
    global top
    if _operator == ')':
        while oper_stack[top] != '(':
            expression.append(oper_stack.pop())
            top -= 1
        else:
            oper_stack.pop()
            top -= 1
        return

    if oper_stack:
        while icp[_operator] <= isp[oper_stack[top]]:
            expression.append(oper_stack.pop())
            top -= 1
        else:
            oper_stack.append(_operator)
            top += 1
    else:
        oper_stack.append(_operator)
        top = 0

def calculate(f_num, _operator, b_num):
    if _operator == '+':
        return f_num + b_num
    elif _operator == '-':
        return f_num - b_num
    elif _operator == '/':
        return f_num / b_num
    elif _operator == '*':
        return  f_num * b_num


for tc in range(1, 11):
    l = int(input())
    cal_str = input()

    isp = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    icp = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 3
    }

    oper_stack = []
    expression = []
    top = -1

    for i in range(l):
        char = cal_str[i]
        if '0' <= char <= '9':
            expression.append(char)
        else:
            push_operator(char)

    num_stack = []
    E = len(expression)

    for e in range(E):
        if '0' <= expression[e] <= '9':
            num_stack.append(int(expression[e]))
        else:
            b_num = num_stack.pop()
            f_num = num_stack.pop()
            num_stack.append(calculate(f_num, expression[e], b_num))

    print('#{} {}'.format(tc, num_stack.pop()))