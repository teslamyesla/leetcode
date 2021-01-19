"""
Time：O(n ^ (target/min) ), （拷贝过程视作O(1)
), n为集合中数字个数，min为集合中最小的数字
每个位置可以取集合中的任意数字，最多有target/min个数字。

Space：O(n ^ (target/min) ), n为集合中数字个数，min为集合中最小的数字
对于用来保存答案的列表，最多有ntarget/min种组合

Reference:
youtube: https://www.youtube.com/watch?v=9lQnt4p7_nE
nine chapter: https://www.jiuzhang.com/problem/combination-sum/#tag-lang-ALL
discussion: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

Combination Sum与Subsets区别：
1. 有一个target的限制
2. 同一个元素可以取多次

"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, candidates, target, start, path, res):
        if target == 0:
            res.append(list(path))
            return
        
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue 
            
            path.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, path, res) # not i + 1 because we can reuse elements
            path.pop()

