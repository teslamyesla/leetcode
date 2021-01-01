"""
Time: O(n)
Space: O(n)

Note:
The idea is to traverse the tree starting from the root. If any of the given keys (n1 and n2) matches with the root, 
then the root is LCA (assuming that both keys are present, this assumption is very important, see example below!). 
If the root doesn’t match with any of the keys, we recur for the left and right subtree. 
The node which has one key present in its left subtree and the other key present in the right subtree is the LCA. 
If both keys lie in the left subtree, then the left subtree has LCA, otherwise, LCA lies in the right subtree.  

How could LCA exist in both root.left and root.right when root is the LCA? To understand the return value of LCA, let's look at one simple example

Example:

    root
   /    \
  A      B
  
After checking the corner case, we need to divide and conquer to check self.lowestCommonAncestor(root.left, A, B) and self.lowestCommonAncestor(root.right, A, B),
which are self.lowestCommonAncestor(A, A, B) and self.lowestCommonAncestor(B, A, B). Here, we can see the assumption of assuming both keys are present is important,
where in the base case it no longer hold (B is out of presence of the tree in the case of (A,A,B))! Thus the meaning of LCA return value is more of the root where
we can find at least one node. That's why we could have LCA return value both exists in root.left branch as well as root.right branch, and we need to check that to 
determine what's the final LCA.

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
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        """
        递归查找A和B， 找到A和B第一次在同一棵子树中的子树根节点即是LCA: https://www.jiuzhang.com/problem/lowest-common-ancestor-of-a-binary-tree/#tag-lang-ALL
        """
        if root is None:
            return None
        if root == A or root == B: # If either n1 or n2 matches with root's key, report the presence of at least one node by returning root
            return root
        
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
