"""
Almost same as "Predict the Winner" problem: https://github.com/teslamyesla/leetcode/blob/master/python/0486-predict-the-winner.py

Solution 1: Top-Down DFS + memo

Time: O(n^2)
Space: O(n^2)

Solution 2: Bottom-Up DP

Time: O(n^2)
Space: O(n^2)

"""

class Solution:
    """
    Solution 2: Bottom-Up DP
    """
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        # dp[i][j]: max(Alex - Lee) for pile i to pile j
        dp = [[float('-inf')] * n for _ in range(n) ]
        
        for i in range(n):
            dp[i][i] = piles[i]
            
        for j in range(n):
            for i in range(j - 1, -1, -1):
                dp[i][j] = max(dp[i][j], piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
                
        return dp[0][n-1] > 0
        
    """
    Solution 1: Top-Down DFS + memo
    
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        return self.dfs(piles, 0, len(piles) - 1, memo) > 0
    
    def dfs(self, piles, start, end, memo):
        if start == end: # no choice but pick piles[start]
            return piles[start]
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        memo[(start, end)] = max(piles[start] - self.dfs(piles, start + 1, end, memo),
                                 piles[end] - self.dfs(piles, start, end - 1, memo))
        
        return memo[(start, end)]
    """

    
    
