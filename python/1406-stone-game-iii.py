""" 
Time: O(n)
Space: O(n)
"""

"""
Trick: dfs returns diff instead of absolute value of the first picker
"""

class Solution:
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
            
            
