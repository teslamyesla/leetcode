"""
树的三个特征：
1. 连通
2. n-1条边
3. 无环
满足以上任意两个条件即可

Solution 1: Check n-1 edges + DFS for graph connectivity

Time: O(V+E) = O(n)
Space: O(V+E) = O(n)

Solution 2: Check n-1 edges + Union find for graph cycle

Time: O(n)
Space: O(n)

"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    """
    Solution 2: Check n-1 edges + Union find for graph cycle
    """
    def validTree(self, n, edges):
        # write your code here
        
        if n == 0 or len(edges) != n - 1:
            return False
            
        parents = {x: x for x in range(n)}
        
        for node_A, node_B in edges:
            parent_A, parent_B = self.find(node_A, parents), self.find(node_B, parents)
            
            if parent_A == parent_B: # has cycle
                return False
                
            parents[parent_A] = parent_B
        
        # no cycle  
        return True
        
    def find(self, x, parents):
        if x == parents[x]:
            return x
            
        return self.find(parents[x], parents)
        
    
    """
    Solution 1: Check n-1 edges + DFS for graph connectivity
    
    def validTree(self, n, edges):
        # write your code here
        
        if n == 0 or len(edges) != n - 1:
            return False
            
        neighbors = {x: [] for x in range(n)}
        
        for node_in, node_out in edges:
            neighbors[node_in].append(node_out)
            neighbors[node_out].append(node_in)
            
        visited = {}
        
        self.dfs(0, neighbors, visited)
        
        return len(visited) == n # visited all nodes
            
    def dfs(self, node, neighbors, visited):
        if node in visited:
            return
        
        visited[node] = True
        
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                self.dfs(neighbor, neighbors, visited)
                
        return 
    """
