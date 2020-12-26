"""
Time: O(V + E)
Space: O(V)

Note:
1. input type is a list of directed graph node, thus initialized indegree dictionary by for loop nodes in list
2. topological order return type is a list of nodes, not a list of values

"""

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree = {x: 0 for x in graph}
        
        for node in indegree:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
                
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        res = []    
        while queue:
            node = queue.pop(0)
            res.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res
        
        
