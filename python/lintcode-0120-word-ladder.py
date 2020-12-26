"""
Time Complexity: O((M^2)×N), where M is the length of each word and N is the total number of words in the input word list.

For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. Since the length of each word is M and we have N words, the total number of iterations the algorithm takes to create all_combo_dict is M×N. Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to create the new string. This adds up to a complexity of O(M2×N).
Breadth first search in the worst case might go to each of the N words. For each word, we need to examine M possible intermediate words/combinations. Notice, we have used the substring operation to find each of the combination. Thus, M combinations take O(M^2) time. As a result, the time complexity of BFS traversal would also be O((M^2)×N).
Combining the above steps, the overall time complexity of this approach is O((M^2)×N).

Space Complexity: O((M^2)×N).

Each word in the word list would have M intermediate combinations. To create the all_combo_dict dictionary we save an intermediate word as the key and its corresponding original words as the value. Note, for each of M intermediate words we save the original word of length M. This simply means, for every word we would need a space of M^2 to save all the transformations corresponding to it. Thus, all_combo_dict would need a total space of O((M^2)×N).
Visited dictionary would need a space of O(M×N) as each word is of length M.
Queue for BFS in worst case would need a space for all O(N) words and this would also result in a space complexity of O(M×N).
Combining the above steps, the overall space complexity is O((M^2)×N) + O(M∗N) + O(M∗N) = O((M^2)×N) space.

Complexity Reference: https://leetcode.com/problems/word-ladder/solution/

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
        dict.add(end)
        queue = [start]
        visited = set(start)
        
        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == end:
                    return dist
                    
                next_nodes = self.getNextWord(node)
                for next_node in next_nodes:
                    if next_node in dict and next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)
        return 0
        
    def getNextWord(self, word):
        res = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                res.append(left + char + right)
        return res
            
