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
