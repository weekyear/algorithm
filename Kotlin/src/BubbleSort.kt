val lst = mutableListOf(1, 34, 5, 6, 78, 23, 56, 31, 64)

fun bubbleSort(): List<Int> {
    for (i in lst.indices) {
        for (j in 0 until lst.count()-1-i) {
            if (lst[j] > lst[j + 1]) {
                val temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
            }
        }
    }
    return lst
}