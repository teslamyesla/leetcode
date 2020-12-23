"""
Time: O(V + E)
Space: O(V + E)

Reference of complexity analysis: https://www.jiuzhang.com/problem/course-schedule/#tag-lang-python

时间复杂度O(V + E)

    建图，扫描一遍所有的边O(E)。
    每个节点最多入队出队1次，复杂度O(V)。
    邻接表最终会被遍历1遍，复杂度O(E)。
    综上，总复杂度为O(E + V)。

空间复杂度O(V + E)

    邻接表占用O(E + V)的空间。
    队列最劣情况写占用O(V)的空间。
    综上，总复杂度为O(V + E)。
    
"""

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        indegree = {x:0 for x in range(numCourses)}
        neighbors = {x:[] for x in range(numCourses)}
        
        for node_next, node_prev in prerequisites:
            indegree[node_next] += 1
            neighbors[node_prev].append(node_next)
            
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        visited = []
        while queue:
            node = queue.pop(0)
            visited.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return len(visited) == numCourses
