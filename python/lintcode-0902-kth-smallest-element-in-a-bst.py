"""
Time: O(n)
Space: O(n)

Reference: https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/solution
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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    
    """
    Solution 2: 类似于 Quick Select 的方式。
                这个算法的好处是，如果多次查询的话，给每个节点统计儿子个数这个过程只需要做一次。查询可以很快。
                时间复杂度 O(n)最好最坏都是。
    """
    def kthSmallest(self, root, k):
        count_dict = {}
        self.countNodes(root, count_dict)
        return self.quickSelect(root, k, count_dict)
        
    def countNodes(self, root, count_dict):
        if root is None:
            return 0
            
        left_count = self.countNodes(root.left, count_dict)
        right_count = self.countNodes(root.right, count_dict)
        count_dict[root] = left_count + right_count + 1
        
        return count_dict[root]
        
    def quickSelect(self, root, k, count_dict):
        if root is None:
            return -1
            
        # corner case handle: root.left could be None 
        left_count = count_dict[root.left] if root.left else 0 
        
        if left_count == k - 1:
            return root.val
        elif left_count > k - 1:
            return self.quickSelect(root.left, k, count_dict)
        else:
            return self.quickSelect(root.right, k - left_count - 1, count_dict)
    
    """
    Solution 1: 使用 Binary Search Tree Iterator 的方式
                （可以参考 binary search tree iterator 那个题）
                用 stack，从第一个点开始，走 k-1 步，就是第 k 个点了。
                时间复杂度是 O(h+k) h 是树的高度。
    
    def kthSmallest(self, root, k):
        # write your code here
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else: # reach leftmost None, pop from stack
                k -= 1
                peak = stack.pop()
                if k == 0:
                    return peak.val
                root = peak.right
    """    
                    
                    
    
                
