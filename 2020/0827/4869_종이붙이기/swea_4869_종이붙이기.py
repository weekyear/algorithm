import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

result = 0

def solve(cur_stack, num, two_stack):
    global result
    for i in range(2):
        if i == 0:
            new_stack = cur_stack + 10
        else:
            new_stack = cur_stack + 20
            two_stack += 1

        if new_stack == num:
            result += 2 ** two_stack
        elif new_stack < num:
            solve(new_stack, num, two_stack)

for test_case in range(T):
    N = int(input())
    result = 0
    solve(0, N, 0)

    print('#{} {}'.format(test_case+1, result))