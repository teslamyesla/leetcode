"""
DFS + memo

Time complexity: O(l⋅n). The memo array of size l*n has been filled just once. Here, l refers to the range of sum and n refers to the size of nums array.
Space complexity: O(l⋅n). The depth of recursion tree can go upto n. The memo array contains l⋅n elements. 

"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        return self.dfs(nums, 0, S, memo)
        
    def dfs(self, nums, idx, target, memo):  
        if (target, idx) in memo:
            return memo[(target, idx)]
        
        if idx == len(nums):
            if target == 0:
                return 1
            else:
                return 0
        
        memo[(target, idx)] = self.dfs(nums, idx + 1, target - nums[idx], memo) +\
                              self.dfs(nums, idx + 1, target + nums[idx], memo)
        
        return memo[(target, idx)]
