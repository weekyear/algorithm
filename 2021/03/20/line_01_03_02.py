samples = [
    [[1, 3, 2], [1, 2, 3]],
    [[1, 4, 2, 3], [2, 1, 3, 4]],
    [[3, 2, 1], [2, 1, 3]],
    [[3, 2, 1], [1, 3, 2]],
    [[1, 4, 2, 3], [2, 1, 4, 3]],
]


def dfs(room, cur_enter, cur_leave, visited, k):
    global num_all_case
    global meet_stack
    if k == 2 * len_s:
        num_all_case += 1
        for y in range(1, len_s + 1):
            for x in range(1, len_s + 1):
                if visited[y][x] == 1:
                    meet_stack[y][x] += 1
        return

    if len(cur_enter):
        e = cur_enter.pop(0)
        cur_visited = [v[:] for v in visited]
        for s in room:
            cur_visited[s][e] += 1
            cur_visited[e][s] += 1
        room.append(e)
        dfs(room, cur_enter, cur_leave, cur_visited, k + 1)
        cur_enter.insert(0, e)
        room.pop()

    if len(room):
        if cur_leave and room.count(cur_leave[0]):
            remove_idx = room.index(cur_leave[0])
            l = cur_leave.pop(0)
            room.pop(remove_idx)
            dfs(room, cur_enter, cur_leave, visited, k + 1)
            cur_leave.insert(0, l)
            room.insert(remove_idx, l)


def solution(enter, leave):
    global len_s
    global num_all_case
    global meet_stack
    num_all_case = 0
    len_s = len(enter)
    answer = []
    visited = [[0 for _ in range(len_s + 1)] for _ in range(len_s + 1)]
    meet_stack = [[0 for _ in range(len_s + 1)] for _ in range(len_s + 1)]

    dfs([], enter, leave, visited, 0)

    for m in range(1, len(meet_stack)):
        cur_meet = 0
        for n in meet_stack[m]:
            if n == num_all_case:
                cur_meet += 1
        answer.append(cur_meet)

    return answer


for sample in samples:
    enter, leave = sample
    print(solution(enter, leave))