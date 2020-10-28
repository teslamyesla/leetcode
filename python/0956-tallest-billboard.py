"""
Two solutions: DFS + memo or DP, both are a bit tricky and are hard to come up with!!

Solution 1: DFS + memo
Time Complexity: O(NS). The memo array of size N*S has been filled just once. Here, S refers to the range of sum (which is upper limit of range of delta) and N refers to the size of rods.
Space Complexity: O(NS)

Solution 2: DP
Time Complexity: O(NS), where N is the size of rods, and S is the sum of rods.
Space Complexity: O(NS). 

"""

class Solution:
    """
    Solution 2: DP
    
    Reference: https://github.com/daihui-lu/programmingPractice/blob/main/leetcode/956_tallestBillboard.py
    https://github.com/StevenSYT/leetcode_summary/blob/main/DP/956.tallest-billboard.py
    
    Key tricks:
    1. DP key is curr_sum (left bucket positie, right bucket negative), value is max of left_height
    2. for each rod, can add to left bucket: dp[curr_sum + rod], right bucket: dp[curr_sum - rod], or abandon: dp[curr_sum]
    3. dictionary cannot change size during iteration, thus need to use list(dp.items()) or create a new copy
    4. use dp.get(curr_sum + rod, 0) in the case of curr_sum + rod is not in dp, set max of left_height to be zero
    """
    
    def tallestBillboard(self, rods: List[int]) -> int: 
        dp = {0:0}
        
        for rod in rods:
            for curr_sum, left_height in list(dp.items()):
                dp[curr_sum + rod] = max(dp.get(curr_sum + rod, 0), left_height + rod)
                dp[curr_sum - rod] = max(dp.get(curr_sum - rod, 0), left_height)
                # dp[curr_sum] = max(dp.get(curr_sum, 0), left_height)
                
        return dp[0]
        
        
    """
    Solution 1: DFS + memo, reference: https://leetcode.com/problems/tallest-billboard/discuss/204160/C%2B%2B-16-ms-DFS-%2B-memo
        
    Key tricks:
    1. memo[(idx, sum1, sum2)] -> TLE, memo key is: memo[(idx, abs(sum1-sum2))]
    2. dfs(idx, sum1, sum2) returns the max height of supporting columns with rods[idx:] 
    3. memo[(idx, delta)] = gap means with rods[idx:] left to play with, and a current difference of delta between the two supports, we could even out the two supports by adding gap to the max support (or equivalently, adding gap+delta to min support)
    4. for example, when sum1=50, sum2=30, memo[(idx, abs(50-30))] = 150 means we could even out 50,30 -> 50+150 (dfs return value=200); samely, when sum1=100, sum2=80, we could also even out 100,80 -> 100+150 (dfs return value=250); 
    5. for same (idx, delta), memo value is the same, while dfs return value is different
    6. when invalid (cannot reach a valid status with two equal supports), memo needs to store -1 instead of 0! otherwise it will mix optimal (where gap=0) with invalid (where gap=-1)
        
    def tallestBillboard(self, rods: List[int]) -> int: 
        if not rods:
            return 0
        
        memo = {}
        return self.dfs(rods, 0, 0, 0, memo)
        
    def dfs(self, rods, idx, sum1, sum2, memo):
        if idx == len(rods):
            return sum1 if sum1 == sum2 else -1
        
        if (idx, abs(sum1-sum2)) not in memo:
            max_support = max(self.dfs(rods, idx+1, sum1+rods[idx], sum2, memo),
                              self.dfs(rods, idx+1, sum1, sum2+rods[idx], memo),
                              self.dfs(rods, idx+1, sum1, sum2, memo))
            if max_support == -1:
                memo[(idx, abs(sum1-sum2))] = -1
            else:
                memo[(idx, abs(sum1-sum2))] = max_support - max(sum1, sum2)
                
        if memo[(idx, abs(sum1-sum2))] != -1:
            return memo[(idx, abs(sum1-sum2))] + max(sum1, sum2)
        
        return -1
    """

        
