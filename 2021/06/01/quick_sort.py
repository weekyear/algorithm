def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

array = [1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432]
quick_sort(array)
print(array)