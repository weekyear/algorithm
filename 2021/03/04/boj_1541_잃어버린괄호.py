import sys
sys.stdin = open('input_1541.txt', 'r')

info = input().split('-')

result = 0

for i_1 in range(len(info)):
    cur_sum = sum(map(int, info[i_1].split('+')))

    if i_1 > 0:
        result -= cur_sum
    else:
        result += cur_sum

print(result)

