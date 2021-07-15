import kotlin.math.*

class Solution {
    fun solution(n: Int): Int {
        val lst = mutableListOf<Int>()
        var _num = n
        while (_num != 0) {
            lst.add(_num % 3)
            _num /= 3
        }

        var result = 0
        for ((idx, value) in lst.withIndex()) {
            result += value * (3.toDouble().pow(lst.size - 1 - idx)).toInt()
        }

        return result
    }
}