"""
Time: O(2^N) 
Space: O(N) for path and dfs stack (ignore space to save res)

Reference:
3 Solutions youtube: https://www.youtube.com/watch?v=0ElTC4XiDvc

有重复数字，需要：
1. sort
2. 每个重复数字只第一个进loop的时候加一次，否则会12(1), 12(2)
"""
class Solution:
    """
    Solution 2: DFS backtracking - choose or not choose, only add the leaf path to res
    """
    def subsetsWithDup(self, nums):
        res = []
        nums.sort() # put same numbers together
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, path, res):
        if start == len(nums):
            res.append(list(path))
            return
        
        path.append(nums[start])
        self.dfs(nums, start + 1, path, res)
        path.pop()
        
        if len(path) > 0 and path[-1] == nums[start]:
            return
        self.dfs(nums, start + 1, path, res)     
    
    """
    Solution 1: DFS backtracking - enumerate numbers for a position, add all paths during the process to res
    Time: O(2^N)
    Space: O(N)
    
    def subsetsWithDup(self, nums):
        res = []
        nums.sort() # put same numbers together
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, start, path, res):
        res.append(list(path))
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: # skip the same number at a certain depth
                continue
                
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()
    """
            
            
