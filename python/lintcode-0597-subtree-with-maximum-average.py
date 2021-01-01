"""
Time: O(n)
Space: O(n)

空间复杂度：每个节点记录一个sum和num，空间复杂度O(n)。
时间复杂度：每个节点递归访问一次，时间复杂度为O(n)。

Reference: https://www.jiuzhang.com/problem/subtree-with-maximum-average/#tag-lang-python

Note:
1. __init__ part can be replaced with curr_max_avg = 0, curr_max_avg_node = None, when referring to the variable, still use self.var_name, see detail in code comment
2. An easy mistake is to initialize curr_max_avg_node with root, but this could be very wrong when root.val is far smaller than the real avg and no branch can beat this default value!
Thus the correct way is to initialize curr_max_avg = 0 and set curr_max_avg_node to None!

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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.curr_max_avg = 0
        self.curr_max_avg_node = None
        
    """
    # __init__ part can be replaced as below two lines:
    curr_max_avg = 0
    curr_max_avg_node = None
    """
    
    def findSubtree2(self, root):
        # write your code here
        if root is None:
            return root
        
        self.helper(root)
        return self.curr_max_avg_node
        
    def helper(self, root):
        if root is None:
            return 0, 0
        
        sum_left, num_left = self.helper(root.left)
        sum_right, num_right = self.helper(root.right)
        
        sum_all = sum_left + root.val + sum_right
        num_all = num_left + num_right + 1
        
        if self.curr_max_avg_node is None or sum_all / num_all > self.curr_max_avg:
            self.curr_max_avg, self.curr_max_avg_node = sum_all / num_all, root
        
        return sum_all, num_all
