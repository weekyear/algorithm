def combination_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combination_2(array[i+1:], r-1):
                yield [array[i]] + next

# for i in combination_2([1, 2, 3, 4], 3):
#     print(i, end=" ")


def permutation(array, r, prefix="nothing"):
    for i in range(len(array)):
        if prefix == array[i]: continue
        if r == 1:
            yield [array[i]]
        else:
            for next in permutation(array, r-1, array[i]):
                yield [array[i]] + next

# for i in permutation([1, 2, 3, 4], 3):
#     print(i, end=' ')

visited = [0 for _ in range(5)]

def permutations_3(array, r, prefix="nothing"):
    for i in range(len(array)):
        if array[i] == prefix: continue
        if r == 1:
            yield [array[i]]
        else:
            temp = [i for i in array]
            temp.remove(array[i])
            for next in permutations_3(temp, r-1, prefix):
                yield [array[i]] + next

for i in permutations_3([1, 2, 3], 2):
    print(i, end=' ')