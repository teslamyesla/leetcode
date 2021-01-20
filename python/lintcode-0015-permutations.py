"""
Time: O(n!)
Space: O(n) (ignore res)

Reference: 
https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
https://www.youtube.com/watch?v=8t7bIHIr9JY
"""

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res): # no "start" parameter
        if len(path) == len(nums):
            res.append(list(path))
            return
        
        for i in range(0, len(nums)): # (0, len(nums)) instead of (start, len(nums))
            if nums[i] in path:
                continue
            
            path.append(nums[i])
            self.dfs(nums, path, res)
            path.pop()
                
        
        
