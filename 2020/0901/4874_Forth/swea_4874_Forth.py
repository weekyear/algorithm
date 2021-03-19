import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def is_operator(char):
    if char == '+' or char == '-' or char == '*' or char == '/':
        return True
    else:
        return False

def calculate(f_num, _operator, b_num):
    if _operator == '+':
        return f_num + b_num
    elif _operator == '-':
        return f_num - b_num
    elif _operator == '/':
        return f_num // b_num
    elif _operator == '*':
        return f_num * b_num

for tc in range(T):
    expression = input().split()

    num_stack = []
    top = -1
    flag = 0
    e_leng = len(expression) - 1

    for i in range(e_leng):
        char = expression[i]
        if is_operator(char):
            try:
                b_num, f_num = num_stack.pop(), num_stack.pop()
                top -= 2
                num_stack.append(calculate(f_num, char, b_num))
                top += 1
            except:
                flag = 1
                break
        else:
            num_stack.append(int(char))
            top += 1

    if flag or top != 0:
        result = 'error'
    else:
        result = num_stack.pop()

    print('#{} {}'.format(tc+1, result))