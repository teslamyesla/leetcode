"""
Time: O(C(N, K))
Space: O(N * K)

复杂度分析: 设待选的最大的数为N，要选的数为K。C(N, K)代表N个数中挑选出K个不同数的组合数个数。

时间复杂度

    N层的满二叉树的状态共2^N个，未剪枝的情况下时间复杂度为O(2^N)。
    剪枝后可以减少大量的搜索节点，时间复杂度可达到O(C(N, K))。

空间复杂度

    递归的空间复杂度取决于搜索树的最大深度，最大深度为N，空间复杂度为O(N * K)。
"""

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        res = []
        nums = [i for i in range(1, n + 1)]
        self.dfs(nums, k, 0, [], res)
        return res
    
    def dfs(self, nums, k, start, path, res):
        if k == 0:
            res.append(list(path))
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, k - 1, i + 1, path, res)
            path.pop()
            
            
            
