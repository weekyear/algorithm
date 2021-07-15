class Solution {
    fun solution(s: String): String {
        return s.toList().sortedBy { e -> -e.toInt() }.joinToString("")
    }
}