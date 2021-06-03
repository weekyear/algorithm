import kotlin.random.Random
import kotlin.system.measureNanoTime

class Sort {

    fun bubbleSort(): List<Int> {
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
        var lst = createRandomNumberList()
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

    fun selectionSort(): List<Int> {
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
        var lst = createRandomNumberList()
        for (i in 0 until lst.count() - 1) {
            var minVal = 0xffffff
            var minIdx = -1
            for (j in i until lst.count()) {
                if (minVal > lst[j]) {
                    minVal = lst[j]
                    minIdx = j
                }
            }
            lst[minIdx] = lst[i]
            lst[i] = minVal
        }
        return lst
    }

    fun insertionSort(): List<Int> {
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
        var lst = createRandomNumberList()
        for (i in 1 until lst.count()) {
            for (j in i - 1 downTo 0) {
                if (lst[j] < lst[i]) {
                    val temp = lst[i]
                    lst.removeAt(i)
                    lst.add(j + 1, temp)
                    break
                }
            }
        }
        return lst
    }

    fun insertionSort_02(): List<Int> {
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
//        var lst = createRandomNumberList()
        var lst = mutableListOf(5, 3, 8, 4, 9, 1, 6, 2, 7)
        for (i in 1 until lst.count()) {
            val temp = lst[i]
            for (j in i - 1 downTo 0) {
                if (lst[j] < lst[i]) {
                    lst[j + 1] = temp
                    break
                } else {
                    lst[j + 1] = lst[j]
                }
            }
        }
        return lst
    }

    fun quickSort(array: MutableList<Int>, low: Int, high: Int) {
        if (high <= low) return

        val mid = partition(array, low, high)
        quickSort(array, low, mid - 1)
        quickSort(array, mid, high)
    }

    fun partition(array: MutableList<Int>, low: Int, high:Int): Int {
        val pivot = array[(low + high) / 2]
        var left = low
        var right = high
        while (left <= right) {
            while (array[left] < pivot) {
                left++
            }
            while (array[right] > pivot) {
                right--
            }
            if (left <= right) {
                val temp = array[left]
                array[left] = array[right]
                array[right] = temp
                left++
                right--
            }
        }
        return left
    }

    fun createRandomNumberList(): MutableList<Int> {
        val lottoNumbers = mutableListOf<Int>()

        while (lottoNumbers.size < 100000) {
            val randomNumber = Random.nextInt(1, 905856)

            if (lottoNumbers.contains(randomNumber)) {
                continue
            }

            lottoNumbers.add(randomNumber)
        }

        return lottoNumbers
    }
}

fun main(args: Array<String>) {
//    val elapsedBubble: Long = measureNanoTime {
//        Sort().bubbleSort()
//    }
//    println("버블 정렬 시간 : $elapsedBubble")
//
//    val elapsedSelection: Long = measureNanoTime {
//        Sort().selectionSort()
//    }
//    println("선택 정렬 시간 : $elapsedSelection")

    val elapsedInsertion02: Long = measureNanoTime {
        Sort().insertionSort_02()
    }
    println("삽입 정렬 시간 : $elapsedInsertion02")


    val elapsedQuickSort: Long = measureNanoTime {
        var lstRandom = Random
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
        var lst = mutableListOf(5, 3, 8, 4, 9, 1, 6, 2, 7)
//        var lst = Sort().createRandomNumberList()
        Sort().quickSort(lst, 0, lst.count() - 1)

        println(lst)
    }
    println("퀵 정렬 시간 : $elapsedQuickSort")
}