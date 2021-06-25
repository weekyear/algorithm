def solution(string):
    trans, zero = 0, 0
    while string != "1":
        trans += 1
        one_num = 0
        for s in string:
            if s == "1":
                one_num += 1
        zero += len(string) - one_num
        string = bin(one_num)[2:]

    return (trans, zero)