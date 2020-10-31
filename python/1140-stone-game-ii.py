"""
Time: O(n^3), similiar as https://github.com/teslamyesla/leetcode/blob/master/python/0375-guess-number-higher-or-lower-ii.py
Space: O(n^2), memo size n * M, where M is bounded by n, thus n^2

关于dp时间复杂度：dp[(i,M)]自问题从小到达过一遍，至少是n^2复杂度，但n^2还是n^3主要区别在于更新dp[(i,j)]时是只基于某几个dp[(i-1, j)], dp[(i, j-1)]的子问题，还是基于
dp[(i-1, j)], dp[(i-2, j)], ...等几乎之前所有的子问题。例如，https://github.com/teslamyesla/leetcode/blob/master/python/0486-predict-the-winner.py 这种两端取问题，
只能取首尾，就是n^2；https://github.com/teslamyesla/leetcode/blob/master/python/0375-guess-number-higher-or-lower-ii.py 这种中间都能取的问题，就是n^3。
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
        
        
