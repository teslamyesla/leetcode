"""
Leetcode: 269 (Premium): https://leetcode.com/problems/alien-dictionary/

3 Steps:
1. construct neighbors and indegree from char in word, word in words
2. check relationship, update eighbors and indegree, two substeps:
   1) for chars in words[i], words[i+1], if words[i][j] != words[i+1][j] -> means char at words[i][j] is a pre of chat at words[i+1][j]
   2) corner case: when "abc" is pre of "ab", invalid -> return empty string
3. topology sort, if res contains all chars, res is valid. a trick:
   Trick: as we should return the topology order with lexicographical order when there are multiple valid order of letters, we should use PriorityQueue instead of a FIFO Queue!
   Example: ['zy', 'zx'] -> return 'yxz' instead of 'zyx'
   
Time: O(V + E) = O(n * k + n * k) = O(n * k), where n: number of words, k: avg word length
Space: O(V + E) = O(n * k + n * k) = O(n * k), where n: number of words, k: avg word length
   
"""

import heapq

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        neighbors = {}
        indegree = {}
        
        # construct neighbors and indegree with default: [] and 0
        for word in words:
            for char in word:
                if char not in neighbors:
                    neighbors[char] = []
                    indegree[char] = 0
                    
        # check relationship, update neighbors and indegree
        for i in range(len(words)-1):
            if words[i+1] in words[i] and words[i+1][0] == words[i][0]: # corner case of "abc" is pre of "ab" ("ab" in "abc" and starts with the same letter) -> invalid, return empty
                return ""
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]: # words[i][j] is pre of words[i+1][j]
                    neighbors[words[i][j]].append(words[i+1][j])
                    indegree[words[i+1][j]] += 1
                    break
        
        # topology sort, note: as we should return the topo order with lexicographical order when there are multiple valid order of letters, we should use PriorityQueue instead of a FIFO Queue!
        heap = []
        for char in indegree:
            if indegree[char] == 0:
                heapq.heappush(heap, char)
        
        res = []  
        while heap:
            char = heapq.heappop(heap)
            res.append(char)
            for neighbor in neighbors[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)
                    
        if len(res) != len(indegree):
            return ""
        else:
            return "".join(res)
            
            
"""
Revisited this problem on Dec 21, solution:

import heapq

class Solution:
    def alienOrder(self, words):
        # Write your code here
        char_set = set()
        for word in words:
            for char in word:
                char_set.add(char)
                
        indegree = {x: 0 for x in char_set}
        neighbors = {x: set() for x in char_set}
        
        for i in range(1, len(words)):
            for j in range(min(len(words[i-1]), len(words[i]))):
                if words[i-1][j] != words[i][j]:
                    neighbors[words[i-1][j]].add(words[i][j])
                    break
            if words[i] in words[i-1]: # invalid dictionary, to handle corner case of ["abc", "ab"] 
                return ""
                
        for node in neighbors:
            for neighbor in neighbors[node]:
                indegree[neighbor] += 1
                
        heap = [] # maintain an priority queue, always by lexicographical order
        for node in neighbors:
            if indegree[node] == 0:
                heapq.heappush(heap, node)
         
        # topology sort   
        res = []
        while heap:
            node = heapq.heappop(heap)
            res.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)
                    
        return "".join(res) if len(res) == len(indegree) else ""   
        
"""
