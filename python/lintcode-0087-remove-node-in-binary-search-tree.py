"""
Divide and Conquer 分治解法：O(h) time, O(h) space, h: height of tree

1. 递归寻找value所在节点：若小于root，则递归左子树removeNode；若大于root，则递归右子树removeNode
2. 当root.value == value时，root即是需要被移除的节点，此时分三种情况移除:
   a. 当被移除节点既有left child, 又有right child时
      寻找left branch里的max (or right branch里的min)
      copy value to root
      removeNode in left branch (or right branch) recursively
   b. 当被移除节点只有left child (or只有right child)时
      root = root.left (or root = root.right)
   c. 当被移除节点没有子节点时
      root = None
     
Reference: https://www.jiuzhang.com/problem/remove-node-in-binary-search-tree/#tag-lang-python

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
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return None
            
        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right =  self.removeNode(root.right, value)
        else: # value == root.val
            # remove root
            if root.left and root.right:
                # has both left and right children
                # find max in left branch and copy to root, then removeNode(root.left, value)
                left_max = self.findLeftMax(root)
                root.val = left_max.val
                root.left = self.removeNode(root.left, left_max.val)
            elif root.left:
                # only has left
                root = root.left
            elif root.right:
                # only has right
                root = root.right
            else:
                root = None
                
        return root
                
    def findLeftMax(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root
