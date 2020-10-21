"""
Time complexity : O(S∗n), where S is amount, n is number of coins. On each step the algorithm finds the next F(i) in n iterations, therefore in total the iterations are S∗n.
Space complexity : O(S). We use extra space for the dp table.

Note: 
1. initialize dp with float('inf') instead of zeros, due to min problem
2. return dp[-1] if dp[-1] != float('inf'), else return -1

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # F(i) = min(F(i) - coin) + 1 for coin in coins
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1): # start from coin, otherwise dp[i-coin] have index out of range
                dp[i] = min(dp[i], dp[i-coin] + 1)
                
        return dp[-1] if dp[-1] != float('inf') else -1
