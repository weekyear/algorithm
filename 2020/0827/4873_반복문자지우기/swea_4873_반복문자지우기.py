import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    str_sample = input()

    stack = []

    for char in str_sample:
        if stack:
            last_elem = stack[len(stack)-1]
            if last_elem == char:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    print('#{} {}'.format(tc+1, len(stack)))