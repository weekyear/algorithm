def solution(s):
    strings = list(map(lambda string: list(map(int, string.split(','))), s[2:len(s)-2].split('},{')))
    strings.sort(key=lambda elem: len(elem))
    answer = []
    visited = {}
    for string in strings:
        for num in string:
            if not visited.get(num, False):
                visited[num] = True
                answer.append(num)
                break
    return answer