"""
Time: O(2^N) 
Space: O(N) for path and dfs stack (ignore space to save res)

Reference: 
https://leetcode.com/problems/subsets/solution/
https://www.jiuzhang.com/problem/subsets/
https://www.lintcode.com/problem/subsets/solution

3 Solutions youtube: https://www.youtube.com/watch?v=MsHFNGltIxw
Discussion solution: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
"""

class Solution:  
    """
    Solution 3: DFS backtracking - enumerate numbers for a position, add all paths during the process to res
    Time: O(2^N) 
    Space: O(N) for path and dfs stack (ignore space to save res)
    """
    def subsets(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, path, res):
        res.append(list(path))  # path array keep changing! append path[:] or list(path) instead!
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()
    
    """
    Solution 2: DFS backtracking - choose or not choose, only add the leaf path to res
    Time: O(2^N) 
    Space: O(N) for path and dfs stack (ignore space to save res)
    
    def subsets(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, idx, subset, res):
        if idx == len(nums):
            res.append(subset[:]) # subset array keep changing! append subset[:] instead!
            return res
        
        # pick nums[idx]
        subset.append(nums[idx])
        self.dfs(nums, idx + 1, subset, res)
        # not pick nums[idx]
        subset.pop()
        self.dfs(nums, idx + 1, subset, res)
    """
    
    """
    Solution 1: Iterative
    Time: O(2^N) 
    Space: O(N) 
    
    def subsets(self, nums):
        output = [[]]
        nums.sort()
        
        for num in nums:
            output += [curr + [num]for curr in output]
            
        return output
    """
