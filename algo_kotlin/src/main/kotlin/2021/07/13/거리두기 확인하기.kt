import kotlin.math.*

class Solution {
    fun solution(places: Array<Array<String>>): IntArray {
        var answer = mutableListOf<Int>()
        val dyx = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))

        val lenP = places.size
        for (p in 0 until lenP) {
            val lenY = places[p].size
            for (y in 0 until lenY) {
                if (answer.size != p) { break }
                val lenX = places[p][y].length
                for (x in 0 until lenX) {
                    if (answer.size != p) { break }
                    if (places[p][y][x] == 'P') {
                        var Q = mutableListOf<IntArray>()
                        Q.add(intArrayOf(y, x))
                        val visited = Array(lenY) { BooleanArray(lenX) }
                        visited[y][x] = true

                        while (Q.size > 0) {
                            if (answer.size != p) { break }

                            val cur = Q.removeAt(0)

                            for (d in dyx) {
                                if (answer.size != p) { break }
                                val newY = cur[0] + d[0]
                                val newX = cur[1] + d[1]
                                val dist = abs(newY - y) + abs(newX - x)

                                if (-1 < newY && newY < lenY && -1 < newX && newX < lenX && dist <= 2 && !visited[newY][newX]) {
                                    when(places[p][newY][newX]) {
                                        'O' -> {
                                            Q.add(intArrayOf(newY, newX))
                                            visited[newY][newX] = true
                                        }

                                        'P' -> {
                                            answer.add(0)
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            if (answer.size == p) {
                answer.add(1)
            }
        }


        return answer.toIntArray()
    }
}