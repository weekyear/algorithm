def solution(expression):
    ex = 0
    start = 0
    nums, operators = [], []
    for ex in range(len(expression)):
        if expression[ex].isdigit():
            continue
        else:
            nums.append(int(expression[start:ex]))
            operators.append(expression[ex])
            start = ex + 1
    else:
        nums.append(int(expression[start:ex + 1]))

    cases = [
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '+', '*'),
        ('-', '*', '_'),
    ]

    max_val = -1
    for case in cases:
        temp_nums = nums[:]
        temp_operaotrs = operators[:]
        for oper in case:
            o = 0
            while o < len(temp_operaotrs):
                if temp_operaotrs[o] == oper:
                    if oper == '*':
                        temp_nums[o] *= temp_nums[o + 1]
                    elif oper == '+':
                        temp_nums[o] += temp_nums[o + 1]
                    else:
                        temp_nums[o] -= temp_nums[o + 1]
                    temp_nums.pop(o + 1)
                    temp_operaotrs.pop(o)
                else:
                    o += 1
        else:
            if max_val < abs(temp_nums[0]):
                max_val = abs(temp_nums[0])

    return max_val