"""
Time: O(N+E), N is vertical, E is edge
Space: O(N), store vertical visited info

Notes:
1. Complexity see: https://www.jiuzhang.com/problem/search-graph-nodes/
2. Not sure why using node.label == target does not work, need to change to values[node] == target to be accepted
3. Need to keep visited tracker to avoid repeated visit

"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    """
    Not sure why using node.label == target does not work, need to change to values[node] == target to be accepted
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        if values[node] == target:
            return node
            
        queue = [node]
        visited = {}
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if values[curr] == target:
                    return curr
                visited[curr] = True
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                    
        return None
