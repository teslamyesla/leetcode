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
            
