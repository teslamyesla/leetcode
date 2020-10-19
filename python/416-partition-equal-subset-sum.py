class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        memo = {}
        return self.dfs(nums, target, len(nums) - 1, memo)
    
    def dfs(self, nums, target, idx, memo):
        if (target, idx) in memo:
            return memo[(target, idx)]
        
        if target == 0:
            # memo[(target, idx)] = True
            return True
        
        if target < 0 or idx < 0:
            # memo[(target, idx)] = False
            return False
             
        result = self.dfs(nums, target, idx - 1, memo) or \
                 self.dfs(nums, target - nums[idx], idx - 1, memo)
        memo[(target, idx)] = result
        
        return result
