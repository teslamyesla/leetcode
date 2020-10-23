"""
Solution 1: Bottom up 1D DP
Time Complexity : O(m⋅n), where m is the subSetSum, and n is the number of array elements. The time complexity is the same as using 2D DP.
Space Complexity: O(m), As we use an array of size m to store the result of subproblems.

Solution 2: DFS + memo 
Time Complexity : worst case O(2^n), where n is the number of array elements. The calculated subSetSum maybe always unique, where the worst-case time complexity would be the same as the non-memoized version in brute force (The recursive solution takes the form of a binary tree where there are 2 possibilities for every array element and the maximum depth of the tree could be n). However, for normal case, the time complexity should be same as bottom up DP.
Space Complexity: O(m⋅n), where n is the number of array elements and mmm is the subSetSum. We are using a 2 dimensional array memo of size (m⋅n)and O(n) space to store the recursive call stack. This gives us the space complexity as O(n)+ O(m⋅n)

Solution 3: DFS + memo, 和473. Matchsticks to Square统一写法

此题关键在于 1）先转化为subset sum = sum // 2问题 
           2）类coin change DP，但每个元素只能取一次
           
Trick: base case memo could be skipped，直接return，原因在于：base case其实也会有被多个分支重复call的情况，但因为计算起来太简单，和查memo其实差不多了，所以memo与否就不重要了
"""

class Solution:
    """
    Solution 1: Bottom up 1D DP
    """
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1) 
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1): # 每个元素只能取一次因此是逆序
                dp[i] = dp[i] or dp[i-num] 
                
        return dp[target]
        
    """
    Solution 2: DFS + memo
    
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
            memo[(target, idx)] = True
            return True
        
        if target < 0 or idx < 0:
            memo[(target, idx)] = False
            return False
        
        result = self.dfs(nums, target - nums[idx], idx - 1, memo) or \
                 self.dfs(nums, target, idx - 1, memo)
        memo[(target, idx)] = result
        
        return result
    """

    """
    Solution 3: DFS + memo, directly use 473. Matchsticks to Square's method
    
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        nums.sort(reverse=True)
        sums = [0] * 2
        memo = {}
        
        return self.dfs(nums, sums, 0, target, memo)
    
    def dfs(self, nums, sums, idx, target, memo):
        if idx == len(nums):
            if sums[0] == target:
                return True
            else:
                return False
            
        if (idx, tuple(sorted(sums))) in memo:
            return memo[(idx, tuple(sorted(sums)))]
            
        for i in range(2):
            if sums[i] + nums[idx] > target:
                continue
            sums[i] += nums[idx]
            
            if self.dfs(nums, sums, idx + 1, target, memo):
                memo[(idx, tuple(sorted(sums)))] = True
                return True
            sums[i] -= nums[idx]
        
        memo[(idx, tuple(sorted(sums)))] = False
        return False
    """

