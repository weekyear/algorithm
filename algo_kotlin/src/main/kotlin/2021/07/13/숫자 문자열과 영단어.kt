class Solution {
    fun solution(s: String): Int {
        var str = s
        val alphabets = mapOf("zero" to "0", "one" to "1", "two" to "2", "three" to "3",
            "four" to "4", "five" to "5", "six" to "6", "seven" to "7",
            "eight" to "8", "nine" to "9")

        for (alpha in alphabets.keys) {
            str = str.replace(alpha, alphabets[alpha] ?: "")
        }
        return str.toInt()
    }
}
