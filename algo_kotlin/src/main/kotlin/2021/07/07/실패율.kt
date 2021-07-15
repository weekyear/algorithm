class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        val failedUsers = Array(N + 2, { 0 })
        val stageUsers = Array(N + 2, { 0 })
        for (stage in stages) {
            for (i in 1..stage) {
                stageUsers[i] += 1
            }
            failedUsers[stage] += 1
        }

        val sortArray = Array(N + 2, { mutableListOf<Float>() })
        for ((idx, user) in stageUsers.withIndex()) {
            sortArray[idx].add(idx.toFloat())
            if (user != 0) {
                sortArray[idx].add(failedUsers[idx].toFloat() / user.toFloat())
            } else {
                sortArray[idx].add(0f)
            }
        }

        var answer = mutableListOf<Int>()

        for (elem in sortArray.sortedBy { -it[1] }) {
            val curUser = elem[0].toInt()
            if (curUser != 0 && curUser != N + 1) {
                answer.add(curUser)
            }
        }
        return answer.toIntArray()
    }
}