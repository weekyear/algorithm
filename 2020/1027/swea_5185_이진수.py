import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, hexStr = input().split()

    result_list = []
    for h in '19E1E19FE6781819E79F981E1E18':
        n = int(h, 16)
        result_list.append('1' if n & 8 else '0')
        result_list.append('1' if n & 4 else '0')
        result_list.append('1' if n & 2 else '0')
        result_list.append('1' if n & 1 else '0')
    print(len('1011000110101100010011001001001100011010001011010001100000000001101110100011011101101111010001011011000100110010001101'))
    print('#{} {}'.format(tc+1, ''.join(result_list)))