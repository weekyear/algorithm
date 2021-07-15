class Solution {
    fun solution(N: Int, number: Int): Int {
        var answer = -1

        val nums = Array(10) { mutableSetOf<Int>() }

        for (i in 1 until 10) {
            nums[i].add(Array(i) { "${N}" }.joinToString("").toInt())
            for (j in 0 until i) {
                for (elem1 in nums[j]) {
                    for (elem2 in nums[i - j]) {
                        nums[i].add(elem1 + elem2)
                        nums[i].add(elem1 - elem2)
                        nums[i].add(elem1 * elem2)
                        if (elem2 != 0) nums[i].add(elem1 / elem2)
                    }
                }
            }
            if (nums[i].contains(number)) {
                answer = i
                break
            }
        }

        return answer
    }
}