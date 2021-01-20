"""
Time: O(n!)
Space: O(n) (ignore res)

Reference: 
https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
https://www.lintcode.com/problem/permutations-ii/solution

和没有重复元素的 Permutation 一题相比，只加了两句话：
1. Arrays.sort(nums) // 排序这样所有重复的数
2. if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) { continue; } // 跳过会造成重复的情况

"""

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        res = []
        nums.sort()
        used = [False for _ in nums]
        self.dfs(nums, [], res, used)
        return res
        
    def dfs(self, nums, path, res, used):
        if len(path) == len(nums):
            res.append(list(path))
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            path.append(nums[i])
            used[i] = True
            self.dfs(nums, path, res, used)
            path.pop()
            used[i] = False
