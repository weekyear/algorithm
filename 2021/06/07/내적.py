def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

count = 0
for i in range(1, 101, 7):
    count += 1

print(count)

sum_num = 0
count = 1
while count < 101:
    sum_num += count
    count += 1

print(sum_num)
print(sum(range(1, 101)))

def sol(arr):
    visited = [0 for _ in range(101)]
    max_num = 0
    for elem in arr:
        visited[elem] += 1
        if max_num < elem:
            max_num = elem
    results = []
    for v in range(1, elem + 1):
        if visited[v] > 1:
            results.append(visited[v])

    return results if len(results) else [-1]

lst = [
    [1, 2, 3, 3, 3, 3, 4, 4],
    [3, 2, 4, 4, 2, 5, 2, 5, 5],
    [3, 5, 9, 7, 1]
]
for l in lst:
    print(sol(l))