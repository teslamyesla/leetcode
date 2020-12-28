"""
Solution 1: Recurrsive

Time: O(n)
Space: O(h) for the call stack where h is the height of the tree

Solution 2: Iterative

Time: O(n)
Space: O(n) for storing nodes present in any level of binary tree. Worst case happens for a full binary tree, in which last level has n/2 nodes

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    """
    Iterative:
    """
    def invertBinaryTree(self, root):
        if root is None:
            return None
            
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            temp = node.left
            node.left = node.right
            node.right = temp
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return root
    
    """
    Recurrsive:
    
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return None
            
        new_left = self.invertBinaryTree(root.right)
        new_right = self.invertBinaryTree(root.left)
        
        root.left, root.right = new_left, new_right
        
        return root
    """
