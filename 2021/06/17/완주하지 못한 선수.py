def solution(participant, completion):
    dict_part = {}
    for key in participant:
        dict_part[key] = dict_part.get(key, 0) + 1

    for com in completion:
        dict_part[com] -= 1
        if dict_part[com] == 0:
            dict_part.pop(com)

    answer = list(dict_part.keys()).pop()
    return answer

["classic", "pop", "classic", "classic", "pop"]

[500, 600, 150, 800, 2500]