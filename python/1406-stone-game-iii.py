""" 
Solution 1: Top Down DFS + memo
Time: O(n)
Space: O(n)

Solution 2: Bottom Up DP
Time: O(n)
Space: O(n)

Trick: dfs returns diff instead of absolute value of the first picker
"""

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        Solution 2: Bottom Up DP
        """
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0
        
        for i in range(n-1, -1, -1):
            taken = 0
            for j in range(1, 4):
                if i + j - 1 >= n:
                    break
                taken += stoneValue[i + j - 1]
                dp[i] = max(dp[i], taken - dp[i+j])
                
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
        
    """
    Solution 1: Top Down DFS + memo
    
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        res = self.dfs(stoneValue, 0, memo)
        
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        else:
            return 'Tie'
        
    def dfs(self, stoneValue, idx, memo):
        if idx in memo:
            return memo[idx]
        
        if idx == len(stoneValue):
            return 0
        
        res = float('-inf')
        taken = 0
        for i in range(1, 4):
            if idx + i - 1 >= len(stoneValue):
                break
            taken += stoneValue[idx + i - 1]
            res = max(res, taken - self.dfs(stoneValue, idx + i, memo))
        
        memo[idx] = res
        return memo[idx]
    """
            
            
