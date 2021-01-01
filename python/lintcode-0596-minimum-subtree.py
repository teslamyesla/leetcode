"""
Similiar as https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0597-subtree-with-maximum-average.py

Time: O(n)
Space: O(n)

Object attributes can also be set as jiuzhang solution directly within method: https://www.lintcode.com/problem/minimum-subtree/solution

def findSubtree(self, root):
    self.min_sum = float('inf')
    self.min_sum_node = None
    self.helper(root)
    return self.min_sum_node
 
def helper(self, root):
    ....

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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.min_sum = 0
        self.min_sum_node = None
        
    def findSubtree(self, root):
        if root is None:
            return None
            
        self.helper(root)
        return self.min_sum_node
        
    def helper(self, root):
        if root is None:
            return 0
            
        sum_left = self.helper(root.left)
        sum_right = self.helper(root.right)
        sum_all = sum_left + sum_right + root.val
        
        if self.min_sum_node is None or sum_all < self.min_sum:
            self.min_sum = sum_all
            self.min_sum_node = root
            
        return sum_all
