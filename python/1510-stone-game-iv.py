"""
Time complexity: O(N\sqrt{N})since we spend O(\sqrt{N}) at most for each dfs call, and there are O(N) dfs calls in total.
Space complexity: O(N) since we need spaces of O(N) to store the result of dfs.

Notes:
1. math.sqrt(n), equal with n ** 0.5
2. int round to lower end, int(0.9) = 0

"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        return self.dfs(n, memo)
        
    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        
        if n == 0:
            return False
        
        sqrt = int(math.sqrt(n)) # math.sqrt(49) = 7
        # sqrt = int(n ** 0.5) # int round to lower end, int(0.9) = 0
        
        for i in range(1, sqrt + 1):
            if not self.dfs(n - i*i, memo):
                memo[n] = True
                return True
        
        memo[n] = False 
        return False
    
    
    
