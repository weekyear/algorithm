class Solution {
    fun solution(s: String): String {
        return if (s.length % 2 == 1) s[s.length / 2].toString() else s.slice(s.length / 2 - 1..s.length / 2)
    }
}