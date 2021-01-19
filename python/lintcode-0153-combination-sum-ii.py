"""
Time complexity: O(k * 2^N), where k is the average length of each possible solution. Copying such a possible solution list takes O(k) time.
Space complexity: O(N), because of at most N-size recursion stack and N-size of when copying list

Difference with Combination Sum:
Each element can only be used once, thus self.dfs(num, target - num[i], i + 1, path, res)

"""

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        res = []
        num.sort()
        self.dfs(num, target, 0, [], res)
        return res
        
    def dfs(self, num, target, start, path, res):
        if target == 0:
            res.append(list(path))
            return
        
        if target < 0:
            return
        
        for i in range(start, len(num)):
            if i > start and num[i] == num[i-1]: # skip duplicates
                continue
            
            path.append(num[i])
            self.dfs(num, target - num[i], i + 1, path, res) # each element can only be used once
            path.pop()
