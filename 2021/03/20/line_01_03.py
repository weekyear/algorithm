samples = [
    [[1,3,2], [1,2,3]]
    [[1,4,2,3], [2,1,3,4]],
    [[3,2,1], [2,1,3]],
    [[3,2,1], [1,3,2]],
    [[1,4,2,3], [2,1,4,3]],
]

def solution(enter, leave):
    len_e = len(enter) + 1
    answer = [0 for _ in range(len_e - 1)]
    # idx : 들어온 사람, value : 들어온 순서
    enter_order = [0 for _ in range(len_e)]
    leave_order = [0 for _ in range(len_e)]
    for i in range(len_e - 1):
        enter_order[enter[i]] = i
        leave_order[leave[i]] = i

    def combination(array, r):
        for i in range(len(array)):
            if r == 1:
                yield [array[i]]
            else:
                for next in combination(array[i + 1:], r - 1):
                    yield [array[i]] + next

    for i in combination([i for i in range(1, len_e)], 2):
        a, b = i
        if a != b:
            order_a_b = (enter_order[a] - enter_order[b]) // abs(enter_order[a] - enter_order[b])
            order_b_a = (leave_order[a] - leave_order[b]) // abs(leave_order[a] - leave_order[b])
            if order_a_b != order_b_a:
                answer[a - 1] += 1
                answer[b - 1] += 1
            else:
                before_enter = enter_order[b] if enter_order[a] > enter_order[b] else enter_order[a]
                after_enter = enter_order[a] if enter_order[a] > enter_order[b] else enter_order[b]
                after_value = leave_order[after_enter]
                e_after_a_b = []
                for e in range(before_enter + 1, after_enter):
                    e_after_a_b.append(enter[e])

                for f in e_after_a_b:
                    if leave_order[f] > after_value:
                        answer[a - 1] += 1
                        answer[b - 1] += 1
                        break

    return answer

for sample in samples:
    enter, leave = sample
    print(solution(enter, leave))

[2, 2, 1, 3]