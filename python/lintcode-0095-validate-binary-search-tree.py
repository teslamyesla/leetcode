"""
Time Complexity: O(n)
Space Complexity : O(n) function Call Stack size

Note:
Solution 1 uses maxBound, minBound, where both starts from infinity and left branch's maxBound becomes root.val and right branch's minBound becomes root.val.
           If at any time root.val >= maxBound or <= minBound, return False.
           Therefore in this solution, initialization is maxBound = float('inf') and minBound = float('-inf')
           
Solution 2 uses max, min calculation where if validLeft and validRight and maxLeft < root.val < minRight, the tree is a valid BST.
           Here returned max = max(maxLeft, root.val, maxRight) and min(minLeft, root.val, minRight)
           Therefore in this solution, initialization is reversed: max = float('-inf') and min = float('inf')

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
    """
    Solution 2: Calculate max, min in helper
    """
    def isValidBST(self, root):
        return self.helper(root)[0]
        
    def helper(self, root):
        if root is None:
            return True, float('-inf'), float('inf') 
            
        validLeft, maxLeft, minLeft = self.helper(root.left)
        validRight, maxRight, minRight = self.helper(root.right)
        
        return validLeft and validRight and maxLeft < root.val < minRight, \
               max(maxLeft, root.val, maxRight), \
               min(minLeft, root.val, minRight)
    
    """
    Solution 1: Use maxBound, minBound
    
    def isValidBST(self, root):
        return self.helper(root, float('inf'), float('-inf'))
    
    def helper(self, root, maxBound, minBound):
        if root is None:
            return True
            
        if root.val >= maxBound or root.val <= minBound:
            return False
        
        return self.helper(root.left, root.val, minBound) and self.helper(root.right, maxBound, root.val)
    """
        
        
