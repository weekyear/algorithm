import kotlin.math.*

class Solution {
    fun solution(arr: IntArray): Int {
        var a = arr[0]
        var b = 0
        for (idx in 1 until arr.size) {
            var b = arr[idx]
            var c = a
            var d = b
            if (d > c) {
                val temp = c
                c = d
                d = temp
            }

            while (d > 0) {
                val temp = d
                d = c % d
                c = temp
            }
            a = a * b / c
        }
        return a
    }
}