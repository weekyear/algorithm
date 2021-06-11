def binary_search(lst, goal):
    lst.sort()
    left, right = 0, len(lst) - 1

    while left < right:
        mid = (left + right) // 2
        if lst[mid] > goal:
            right = mid - 1
        elif lst[mid] < goal:
            left = mid + 1
        else:
            break


print(binary_search([4, 3, 6, 2, 8, 1, 9, 5, 7], 6))