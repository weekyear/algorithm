def solution(s):
    from collections import deque
    Q = deque(s)
    results = []

    while Q:
        char = Q.popleft()
        if results and results[len(results) - 1] == char:
            results.pop()
        else:
            results.append(char)

    return 0 if len(results) else 1