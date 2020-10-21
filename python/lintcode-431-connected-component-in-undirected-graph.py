"""

Solution 1: DFS
Time: O(V+E)
Space: O(V+E)

Solution 2: Union Find
Time: O(ElogE), faster implementation makes it O(E) (http://users.pja.edu.pl/~msyd/wyka-eng/mst.pdf)
Space: O(V)

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
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    """
    Solution 2: Union Find
    """
    def connectedSet(self, nodes):
        parents = {x: x for x in nodes}
        
        for node in nodes:
            for neighbor in node.neighbors:
                node_parent = self.find(node, parents)
                neighbor_parent = self.find(neighbor, parents)
                if node_parent != neighbor_parent:
                    parents[neighbor_parent] = node_parent
                    
        res = {}
        for node in parents:
            key = self.find(node, parents)
            if key not in res:
                res[key] = [node.label]
            else:
                res[key].append(node.label)
                
        return [sorted(res[key]) for key in res]
                
        
    def find(self, x, parents):
        if parents[x] == x:
            return x
            
        return self.find(parents[x], parents)
    
    
    """
    Solution 1: DFS
    
    def connectedSet(self, nodes):
        # write your code here
        visited = {}
        res = []
        
        for node in nodes:
            if node not in visited:
                path = []
                self.dfs(node, visited, path)
                res.append(sorted(path))
                
        return res
    
    def dfs(self, node, visited, path):
        if node in visited:
            return 
        
        visited[node] = True
        path.append(node.label)
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited, path)
                
        return
    """
        
        
    
