"""
Solution 1: Recurrsive
Time complexity : O(n). The time complexity is O(n) because the recursive function is T(n)=2⋅T(n/2)+1T(n) = 2⋅T(n/2)+1T(n)=2⋅T(n/2)+1
Space complexity : The worst case space required is O(n), and in the average case it's O(log⁡n) where n is number of nodes

Solution 2: Iterative
Time complexity : O(n)
Space complexity : O(n)

Note: The iterative solution using stack is important, to be memorized!!!

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
