def solution(number, k):
    answer = []
    remains = len(number) - k
    start = 0
    end = len(number) - (len(number)-k - 1)

    for r in range(remains):
        max_val = '0'
        max_idx = start
        for i in range(start, end):
            if i < len(number):
                if max_val < number[i]:
                    max_val = number[i]
                    max_idx = i
                    if max_val == '9':
                        break
        answer.append(max_val)
        start = max_idx + 1
        end += 1

    return ''.join(answer)


# print(solution("4177252841", 4))
print(solution("1231234", 3))
