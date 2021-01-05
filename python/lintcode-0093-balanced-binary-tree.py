"""
Time: O(n)
Space: O(h)
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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.isBalanced_height(root)[0]
        
    def isBalanced_height(self, root):
        if root is None:
            return True, 0
            
        left_balanced, left_height = self.isBalanced_height(root.left)
        right_balanced, right_height = self.isBalanced_height(root.right)
        
        if left_balanced and right_balanced and abs(left_height - right_height) <= 1:
            return True, max(left_height, right_height) + 1
        else:    
            return False, max(left_height, right_height) + 1
