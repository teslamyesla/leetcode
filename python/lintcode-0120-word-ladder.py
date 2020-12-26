"""
Time Complexity: O(26*(M^2)×N), where M is the length of each word and N is the total number of words in the input word list.

N为dict中单词个数，26代表字符集大小，M为单词长度。因为bfs所有节点最多遍历一次(N)，每次遍历到之后，需要扫遍单词的每个字符(M)，每个字符均可以变化为其他25个不同字母(26)，同时set.contain()的平均复杂度一般是O(M)
所以总复杂度是 N*26*M*M

Space Complexity: O(M*N).
N为dict中单词个数，M为单词长度。用于bfs的队列最大需存下所有节点。

Complexity Reference: https://leetcode.com/problems/word-ladder/solution/
https://www.jiuzhang.com/problem/word-ladder/#tag-lang-python
https://www.1point3acres.com/bbs/thread-205253-1-1.html

"""

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end) # add end to dict due to problem description "start and end words do not need to appear in the dictionary"
        queue = [start]
        visited = set(start)
        
        dist = 0
        while queue:
            dist += 1 # 'a'->'c', return length of seq (which is 2) instead of length of trans (which is 1), thus ++
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == end:
                    return dist
                    
                next_nodes = self.getNextWord(node)
                for next_node in next_nodes:
                    if next_node in dict and next_node not in visited: # check whether next_node has been visited!
                        visited.add(next_node)
                        queue.append(next_node)
        return 0
        
    def getNextWord(self, word): 
        res = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz": # core part of the solution!
                if word[i] == char: # avoid self
                    continue
                res.append(left + char + right)
        return res
            
