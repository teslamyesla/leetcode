"""
Time: O(n^2), memo of size n * M filled once, where M is bounded by n, thus n^2
Space: O(n^2), memo size n * M, where M is bounded by n, thus n^2
"""

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        return self.dfs(piles, 0, 1, memo)
    
    def dfs(self, piles, idx, M, memo): # memo records future sum of Alex starting from idx
        if (idx, M) in memo:
            return memo[(idx, M)]
        
        if idx == len(piles):
            return 0
        
        if idx + 2*M >= len(piles): # take all the rest, no need to leave them to Lee
            return sum(piles[idx:])
        
        # Alex can take from x = 1~2M piles
        max_res = 0
        for x in range(1, 2*M + 1):
            oppo_sum = self.dfs(piles, idx+x, max(M,x), memo)
            res = sum(piles[idx+x:]) - oppo_sum + sum(piles[idx:idx+x])
            max_res = max(max_res, res)
        
        memo[(idx, M)] = max_res
        return max_res
        
        
