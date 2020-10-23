"""

Bottom up 1D DP
Time Complexity : O(m⋅n), where m is the subSetSum = total // 2, and n is the number of stones. 
Space Complexity: O(m), As we use an array of size m to store the result of subproblems.

Note:
1. Key trick is to transform problem to find target cloest to total // 2
2. Similiar as 416 (https://github.com/teslamyesla/leetcode/blob/master/python/416-partition-equal-subset-sum.py), but instead of true false, dp[i] stores max amount achievable that <= i

"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        x1 > x2, x1-x2 > x3, x1-x2-x3 > x4, ans = x1-x2-x3-x4
        x1 > x2, x3 > x1-x2, x4 > x3-(x1-x2), ans = x4+x1-(x3+x2)
        divide stones into two parts: S1 and S2, return min(S1-S2)
        total = S1+S2, return min(S1-S2) = min(total-2*S2)
        dp: find subset sum closest to total // 2 (<= total // 2)
        """
        total = sum(stones)
        target = total // 2 # transform problem to find target closest to total // 2
        
        dp = [0] * (target + 1) # dp[i] stores max amount achieveable that <= i
        
        for stone in stones:
            for i in range(target, stone - 1, -1):
                dp[i] = max(dp[i], dp[i-stone] + stone)
                
        return total - 2 * dp[target]
        
        
