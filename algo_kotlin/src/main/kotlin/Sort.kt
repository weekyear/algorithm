import kotlin.random.Random
import kotlin.system.measureNanoTime

class Sort {
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

    fun mergeSort(array: MutableList<Int>, start: Int, end: Int) {
        if (start >= end) return

        val mid = (start + end) / 2
        mergeSort(array, start, mid)
        mergeSort(array, mid + 1, end)

        merge(array, start, mid, end)
    }

    fun merge(array: MutableList<Int>, start: Int, mid:Int, end: Int) {
        val newList = mutableListOf<Int>()
        var idxA = start
        var idxB = mid + 1

        while (idxA <= mid && idxB <= end) {
            if (array[idxA] <= array[idxB]) {
                newList.add(array[idxA])
                idxA++
            } else {
                newList.add(array[idxB])
                idxB++
            }
        }

        if (idxA > mid) {
            for (i in idxB..end) {
                newList.add(array[i])
            }
        }

        if (idxB > end) {
            for (i in idxA..mid) {
                newList.add(array[i])
            }
        }

        for (e in newList.indices) {
            array[start + e] = newList[e]
        }
    }

    fun heapSort(array: MutableList<Int>): List<Int> {
        var results = mutableListOf<Int>()
        // array ?????? ?????? ??????
        var arrayLen = array.count()
        // max heap ?????????
        // ?????? ????????? ?????? ???????????? ??????
        for (i in arrayLen / 2 - 1 downTo 0) {
            heapify(array, arrayLen, i)
        }

        // ????????? ??????
        for (j in arrayLen - 1 downTo 0) {
            results.add(array[0])
            array[0] = array[j]
            heapify(array, --arrayLen, 0)
        }
        return results
    }


    fun heapify(array: MutableList<Int>, heapSize: Int, pIdx: Int) {
        // ?????? ??????, ?????? ?????? ??????, ?????? ?????? ?????? ??????
        var p = pIdx
        var l = pIdx * 2 + 1
        var r = pIdx * 2 + 2
        // ?????? ?????? ????????? ??????
        if (l < heapSize && array[l] < array[p]) {
            p = l
        }
        // ????????? ?????? ????????? ??????
        if (r < heapSize && array[r] < array[p]) {
            p = r
        }

        // ?????? ????????? ????????? ?????? ????????? ?????? ????????? ????????????
        if (pIdx != p) {
            val temp = array[p]
            array[p] = array[pIdx]
            array[pIdx] = temp
            heapify(array, heapSize, p)
        }
    }

    fun solution(m: IntArray): Int {
        val queue = mutableListOf<IntArray>()
        val maxIdx = m.size - 1
        val destinations = mutableListOf<Int>()
        val visited = Array(m.size) { false }.toBooleanArray()
        var answer = 0

        for ((idx, value) in m.withIndex()) {
            var dest = idx
            while (m[dest] != 0) {
                dest += m[dest]
                dest = if (dest < 0) 0 else dest
                dest = if (dest > maxIdx) maxIdx else dest
            }
            destinations.add(dest)
        }

        while (queue.size > 0) {
            val pos = queue[0][0]
            val step = queue[0][1]
            queue.removeAt(0)

            for (i in 1..6) {
                if (pos + i >= maxIdx || destinations[pos + i] >= maxIdx) {
                    answer = step + 1
                }
                if (!visited[pos + i]) {
                    visited[pos + i] = true
                    queue.add(intArrayOf(destinations[pos + i], step + 1))
                }
            }
        }
        return answer
    }
}

fun main(args: Array<String>) {
    println(mutableListOf(5, 3, 8, 4, 9, 1, 6, 2, 7))
//    val elapsedBubble: Long = measureNanoTime {
//        Sort().bubbleSort()
//    }
//    println("?????? ?????? ?????? : $elapsedBubble")
//
//    val elapsedSelection: Long = measureNanoTime {
//        Sort().selectionSort()
//    }
//    println("?????? ?????? ?????? : $elapsedSelection")
//
//    val elapsedInsertion02: Long = measureNanoTime {
//        Sort().insertionSort_02()
//    }
//    println("?????? ?????? ?????? : $elapsedInsertion02")
//
//    val elapsedQuickSort: Long = measureNanoTime {
//        var lstRandom = Random
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
//        var lst = mutableListOf(5, 3, 8, 4, 9, 1, 6, 2, 7)
//        var lst = Sort().createRandomNumberList()
//        Sort().quickSort(lst, 0, lst.count() - 1)
//    }
//    println("??? ?????? ?????? : $elapsedQuickSort")
//
//    val elapsedMergeSort: Long = measureNanoTime {
//        var lstRandom = Random
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
//        var lst = mutableListOf(5, 3, 8, 4, 9, 1, 6, 2, 7)
//        Sort().mergeSort(lst, 0, lst.count() - 1)
//    }
//    println("?????? ?????? ?????? : $elapsedMergeSort")

    val elapsedHeapSort: Long = measureNanoTime {
//        var lst = mutableListOf(1, 34, 5, 60, 78, 23, 56, 31, 64, 45, 63, 44, 78, 5345, 6, 35634, 74545, 478, 95, 243452, 757, 845, 3534, 243, 6456, 967, 43242, 432)
        var lst = mutableListOf(5, 3, 8, 4, 9, 1, 6, 2, 7)
        println(Sort().heapSort(lst))
    }
    println("?????? ?????? ?????? : $elapsedHeapSort")
}