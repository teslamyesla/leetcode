"""
DFS + Backtracking

Time Complexity : O(4^N) because we have a total of N sticks and for each one of those matchsticks, we have 4 different possibilities for the subsets they might belong to or the side of the square they might be a part of.
Space Complexity : O(N). For recursive solutions, the space complexity is the stack space occupied by all the recursive calls. The deepest recursive call here would be of size N and hence the space complexity is O(N). There is no additional space other than the recursion stack in this solution. 

"""

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        total = sum(nums)
        if total % 4 != 0:
            return False
        
        target = total // 4
        nums.sort(reverse=True)
        sums = [0] * 4
        
        return self.dfs(nums, sums, 0, target)
    
    def dfs(self, nums, sums, idx, target):
        if idx == len(nums):
            if sums[0] == sums[1] == sums[2] == target:
                return True
            else:
                return False
            
        for i in range(4):
            if sums[i] + nums[idx] > target:
                continue
            sums[i] += nums[idx]
            
            if self.dfs(nums, sums, idx + 1, target):
                return True
            sums[i] -= nums[idx]
            
        return False
