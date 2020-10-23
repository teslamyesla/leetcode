"""
Time complexity : O(S*n), where S is amount, n is number of coins. On each step the algorithm finds the next F(i) in n iterations, therefore in total the iterations are S*n.
Space complexity : O(S). We use extra space for the dp table.
Note: 
1. dp[i] = dp[i] + dp[i-coin] for coin in coins
2. if i == coin, dp[i] = dp[i] + 1
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # corner cases
        if amount == 0: # if no amount, 1 way to make that is use no coin
            return 1
        if not coins: # if no coins, no way to make any amount
            return 0
        
        # F(i) = sum of F(i-coin) for coin in coins
        dp = [0] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                if i == coin:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-coin]
                
        return dp[-1]

    
    
