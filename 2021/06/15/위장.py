def solution(clothes):
    clothes_dict = {}
    for cloth, _type in clothes:
        clothes_dict[_type] = clothes_dict.get(_type, 1) + 1

    answer = 1
    for c in clothes_dict.values():
        answer *= c

    return answer - 1