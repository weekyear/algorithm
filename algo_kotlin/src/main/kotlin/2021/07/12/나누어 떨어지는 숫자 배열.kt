class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        var answer = intArrayOf()

        arr.forEach { if (it % divisor == 0) { answer += it } }
        answer.sort()

        return if (answer.size > 0) answer else intArrayOf(-1)
    }
}