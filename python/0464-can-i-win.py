"""

Time: O(N * 2^N)
Space: O(2^N)

How many allowed values sets are possible? The length of the allowed value set can range 1 to maxChoosableInteger(N). So the answer is (N,1) + (N,2) + ..(N,N) where (N,K) means choose K from N. This is equal to 2^N.
Now at my turn, if the max(allowed) + so_far >= target, then I will win. Otherwise, I choose from the allowed values one by one and recursively call for the other player. If with any choice the opponent fails for sure, then also I can win for sure from this state.
What is the time complexity? For a brute force solution, the game tree has 10 choices at first level, each of these choices has 9 choices at second level, and so on. So the complexity is N!. But with memoization, we only compute 2^N sub-problems, and in each problem we do O(N) work. So total time complexity is O(N2^N).

Reference: https://leetcode.com/problems/can-i-win/discuss/95319/Python-solution-with-detailed-explanation

"""

class Solution:
    """
    Reference: https://github.com/KOPFYF/LCEveryday/blob/master/canIWin464.py
    """
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        
        nums = [x for x in range(1, maxChoosableInteger + 1)]
        memo = {}
        return self.dfs(nums, desiredTotal, memo)
    
    def dfs(self, nums, desiredTotal, memo):
        if tuple(nums) in memo: # hash with tuple, faster than str()
            return memo[tuple(nums)]
        
        if not nums:
            return False
        
        if nums[-1] >= desiredTotal: # if max >= desiredTotal, we win
            return True
        
        # after we pick nums[i], next player loop all choices
        for i in range(len(nums)):
            if not self.dfs(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                # next player loses with nums[i] picked, we win
                memo[tuple(nums)] = True
                return True
            
        # next player wins all choices, we lose    
        memo[tuple(nums)] = False
        return False
                
        
        
        
    
        
        
