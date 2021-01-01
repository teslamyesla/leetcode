"""
Time Complexity: O(n)
Space Complexity : O(n) function Call Stack size
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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        return self.helper(root, float('inf'), float('-inf'))
    
    def helper(self, root, maxBound, minBound):
        if root is None:
            return True
            
        if root.val >= maxBound or root.val <= minBound:
            return False
            
        return self.helper(root.left, root.val, minBound) and \
                self.helper(root.right, maxBound, root.val)
    
    """
    Solution 2: Calculate max, min in helper
    
    def isValidBST(self, root):
        if root is None:
            return True
            
        maxLeft, minLeft = self.returnMaxMin(root.left)
        maxRight, minRight = self.returnMaxMin(root.right)
            
        return self.isValidBST(root.left) and self.isValidBST(root.right) and maxLeft < root.val and minRight > root.val
        
    def returnMaxMin(self, root):
        if root is None:
            return float('-inf'), float('inf')
        maxLeft, minLeft = self.returnMaxMin(root.left)
        maxRight, minRight = self.returnMaxMin(root.right)    
        return max(root.val, maxLeft, maxRight), min(root.val, minLeft, minRight)
    """
 
