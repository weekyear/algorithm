def solution(new_id):
    answer = []

    def delete_dot(answer):
        if len(answer) and answer[0] == '.':
            answer.pop(0)

        if len(answer) and answer[len(answer) - 1] == '.':
            answer.pop()

    for ch in new_id:
        if ch.isalpha():
            answer.append(ch.lower())
        elif ch.isdigit() or ch == '-' or ch == '_':
            answer.append(ch)
        elif ch == '.':
            if not len(answer) or answer[len(answer) - 1] != '.':
                answer.append(ch)

    delete_dot(answer)

    if not len(answer):
        answer.append('a')

    while len(answer) > 15:
        answer.pop()
    else:
        delete_dot(answer)

    while len(answer) < 3:
        answer.append(answer[len(answer) - 1])

    return ''.join(answer)