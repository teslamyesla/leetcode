"""
Time Complexity: O((M^2)×N), where M is the length of each word and N is the total number of words in the input word list.

For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. Since the length of each word is M and we have N words, the total number of iterations the algorithm takes to create all_combo_dict is M×N. Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to create the new string. This adds up to a complexity of O(M2×N).
Breadth first search in the worst case might go to each of the N words. For each word, we need to examine M possible intermediate words/combinations. Notice, we have used the substring operation to find each of the combination. Thus, M combinations take O(M^2) time. As a result, the time complexity of BFS traversal would also be O((M^2)×N).
Combining the above steps, the overall time complexity of this approach is O((M^2)×N).

Space Complexity: O(M*N).
N为dict中单词个数，M为单词长度。用于bfs的队列最大需存下所有节点。

Complexity Reference: https://leetcode.com/problems/word-ladder/solution/
https://www.jiuzhang.com/problem/word-ladder/#tag-lang-python

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
            
