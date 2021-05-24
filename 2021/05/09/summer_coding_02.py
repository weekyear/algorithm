def solution(t, r):
    lst = []
    final_client = 0
    for i in range(len(t)):
        lst.append((t[i], r[i], i))
        if t[i] > final_client:
            final_client = t[i]

    lst.sort(key=lambda l:(l[0], l[1]))

    time = 0
    Q = []
    answer = []
    while Q or lst:
        while True:
            if len(lst) and lst[0][0] <= time:
                Q.append(lst.pop(0))
            else:
                break
        Q.sort(key=lambda l:(l[1], l[0]))
        if len(Q):
            answer.append(Q.pop(0)[2])
        time += 1

    return answer

print(solution([0, 1, 3, 0, 0], [0,1,2,0,1]))