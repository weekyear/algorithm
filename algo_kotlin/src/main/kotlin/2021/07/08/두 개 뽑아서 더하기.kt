class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        val visited = Array(200, { false })
        for (i in 0 until numbers.size) {
            for (j in i + 1 until numbers.size) {
                val curSum = numbers[i] + numbers[j]
                if (!visited[curSum]) {
                    answer.add(curSum)
                    visited[curSum] = true
                }
            }
        }

        return answer.sorted().toIntArray()
    }
}