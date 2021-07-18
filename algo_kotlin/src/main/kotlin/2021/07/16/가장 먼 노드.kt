class Solution {
    fun solution(n: Int, edges: Array<IntArray>): Int {
        val graph = Array(n + 1) { mutableListOf<Int>() }

        for (edge in edges) {
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }

        val visited = Array(n + 1) { -1 }
        visited[1] = 0
        var maxVal = 0
        val queue = mutableListOf(arrayOf(1, 0))

        while (queue.size > 0) {
            val infos = queue.removeAt(0)

            for (w in graph[infos[0]]) {
                if (visited[w] == -1) {
                    visited[w] = infos[1] + 1
                    if (maxVal < visited[w]) { maxVal = visited[w] }
                    queue.add(arrayOf(w, visited[w]))
                }
            }
        }

        return visited.count { elem -> elem == maxVal}
    }
}