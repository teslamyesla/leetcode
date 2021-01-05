"""
Time: O(n)
Space: O(h)

Note: how to connect & return value (return right_last or left_last or root) is the core part
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    """
    Solution: Divide and Conquer
    
    flatten_and_return_last_node函数 return 这个 tree 的最后一个点。
    """
    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)
        return root
        
    def flatten_and_return_last_node(self, root):
        if root is None:
            return None
            
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)
        
        # connect
        if left_last is not None:
            left_last.right = root.right
            root.left, root.right = None, root.left
            
        return right_last or left_last or root
    
