"""
Time: O(h), where h is height of BST, in the worst case it's O(n)
Space: O(1) for iterative, O(h) for recurrsive

Reference: https://www.lintcode.com/problem/insert-node-in-a-binary-search-tree/solution
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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    
    """
    Solution 2: Iterative
    """
    def insertNode(self, root, node):
        if root is None:
            return node
            
        curr = root
        while curr:
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                    return root
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    return root
                else:
                    curr = curr.right
                    
        return root
        
    """
    Solution 1: Recurrsive
    
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node
            
        if node.val < root.val:
            if root.left is None:
                root.left = node
            else:
                self.insertNode(root.left, node)
        
        else:
            if root.right is None:
                root.right = node
            else:
                self.insertNode(root.right, node)
                
        return root
    """
