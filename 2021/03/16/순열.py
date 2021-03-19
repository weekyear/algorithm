# def permutation(array, r):
#     for i in range(len(array)):
#         if r == 1:
#             yield [array[i]]
#         else:
#             temp = [n for n in array]
#             temp.remove(array[i])
#             for j in permutation(temp, r - 1):
#                 yield [array[i]] + j
#
# for k in permutation([1, 2, 3, 4], 3):
#     print(k, end=" ")
#
# print()
#
# def combination(array, r):
#     for i in range(len(array)):
#         if r == 1:
#             yield [array[i]]
#         else:
#             for j in permutation(array[i+1:], r - 1):
#                 yield [array[i]] + j
#
# for k in combination([1, 2, 3, 4], 3):
#     print(k, end=" ")
#
print(int(-0.545))