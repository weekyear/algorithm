import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    str_sample = input()

    stack = []
    isRight = 1
    for char in str_sample:
        if char == '{' or char == '(':
            stack.append(char)
        elif char == '}':
            if not stack or stack.pop() != '{':
                isRight = 0
                break
        elif char == ')':
            if not stack or stack.pop() != '(':
                isRight = 0
                break

    if stack:
        isRight = 0

    print('#{} {}'.format(tc+1, isRight))