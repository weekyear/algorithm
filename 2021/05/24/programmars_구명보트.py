def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people) - 1
    while start <= end:
        answer += 1
        max_w = people[start]
        start += 1
        if people and max_w + people[end] <= limit:
            end -= 1

    return answer