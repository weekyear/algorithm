import kotlin.system.measureNanoTime

class Solution {
//    fun solution(sizes: Array<IntArray>): Int {
//        var max_x = 0
//        var max_y = 0
//        for (size in sizes) {
//            val cur_x = size.max()
//            val cur_y = size.min()
//            if (cur_x ?: 0 > max_x) {
//                max_x = cur_x ?: 0
//            }
//
//            if (cur_y ?: 0 > max_y) {
//                max_y = cur_y ?: 0
//            }
//        }
//
//        return max_x * max_y
//    }
//
//    fun solution(bricks: IntArray, n: Int, k: Int): Int {
//        val comb = mutableListOf<MutableList<Int>>()
//        fun combination(arr: IntArray, visited: BooleanArray, start: Int, m: Int, r: Int) {
//            if (r == 0) {
//                print(visited)
//            }
//
//            for (i in start until n) {
//                visited[i] = true
//                combination(arr, visited, i + 1, n , r - 1)
//                visited[i] = false
//            }
//        }
//        val elements = 1 until (bricks.size - 1)
//        val visited = Array(bricks.size) { false }
//        combination(elements.toList().toIntArray(), visited.toBooleanArray(), 1, bricks.size - 2, 2)
//        var answer: Int = 0
//        return answer
//    }

    fun solution(m: IntArray): Int {
        val queue = mutableListOf<IntArray>()
        val maxIdx = m.size - 1
        val destinations = mutableListOf<Int>()
        val visited = Array(m.size) { false }.toBooleanArray()
        var answer = 0

        for ((idx, value) in m.withIndex()) {
            var dest = idx
            while (m[dest] != 0) {
                dest += m[dest]
                dest = if (dest < 0) 0 else dest
                dest = if (dest > maxIdx) maxIdx else dest
            }
            destinations.add(dest)
        }

        visited[0] = true
        queue.add(intArrayOf(0, 0))
        while (queue.size > 0) {
            val pos = queue[0][0]
            val step = queue[0][1]
            queue.removeAt(0)

            for (i in 1..6) {
                if (pos + i >= maxIdx || destinations[pos + i] >= maxIdx) {
                    answer = step + 1
                    break
                }
                if (!visited[pos + i]) {
                    visited[pos + i] = true
                    queue.add(intArrayOf(destinations[pos + i], step + 1))
                }
            }
            if (answer != 0) {
                break
            }
        }
        return answer
    }

}

fun main(args: Array<String>) {
    print(Solution().solution(intArrayOf(0,0,0,0,0,0,0,0,0)))
}