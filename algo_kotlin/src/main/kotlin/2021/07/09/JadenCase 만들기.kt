class Solution_1 {
    fun solution(s: String): String {
        var answer = StringBuilder()
        for (c in 0 until s.length) {
            answer.append(if (c == 0 || s[c - 1] == ' ') s[c].toUpperCase() else s[c].toLowerCase())
        }
        return answer.toString()
    }
}

class Solution_2 {
    fun solution(s: String): String {
        return s.toLowerCase().split(" ").map {
            it.capitalize()
        }.joinToString(" ")
    }
}