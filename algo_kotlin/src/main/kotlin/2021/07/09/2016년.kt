class Solution {
    fun solution(a: Int, b: Int): String {
        val calendar = listOf(31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        val daysOfWeek = listOf("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")

        var days = (0 until a - 1).fold(0) { total, next ->
            total + calendar[next]!!
        } + b - 1

        var answer = daysOfWeek[days % 7]
        return answer
    }
}