"""
Time:
Space: 

Notes:
1. Use topology sort, with subtle difference
2. Check unique_nodes == set(org) to handle corner cases: a) [1], []  b) [1,2,3,4,5], [[1,2,3,4,5], [10000]]
3. Dependency relationship comes with multiple nodes instead of two nodes (node_in, node_out), thus use neighbors[seq[i-1]].add(seq[i]) to update
4. Use set() to record neighbors, instead of [], to avoid duplicates in dependency: e.g., [[1,2,3], [2,3,4]], neighbors[2] = 3, not [3,3]
5. Same reason as above, update indegree after fully update neighbors, to avoid duplicate counting: e.g. [[2,3], [2,3,4]], indegree[3] = 1, not 2
6. Make sure there's always only 1 element in the queue, due to uniqueness requirement of topology sort: if len(queue) > 1: return False

"""

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        unique_nodes = set()
        for seq in seqs:
            for x in seq:
                unique_nodes.add(x)
                
        if set(org) != unique_nodes:
            return False
        
        indegree = {x: 0 for x in org}
        neighbors = {x: set() for x in org}
        
        for seq in seqs:
            for i in range(1, len(seq)):
                neighbors[seq[i-1]].add(seq[i])
        
        for node in neighbors:
            for neighbor in neighbors[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
                
        res = [] 
        while queue:
            if len(queue) > 1: # one unique element at a time
                return False 
            node = queue.pop(0)
            res.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res == org
            
        
                
        
        
            

            
        
