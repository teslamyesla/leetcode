"""
Similiar as 0615 course schedule

Time: O(V + E)
Space: O(V + E)

"""

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        indegree = {x : 0 for x in range(numCourses)}
        neighbors = {x : [] for x in range(numCourses)}
        
        for node_next, node_prev in prerequisites:
            indegree[node_next] += 1
            neighbors[node_prev].append(node_next)
            
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
                
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res if len(res) == numCourses else []
