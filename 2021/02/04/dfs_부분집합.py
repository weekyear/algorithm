peoples = ['A', 'B', 'C']
result = []

def dfs(k):
    if k == len(peoples):
        print(result)
        return

    result.append(peoples[k])
    dfs(k + 1)
    result.pop()
    dfs(k + 1)

dfs(0)