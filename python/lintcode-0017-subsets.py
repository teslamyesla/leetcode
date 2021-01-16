"""
Time: O(N * 2^N) to generate all subsets and then copy them into output list
Space: O(N * 2^N) to keep all the subsets of length N, since each of N elements could be present or absent. 

Reference: 
https://leetcode.com/problems/subsets/solution/
https://www.jiuzhang.com/problem/subsets/
https://www.lintcode.com/problem/subsets/solution
"""
        
class Solution:        
    """
    Solution 2: DFS backtracking
    Time: O(N * 2^N) to generate all subsets and then copy them into output list
    Space: O(N * 2^N) to keep all the subsets of length N, since each of N elements could be present or absent. 
    """
    def subsets(self, nums):
        nums.sort()
        res = []
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
    Solution 1: Iterative (Bottom Up DP)
    Time: O(N * 2^N) to generate all subsets and then copy them into output list
    Space: O(N * 2^N). This is exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.
    
    def subsets(self, nums):
        nums.sort()
        output = [[]]
        
        for num in nums:
            output += [curr + [num]for curr in output]
            
        return output
    """
        
