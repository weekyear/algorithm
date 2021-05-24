def solution(new_id):
    id_length = len(new_id)
    char_list = []
    print(0)
    for char in new_id:
        if char.isalpha():
            char_list.append(char.lower())
        elif char.isdigit() or char == '-' or char == '_':
            char_list.append(char)
        elif char == '.':
            if len(char_list) != 0 and len(char_list) != id_length - 1 and char_list[len(char_list) - 1] != '.':
                char_list.append(char)

    if len(char_list) == 0:
        char_list.append('a')

    while len(char_list) > 15:
        char_list.pop()

    if char_list[len(char_list) - 1] == '.':
        char_list.pop()

    while len(char_list) < 3:
        char_list.append(char_list[len(char_list) - 1])

    answer = ''.join(char_list)
    return answer