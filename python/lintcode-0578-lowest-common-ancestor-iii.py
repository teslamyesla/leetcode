"""
Time: O(n)
Space: O(n)

Reference: https://www.jiuzhang.com/problem/lowest-common-ancestor-iii/

和 88. LCA https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0088-lowest-common-ancestor-of-a-binary-tree.py主要区别在于
88题默认A, B nodes都存在在树里，而本题需要helper函数返回tuple (foundA, foundB, LCA)
foundA = left_foundA or right_foundA or root == A
foundB = left_foundB or right_foundB or root == B
LCA的更新规则和88题一致：
    a. if root == A or B: LCA是root
    b. if left_LCA and right_LCA: LCA是root
    c. if left_LCA only: LCA是left_LCA
    d. if right_LCA only: LCA是right_LCA
    e. otherwise: LCA是None

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        foundA, foundB, LCA = self.helper(root, A, B)
        if foundA and foundB:
            return LCA
        return None
        
    def helper(self, root, A, B):
        if root is None:
            return False, False, None
            
        left_foundA, left_foundB, left_LCA = self.helper(root.left, A, B)
        right_foundA, right_foundB, right_LCA = self.helper(root.right, A, B)
        
        foundA = left_foundA or right_foundA or root == A
        foundB = left_foundB or right_foundB or root == B
        
        if root == A or root == B:
            return foundA, foundB, root
        if left_LCA and right_LCA:
            return foundA, foundB, root
        if left_LCA:
            return left_foundA, left_foundB, left_LCA
        if right_LCA:
            return right_foundA, right_foundB, right_LCA
        return foundA, foundB, None
        
    
