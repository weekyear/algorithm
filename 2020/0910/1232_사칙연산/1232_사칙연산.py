import sys

sys.stdin = open('input.txt', 'r')

def is_operator(char):\
    return char in ['*', '/', '+', '-']

def calculate(f_num, _operator, b_num):
    if _operator == '+':
        return f_num + b_num
    elif _operator == '-':
        return f_num - b_num
    elif _operator == '/':
        return f_num / b_num
    elif _operator == '*':
        return  f_num * b_num

def inorder(v):
    if is_operator(tree[v]):
        return calculate(inorder(L[v]), tree[v], inorder(R[v]))
    else:
        return int(tree[v])

for tc in range(10):
    N = int(input())
    tree = ['0'] * (N+1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)

    for n in range(1, N+1):
        input_data = input().split()
        for i in range(1, len(input_data)):
            if i < 2:
                tree[n] = input_data[i]
            else:
                if not L[n]:
                    L[n] = int(input_data[i])
                else:
                    R[n] = int(input_data[i])

    print('#{} {}'.format(tc+1, int(inorder(1))))