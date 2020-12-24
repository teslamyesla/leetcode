"""
Time: O(V + E)
Space: O(V)

"""

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

"""
Reference: https://www.jiuzhang.com/problem/clone-graph/#tag-lang-python
1.从原图给定的点找到所有点
2.复制所有的点 (用hashtable存对应点mapping)
3.复制所有的边
"""

class Solution:
    def cloneGraph(self, node):
        """
        Iterative:
        """
        if node is None:
            return None
            
        queue = [node]
        visited = {node: UndirectedGraphNode(node.label)}
        
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = UndirectedGraphNode(neighbor.label)
                visited[curr].neighbors.append(visited[neighbor])
                    
        return visited[node]

"""
Recurrsive:

class Solution:
    def __init__(self):
        self.mapping = {}
        
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None
        
        if node in self.mapping:
            return self.mapping[node]
            
        root = UndirectedGraphNode(node.label)
        self.mapping[node] = root
        
        for neighbor in node.neighbors:
            root.neighbors.append(self.cloneGraph(neighbor))
        
        return root
"""
        
        
