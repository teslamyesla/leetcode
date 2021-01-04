"""
Time: O(n)
Space: O(n)

Note:
我们在中序遍历的过程中将在数值范围内的值按序加入到数组中，就能得到最终的结果

二叉树中序遍历：
    如果当前节点为空，直接返回。
    先遍历左节点。
    判断当前节点的值是否在范围内，如果是，加入结果数组中。
    再遍历右节点。
    
Reference:
https://www.jiuzhang.com/problem/search-range-in-binary-search-tree/#tag-lang-python

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    
    """
    Solution 2: Iterative
    """
    def searchRange(self, root, k1, k2):
        if root is None:
            return []
            
        stack = []
        res = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else: # reach leftmost None, pop from stack
                peak = stack.pop()
                if k1 <= peak.val <= k2:
                    res.append(peak.val)
                if peak.val > k2:
                    break
                root = peak.right
                
        return res
    
    """
    Solution 1: Recurrsive
    
    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        self.helper(root, k1, k2, res)
        return res
        
    def helper(self, root, k1, k2, res):
        if root is None:
            return res
        
        # 剪枝，如果当前节点小于等于k1，不必访问左子树
        if root.val > k1:
            self.helper(root.left, k1, k2, res)
            
        if k1 <= root.val <= k2:
            res.append(root.val)
            
        # 剪枝，如果当前节点大于等于k2，不必访问右子树
        if root.val < k2:
            self.helper(root.right, k1, k2, res)
            
        return res
    """
