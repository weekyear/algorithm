def solution(files):
    from collections import defaultdict
    exception = {' ': 1, '.': 1, '-': 1}
    exception = defaultdict(int, exception)
    answer = []
    file_dict = {}
    for f in range(len(files)):
        head, number = [], []
        for i in range(len(files[f])):
            if files[f][i].isdigit():
                break
            head.append(files[f][i])
        head = ''.join(head).lower()

        for j in range(i, len(files[f])):
            if files[f][j].isalpha() or exception[files[f][j]]:
                break
            number.append(files[f][j])
        number = int(''.join(number))
        if not file_dict.get((head, number), False):
            file_dict[(head, number)] = []
        file_dict[(head, number)].append(f)

    key_list = list(file_dict.keys())
    key_list.sort(key=lambda x: (x[0], x[1]))
    for key in key_list:
        for k in file_dict[key]:
            answer.append(files[k])
    return answer