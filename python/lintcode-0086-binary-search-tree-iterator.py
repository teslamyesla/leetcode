"""
Time: O(1)
Space: O(n)

访问所有节点用时O(n)，所以均摊下来访问每个节点的时间复杂度时O(1)

写法类似Binary Tree in-order-traversal iterative写法掰开来写：https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0067-binary-tree-inorder-traversal.py

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left
        
    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        node = self.stack.pop()
        root = node.right
        
        while root:
            self.stack.append(root)
            root = root.left
        
        return node
