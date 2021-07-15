import kotlin.math.*

class Solution {
    fun solution(a: Int, b: Int): Long {
        val aLong = a.toLong()
        val bLong = b.toLong()
        if (aLong == bLong) { return aLong }

        var len = abs(bLong - aLong) + 1

        if (len % 2 == 0L) {
            return (aLong + bLong) * (len / 2)
        } else {
            return (aLong + bLong) * (len / 2) + (aLong + bLong) / 2
        }
        return 0L
    }
}