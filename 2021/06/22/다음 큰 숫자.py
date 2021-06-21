def solution(n):
    answer = 0
    binary = bin(n)[2:]
    len_b = len(bin(n)[2:])
    cnt_1 = binary.count('1')
    for i in range(n + 1, 2 ** (len_b+2)):
        if cnt_1 ==  bin(i).count('1'):
            answer = i
            break

    return answer