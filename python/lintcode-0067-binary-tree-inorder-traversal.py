"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    
    """
    Solution 2: Iterative
    Reference: https://blog.csdn.net/yangjingjing9/article/details/77054899
    """
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else: # reach left None, pop from stack
                peak = stack.pop()
                res.append(peak.val)
                root = peak.right
        return res
                
    """
    Solution 1: Recurrsive
    
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
            
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    """
