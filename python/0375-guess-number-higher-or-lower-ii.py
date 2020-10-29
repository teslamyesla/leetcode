"""
Solution 1: DFS + memo

Time: O(n^2)
Space: O(n^2)

Solution 2: Bottom up DP

Time: O(n^2)
Space: O(n^2)

"""

class Solution:
    """
    Solution 2: DP
    
    Reference: https://github.com/niufenjujuexianhua/Leetcode/blob/master/%5B375%5DGuess%20Number%20Higher%20or%20Lower%20II.py
    另一种写法是循环len和start, 都是从头到尾循环，从len = 2开始，算完所有start，再算len = 3的所有start，也是同理。切记：bottom up dp的顺序要遵循推演顺序：从短的子数组推演到长的子数组。
    
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf')] * (n + 1) for _ in range(n + 1) ]
        
        for j in range(1, n + 1): # j: end, from 1 ~ n
            for i in range(j, 0, -1): # i: start, from j ~ 1
            # trick: 此处倒序！！倒序因为[1,j]包含了[2,j], ..., [j-1,j], i.e., 要够猜中[1,j]中的任何number, 必须够猜中[2,j]...[j-1,j]中的任何number，若在更新dp[j-1, j]段落前就更新dp[1, j]，取到的dp[j-1, j]的值还未更新，还是inf
                if i == j:
                    dp[i][j] = 0
                elif i + 1 == j:
                    dp[i][j] = i
                else:
                    for x in range(i + 1, j): # do not include i or j, to prevent index out of range!
                        dp[i][j] = min(dp[i][j], max(dp[i][x-1], dp[x+1][j]) + x)
                        
        return dp[1][n]
    """
    
    """
    Solution 1: DFS + memo
    
    数字：1 2 3 4 。。。。。n, 要么是小于要么是大于，分两种情况看:
    假设任意猜的数为x，需要付的钱：x + max(helper(i,x-1),helper(x+1,j))

    Reference: https://github.com/panxuan101/package/blob/main/leetcode/375.%20Guess%20Number%20Higher%20or%20Lower%20II
    """
    def getMoneyAmount(self, n: int) -> int:
        
        memo = {}
        return self.dfs(1, n, memo)
        
    def dfs(self, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
        
        if start >= end: # here handles out of range situations!
            return 0
        
        res = float('inf')
        for x in range(start, end + 1): # here picking x, x could be start or end, thus inclusive!
            res = min(res, max(self.dfs(start, x-1, memo), self.dfs(x+1, end, memo)) + x)
        
        memo[(start, end)] = res
        return memo[(start, end)]
