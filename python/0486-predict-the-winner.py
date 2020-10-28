"""
DFS + memo:

memo[(start, end)] tracks max delta given (start, end) position, you can think of it as the absolute max positive delta regardless of the players picking order!!

1) when a player picks start: then the other player will pick in range (start+1, end) to get the max delta, which to the current player results in delta = nums[start] - dfs(start+1, end)
2) when a player picks end: then the other player will pick in range(start, end-1) to get the max delta, which to the current player results in delta = nums[end] - dfs(start, end-1)

Time complexity : O(n^2). The entire memo array of size nxn is filled only once. Here, n refers to the size of nums array.
Space complexity : O(n^2). memo array of size nxn is used for memoization.

"""

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, memo) >= 0
        
    def dfs(self, nums, start, end, memo):
        if start == end: # no choice but nums[start]
            return nums[start]
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        memo[(start, end)] = max(nums[start] - self.dfs(nums, start + 1, end, memo),
                                 nums[end] - self.dfs(nums, start, end - 1, memo))
        
        return memo[(start, end)]
        
        
    
