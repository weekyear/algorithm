package `2021`.`07`.`05`

class Solution {
    fun solution(nums: IntArray): Int {
        val allSum = nums.sum()
        val primarys = Array(allSum + 1, {true})
        val visited = Array(allSum + 1, {false})
        var answer = 0

        for (i in 2..allSum) {
            var j = i
            while (j + i < allSum + 1) {
                j += i
                primarys[j] = false
            }
        }

        fun combination(arr: IntArray, check: Array<Boolean>, start: Int, n: Int) {
            if (n == 0) {
                val comb = listOf(arr.filterIndexed {idx, t -> check[idx]})
                for (c in comb) {
                    if (primarys[c.sum()]) {
                        answer += 1
                    }
                }

            } else {
                for (i in start until arr.size) {
                    check[i] = true
                    combination(arr, check, i + 1, n - 1)
                    check[i] = false
                }
            }
        }

        combination(nums, Array(nums.size, {false}), 0, 3)

        return answer
    }
}