def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        cur_answer = 0
        temp = s[:i]
        count = 1
        for j in range(i, len(s), i):
            next_temp = s[j:i + j]
            if temp == next_temp:
                count += 1
            else:
                if count == 1:
                    count = ""

                cur_answer += len(str(count) + temp)
                temp = next_temp
                count = 1
        else:
            if count == 1:
                count = ""

            cur_answer += len(str(count) + temp)

        if cur_answer < answer:
            answer = cur_answer

    return answer

lst = [
    "aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"
]

for l in lst:
    print(solution(l))