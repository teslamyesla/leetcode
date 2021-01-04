"""
Time: O(h)
Space: O(1) for Iterative, O(h) for Recurrsive
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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    
    """
    Solution 2: Iterative (Reference: https://www.lintcode.com/problem/closest-binary-search-tree-value/solution)
    """
    def closestValue(self, root, target):
        if root is None:
            return -1
        
        lower = root.val
        upper =  root.val
        
        while root:
            if target < root.val:
                upper = root.val
                root = root.left
            elif target > root.val:
                lower = root.val
                root = root.right
            else:
                return root.val
                
        if abs(lower - target) <= abs(upper - target):
            return lower
        else:
            return upper
    
    """
    Solution 1: Recurrsive (my original solution)
    
    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return -1
            
        res = root.val
        if target < root.val:
            res_left = self.closestValue(root.left, target)
            return res_left if abs(res_left - target) < abs(res - target) else res
        else:
            res_right = self.closestValue(root.right, target)
            return res_right if abs(res_right - target) < abs(res - target) else res
    """
