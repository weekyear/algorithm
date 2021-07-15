package `2021`.`07`.`05`

class Solution {
    fun solution(left: Int, right: Int): Int {
        val oddList = Array(1001, {false})
        var n = 1
        while (n * n <= 1000) {
            oddList[n * n] = true
            n += 1
        }

        var answer = (left..right).reduce { total, next ->
            total + if (oddList[next]) -next else next
        }

        return answer
    }
}