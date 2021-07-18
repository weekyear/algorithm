class Solution {
    fun solution(n: Int, times: IntArray): Long {
        var answer: Long = 0
        var start: Long = 0
        var end: Long = ((times.min() ?: 0).toLong() * n.toLong())

        while (start <= end) {
            var mid = (start + end) / 2
            var count: Long = 0

            for (time in times) {
                count += mid / time
                if (count > n) { break }
            }

            if (count >= n) {
                answer = mid
                end = mid - 1
            } else {
                start = mid + 1
            }
        }


        return answer
    }
}