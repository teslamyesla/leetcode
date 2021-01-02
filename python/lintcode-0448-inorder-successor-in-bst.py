"""
Solution 1: In order traversal of tree
Time: O(n)
Space: O(n)



首先要确定中序遍历的后继:

    如果该节点有右子节点, 那么后继是其右子节点的子树中最左端的节点
    如果该节点没有右子节点, 那么后继是离它最近的祖先, 该节点在这个祖先的左子树内.

使用递归实现:

    如果根节点小于或等于要查找的节点, 直接进入右子树递归
    如果根节点大于要查找的节点, 则暂存左子树递归查找的结果, 如果是 null, 则直接返回当前根节点; 反之返回左子树递归查找的结果.

使用循环实现:

    查找该节点, 并在该过程中维护上述性质的祖先节点
    查找到后, 如果该节点有右子节点, 则后继在其右子树内; 否则后继就是维护的那个祖先节点

在递归实现中, 暂存左子树递归查找的结果就相当于循环实现中维护的祖先节点.

Reference: https://www.lintcode.com/problem/inorder-successor-in-bst/discuss
https://www.lintcode.com/problem/inorder-successor-in-bst/solution

"""

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    
    """
    Solution 3: Iterative O(h) solution.
    """
    def inorderSuccessor(self, root, p):
        if root is None:
            return None
        
        # find p
        successor = None
        while root is not None and root != p:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        # if p does not have right branch, directly return successor 
        if root.right is None: 
            return successor
            
        # else, successor is the leftmost node of right branch
        root = root.right
        while root.left:
            root = root.left
            
        return root
        
    """
    Solution 2: Recursive O(h) solution.
    
    def inorderSuccessor(self, root, p):
        if root is None:
            return None
            
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
            
        leftSuccessor = self.inorderSuccessor(root.left, p)
        return root if leftSuccessor is None else leftSuccessor
    """
        
    """
    Solution 1: Brute-force solution: O(n). The most straight-forward solution is to do a in-order traversal of the BST.
    
    def inorderSuccessor(self, root, p):
        # write your code here
        if root is None:
            return None
            
        stack = []
        prev = None
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else: # reach leftmost None, pop from stack
                peak = stack.pop()
                if prev == p:
                    return peak
                prev = peak
                root = peak.right
                
        return None
    """
            
